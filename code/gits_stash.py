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

import subprocess
from subprocess import PIPE
import helper


def gits_stash(args):
    """
    This function is used to execute stash operations and also
    track your stashes easily in a visual manner
    Usage: gits stash
    """
    try:
        stash_decision = input("Do you want to label your stash to identify the contents in future? (Y/N)")
        if stash_decision == "Y":
            stash_label: str = input("Please enter the message label now !!\n")
            stash_executor: list = ["git", "stash", "save", stash_label]
        else:
            stash_executor: list = ["git", "stash"]

        process0 = subprocess.Popen(stash_executor,
                                    stdout=PIPE, stderr=PIPE)
        stdout, stderr = process0.communicate()
        print(stdout.decode("utf-8"))

        if stderr:
            print(f"Error encountered in saving stash file: {stderr}")

        stash_list_executor: list = ["git", "stash", "list"]

        process1 = subprocess.Popen(stash_list_executor, stdout=PIPE,
                                    stderr=PIPE)
        stdout, stderr = process1.communicate()

        print("Here's what your current stash looks like...\n")
        print(stdout.decode("utf-8"))

    except Exception as e:
        print("ERROR: gits stash command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
