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


def gits_rebase(args):
    """This is a highly simplified version of git rebase command.
    This interactive command asks for the branch that you want to rebase and automatically rebases it off master.
    This is the most common scenario. The original GIT rebase command is a little un-intuitive and there is always a
    confusion , about the source branch and the destination branch.
"""
    try:
        print("Is the rebase on current branch?")
        inp = input("[yes/no][y/n]")
        if inp.lower() == "yes" or inp.lower() == "y":
            process1 = subprocess.Popen(
                ['git', 'rebase', helper.get_trunk_branch_name()], stdout=PIPE, stderr=PIPE)
            stdout, stderr = process1.communicate()
            print(stdout.decode("UTF-8"))
        else:
            inp2 = input("Enter the name of the branch you want to rebase: ")
            print(inp, inp2)
            process2 = subprocess.Popen(['git', 'checkout', inp2, 'git', 'rebase', helper.get_trunk_branch_name()],
                                        stdout=PIPE, stderr=PIPE)
            stdout, stderr = process2.communicate()
            print(stdout.decode("UTF-8"))
    except Exception as e:
        print("ERROR: gits reset command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False
    return True
