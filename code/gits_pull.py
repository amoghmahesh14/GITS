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


def gits_pull(args):
    """
    This function is used to pull remote branch and
    merge it into local branch.
    Usage: gits pull
           gits pull --no-commit
           gits pull --rebase
           gits pull --verbose
    """
    try:
        untracked_file_check_status = ["git", "status", "--porcelain"]
        process0 = subprocess.Popen(untracked_file_check_status,
                                    stdout=PIPE, stderr=PIPE)
        stdout, stderr = process0.communicate()
        print(stdout.decode("utf-8"))

        if stdout != b'':
            print("Note: Please commit uncommited changes before pulling")
            return False

        arguments = []
        curr_branch = helper.get_current_branch()
        if args.nocommit is True and args.rebase is True:
            print("You cannot use both nocommit and rebase at the same time")
            return False
        elif args.nocommit is True:
            arguments += ["--no-commit"]
        elif args.rebase is True:
            arguments += ["--rebase"]

        if args.branch is not False and args.branch is not None:
            arguments += [args.branch]
        else:
            arguments += [curr_branch]

        pull_command = ["git", "pull"] + ["origin"] + arguments
        process1 = subprocess.Popen(pull_command, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process1.communicate()
        print(stdout.decode("utf-8"))

    except Exception as e:
        print("ERROR: gits pull command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
