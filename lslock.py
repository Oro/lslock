#!/usr/bin/env python
import os, fcntl, subprocess, stat
import string, random
import click

@click.command()
@click.argument('path', type=click.Path(exists=True))
def display_locked_files(path):
    """Displays all locked files underneath path."""
    click.echo(click.format_filename(path))

def create_locks(directory="/tmp/lslock-test"):
    """Creates some locked files in directory and checks the validity of lslock"""
    pass


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

def create_lock(filename, directory="/tmp/lslock-test"):
    """Creates a locked file filename in directory"""
    if not os.path.exists(directory):
        os.makedirs(directory)
    full_path = os.path.join(directory, filename)
    with open(full_path, "w") as lock_file:
        fcntl.flock(lock_file, fcntl.LOCK_NB|fcntl.LOCK_EX)
        click.echo("Creating lock on {}".format(click.format_filename(full_path)))

def random_string(size=10):
    """Generates a random lowercase string of size"""
    return ''.join(random.choice(string.ascii_lowercase) for x in range(size))

def test():
    assert True

def test_lock_file_creation():
    filename = random_string()
    directory = "/tmp/lsblock-tests"
    create_lock(filename, directory)
    full_path = os.path.join(directory, filename)
    click.echo("Checking if {} exists".format(full_path))
    assert os.path.isfile(full_path)
