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


def switch_branch(args):
    """
    Function that allows user to switch between branches
    """
    try:
        switch_cmd = list()
        switch_cmd.append("git")
        switch_cmd.append("checkout")
        switch_cmd.append(args.branch_name)
        process1 = subprocess.Popen(switch_cmd, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process1.communicate()
        print("Switched to branch:", args.branch_name)

    except Exception as e:
        print("ERROR: gits switch command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
