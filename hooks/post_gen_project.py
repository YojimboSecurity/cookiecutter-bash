# -*- coding: utf-8 -*-
"""post_gen_project.py: Post generation script for cookiecutter

This module is executed after the project is generated and can be used to make
post-generation modifications to the project directory.

This module does the following:
    - initializes a git repository

.. Python Style Guide:
    https://google.github.io/styleguide/pyguide.html
"""
from __future__ import print_function
import os
import shutil
from subprocess import Popen

# Get the root project directory
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

def remove_file(filename: str):
    """
    generic remove file from project dir
    
    Args:
        filename (str): name of the file to remove
    """
    fullpath = os.path.join(PROJECT_DIRECTORY, filename)
    if os.path.exists(fullpath):
        os.remove(fullpath)

def init_git():
    """
    initializes git on the new project folder
    """
    GIT_COMMANDS = [
        ["git", "init"],
        ["git", "add", "."],
        ["git", "commit", "-a", "-m", "Initial Commit."]
    ]

    for command in GIT_COMMANDS:
        git = Popen(command, cwd=PROJECT_DIRECTORY)
        git.wait()

if "{{ cookiecutter.init_git }}" == "y":
    init_git()
else:
    remove_file(".gitignore")