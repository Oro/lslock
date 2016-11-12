#!/usr/bin/env python
from setuptools import setup

setup(
    name='lslock',
    version='0.1',
    py_modules=['lslock'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        lslock=lslock:display_locked_files
    ''',
)
