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


def gits_push(args):
    """
    This function is used to push local changes to remote branch.
    Usage: gits push
    """
    try:
        untracked_file_check_status = ["git", "status", "--porcelain"]
        process0 = subprocess.Popen(untracked_file_check_status,
                                    stdout=PIPE, stderr=PIPE)

        stdout, stderr = process0.communicate()
        print(stdout.decode("utf-8"))

        if stdout != b'':
            print("Note: Please commit uncommited changes")
            return False

        _ = helper.get_current_branch()

        if args.rebase is not False:
            print("Pulling changes from Upstream source branch and rebasing it")
            pull_rebase = ["git", "pull", "--rebase", "origin", args.rebase]
            process1 = subprocess.Popen(pull_rebase, stdout=PIPE, stderr=PIPE)
            stdout, stderr = process1.communicate()
            print(stdout.decode("utf-8"))

        print("Pushing local commits")
        push_commits = ["git", "push"]
        process2 = subprocess.Popen(push_commits, stdout=PIPE, stderr=PIPE)

        stdout, stderr = process2.communicate()
        print(stdout.decode("utf-8"))

    except Exception as e:
        print("ERROR: gits push command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
