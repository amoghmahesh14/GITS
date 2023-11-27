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


def gits_commit_func(args):
    """
    Function that commit files as staged
    in the git command line internface
    Performs operation as similar to git
    commit command. Future additions : user can specify if the commit should be rejected , if the unit test fails.
    """
    try:
        subprocess_command = list()
        subprocess_command.append("git")
        subprocess_command.append("commit")
        commit_message = args.m
        if commit_message == "1":
            new_commit_message = "Update Readme.md"
        elif commit_message == "2":
            new_commit_message = "*** empty log message ***"
        else:
            new_commit_message = commit_message

        if not new_commit_message:
            print("ERROR: gits commit message not present, aborting")
            return False
        subprocess_command.append("-m")
        subprocess_command.append(new_commit_message)
        if not args.amend:
            # do nothing
            pass
        else:
            subprocess_command.append("--amend")

        # print(subprocess_command)
        process = subprocess.Popen(subprocess_command, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        print("your changes committed successfully.")

    except Exception as e:
        print("ERROR: gits commit command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
