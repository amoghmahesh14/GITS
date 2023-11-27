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


def gits_sync(args):
    try:
        untracked_file_check_status = list()
        untracked_file_check_status.append("git")
        untracked_file_check_status.append("status")
        untracked_file_check_status.append("--porcelain")

        process1 = subprocess.Popen(untracked_file_check_status,
                                    stdout=PIPE, stderr=PIPE)

        stdout, stderr = process1.communicate()

        if stdout != b'':
            print("Note: Please commit uncommitted changes")
            return False

        curr_branch = helper.get_current_branch()
        if args.source:
            source_branch = args.source
        else:
            source_branch = helper.get_trunk_branch_name()

        print("Checking out source branch..")
        checkout_master = list()
        checkout_master.append("git")
        checkout_master.append("checkout")
        checkout_master.append(source_branch)
        process2 = subprocess.Popen(checkout_master, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process2.communicate()
        print(stdout.decode('utf-8'))

        print("Pulling Changes from Upstream source branch..")
        pull_upstream = list()
        pull_upstream.append("git")
        pull_upstream.append("pull")
        process3 = subprocess.Popen(pull_upstream, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process3.communicate()
        print(stdout.decode('utf-8'))

        print("Checking out current branch..")
        checkout_current = list()
        checkout_current.append("git")
        checkout_current.append("checkout")
        checkout_current.append(curr_branch)
        process4 = subprocess.Popen(checkout_current, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process4.communicate()
        print(stdout.decode('utf-8'))

        print("Syncing current branch from the updated source branch..")
        rebase_cmd = list()
        rebase_cmd.append("git")
        rebase_cmd.append("rebase")
        rebase_cmd.append(source_branch)
        process5 = subprocess.Popen(rebase_cmd, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process5.communicate()
        print(stdout.decode('utf-8'))

    except Exception as e:
        print("ERROR: gits sync command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False
    return True
