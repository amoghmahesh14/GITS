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


import os
from subprocess import check_output
import shutil


def super_reset(args):
    """
    Function that removes the local repository
    and does a fresh clone.
    This command should be run in the directory
    which consists your git repository.
    It takes the name of the git repository as a parameter
    """
    try:
        if not args.name:
            print("Required parameters are not provided. "
                  "Please add --name parameter.")
            return False
        os.chdir("./" + args.name)
        remote_loc = check_output(["git", "config", "remote.origin.url"])

        if not remote_loc:
            print("Remote location not found. Update git config")
            return False

        remote_loc = remote_loc.strip().decode("utf-8")
        os.chdir("../")
        print("Removing the current repository...")
        shutil.rmtree(args.name)
        print("Freshly cloning...")
        check_output(["git", "clone", remote_loc])

    except Exception as e:
        print("ERROR: gits super reset command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
