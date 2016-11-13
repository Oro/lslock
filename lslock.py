#!/usr/bin/env python
import os, fcntl, subprocess, stat
import string, random
import click
import time
from multiprocessing import Process
import logging


@click.command()
@click.argument('directory', type=click.Path(exists=True), default="/tmp/lslock-test")
@click.option('--verbose', '-v', default=False, is_flag=True, help='Enable verbose output')
def display_locked_files(directory, verbose):
    """Displays all locked files underneath directory."""
    if verbose:
        logging.basicConfig(level=logging.DEBUG)

    logging.info('Checking for locks on %s' % click.format_filename(directory))
    locks = locked_files_in_dir(directory)
    logging.info('Found following locks: {}'.format(locks))
    for lock in locks:
        click.echo('File {} is locked by PID {}'.format(click.format_filename(lock.get('filepath')), lock.get('pid')))
    if not locks:
        click.echo('Found no locked files')

@click.command()
@click.argument('directory', type=click.Path(exists=True), default="/tmp/lslock-test")
@click.option('--number', '-n', default=5, help='How many lock files are generated')
@click.option('--verbose', '-v', default=False, is_flag=True, help='Enable verbose output')
def create_locks(directory, verbose, number):
    """Creates some locked files in directory and checks the validity of lslock"""
    if verbose:
        logging.basicConfig(level=logging.DEBUG)

    for i in range(0,number):
        full_path = os.path.join(directory,str(i))
        p = Process(target=create_lock, args=(full_path,))
        p.start()

    p.join()
    click.echo("All done!")

def create_lock(full_path):
    with open(full_path, "w") as file_to_lock:
        lock_file(file_to_lock)
        check_is_locked_file(full_path)

def locked_files_in_dir(directory):
    """Returns a tuple of dicts of all filepaths in directory that are currently locked"""
    all_locks = {}
    locked_files = []
    files_in_directory = inodes_in_dir(directory)
    with open("/proc/locks", "r") as locks:
        for line in locks:
            pid = line.split()[4] # The fifth position holds the pid of the process locking the file
            inode = line.split()[5] # The sixth position which has the format MAJOR-DEVICE:MINOR-DEVICE:INODE-NUMBER
            inode = inode.split(":")[2] # we are only interested in the inode number, so we split it on : and get the third one
            all_locks[int(inode)] = int(pid)

    # logging.info("Here are all currently locked inodes with their PID: {}".format(all_locks))
    # The intersection of all locks and the locks in the specified directory is what we want
    intersection = set(all_locks) & set(files_in_directory)

    logging.info("All current locks: {}".format(all_locks))
    # to get a dict with both pid and filepath, we need to append the pid we got from /proc/locks and the associated filepath from the file inside the directory
    for lock in intersection:
        locked_files.append({'pid': all_locks[lock], 'filepath': files_in_directory[lock]})
    return locked_files

def inodes_in_dir(directory):
    """Descent into directory and return a dict of all inodes with their filepath"""
    inode_dict = {}
    for filepath in files_in_dir(directory):
        inode_dict[os.stat(filepath).st_ino] = filepath
    return inode_dict


def files_in_dir(directory):
    """Returns all files in directory and its subdirectories
    If a file is given, return the file"""
    file_paths = []

    if os.path.isfile(directory):
        file_paths.append(directory)
    else:
        for root, directories, files in os.walk(directory):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)
    return file_paths

def lock_file(file_to_lock):
    """locks the passed file"""
    fcntl.flock(file_to_lock, fcntl.LOCK_NB|fcntl.LOCK_EX)
    logging.info("Creating lock on {}".format(file_to_lock))

def random_string(size=10):
    """Generates a random lowercase string of size"""
    return ''.join(random.choice(string.ascii_lowercase) for x in range(size))

def test_file_to_lock_creation():
    filename = random_string()
    directory = "/tmp/lslock-test"
    full_path = os.path.join(directory, filename)
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(full_path, "w") as file_to_lock:
        lock_file(file_to_lock)
    logging.info("Checking if {} exists".format(full_path))
    assert os.path.isfile(full_path)

def check_is_locked_file(full_path):
    assert is_locked(full_path)

def check_is_unlocked_file(full_path):
    assert not is_locked(full_path)

def is_locked(full_path):
    logging.info("Checking if {} is locked.".format(full_path))
    locks = locked_files_in_dir(full_path)
    if not locks:
        return []
    lock = [lock for lock in locks if lock.get('filepath') == full_path]
    logging.info("Found lock on {}".format( lock))
    return lock

def test_five_locked_files():
    directory = "/tmp/lslock-test"
    if not os.path.exists(directory):
        os.makedirs(directory)
    for i in range(0, 5):
        full_path = os.path.join(directory,str(i))
        with open(full_path, "w") as file_to_lock:
            lock_file(file_to_lock)
            locks = locked_files_in_dir(full_path)
            logging.info(locks)
            yield check_is_locked_file, full_path

def test_five_unlocked_files():
    directory = "/tmp/lslock-test"
    if not os.path.exists(directory):
        os.makedirs(directory)
    for i in range(0,5):
        full_path = os.path.join(directory,str(i))
        with open(full_path, "w") as unfile_to_lock:
            locks = locked_files_in_dir(full_path)
            logging.info(locks)
            yield check_is_unlocked_file, full_path

