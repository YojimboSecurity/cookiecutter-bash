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

def remove_dir(dirname: str):
    """
    generic remove directory from project dir
    
    Args:
        dirname (str): name of the directory to remove
    """
    fullpath = os.path.join(PROJECT_DIRECTORY, dirname)
    if os.path.exists(fullpath):
        shutil.rmtree(fullpath)

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

if "{{ cookiecutter.add_docs }}".lower() == "n":
    remove_dir("docs")
if "{{ cookiecutter.use_lib }}".lower() == "n":
    remove_dir("lib")
if "{{ cookiecutter.use_git }}".lower() == "y":
    init_git()
else:
    remove_file(".gitignore")