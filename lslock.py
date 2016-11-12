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

def create_lock(directory="/tmp/lslock-test"):
    """Creates a locked file in directory"""
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_name = os.path.join(directory, random_string())
    with open(file_name, "w") as lock_file:
        fcntl.flock(lock_file, fcntl.LOCK_NB|fcntl.LOCK_EX)
        click.echo("Creating lock on " + click.format_filename(file_name))

def random_string(size=10):
    """Generates a random lowercase string of size"""
    return ''.join(random.choice(string.ascii_lowercase) for x in range(size))

def test():
    assert True
