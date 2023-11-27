#!/usr/bin/python
# MIT License
#
# Copyright (c) 2023 Amogh Mahesh and others
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from subprocess import PIPE
import subprocess


def get_current_branch():
    """
    This function returns current checked out branch.
    """
    try:
        subprocess_command = list()
        subprocess_command.append("git")
        subprocess_command.append("rev-parse")
        subprocess_command.append("--abbrev-ref")
        subprocess_command.append("HEAD")
        process = subprocess.Popen(
            subprocess_command, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        branch = stdout.decode('UTF-8')
        return branch.rstrip()
    except:
        print("Error occured while getting current branch name!")
        return None


def get_trunk_branch_name():
    """
    This function returns the name of the trunk branch for the project
    """
    try:
        subprocess_command = list()
        subprocess_command.append("git")
        subprocess_command.append("branch")
        process = subprocess.Popen(
            subprocess_command, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        all_branches = stdout.decode('UTF-8')
        list_of_branch_names = all_branches.split()
        list_of_branch_names.remove('*')
        if "master" in list_of_branch_names:
            return "master"
        elif "main" in list_of_branch_names:
            return "main"
        else:
            print("h")
            return list_of_branch_names[0]

    except:
        print("error occured while getting trunk branch name!")
        return None
