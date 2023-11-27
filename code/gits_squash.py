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


def gits_squash(args):
    """
        This function is used to execute squash the last few commits into a single commit.
        Usage: gits squash -n numberOfCommits -m message ; where N is the last number of commits to squash together
        """
    try:
        subprocess_squash_executor = list()
        subprocess_squash_executor.append("git")
        subprocess_squash_executor.append("reset")
        subprocess_squash_executor.append("--soft")
        squashed_commit_message = args.m
        squash_number = args.n

        print(squashed_commit_message)
        print(squash_number)
        if not squashed_commit_message:
            print("ERROR: gits commit message not present, aborting")
            return False

        if not squash_number:
            print("ERROR: please provide the number of commits you want to squash")
        subprocess_squash_executor.append("reset")
        subprocess_squash_executor.append(f"HEAD~{squash_number}")

        process1 = subprocess.Popen(subprocess_squash_executor, stdout=PIPE,
                                    stderr=PIPE)
        stdout, stderr = process1.communicate()
        print(stdout.decode("utf-8"))

        # staging changes
        subprocess_stager = list()
        subprocess_stager.append("git")
        subprocess_stager.append("add")
        subprocess_stager.append(".")

        process2 = subprocess.Popen(subprocess_stager, stdout=PIPE,
                                    stderr=PIPE)
        stdout_add, stderr1_add = process2.communicate()
        print(stdout_add)

        fresh_commiter = list()
        fresh_commiter.append("git")
        fresh_commiter.append("commit")
        fresh_commiter.append("-m")
        fresh_commiter.append(squashed_commit_message)

        process2 = subprocess.Popen(fresh_commiter, stdout=PIPE,
                                    stderr=PIPE)
        stdout1, stderr1 = process2.communicate()
        print(stdout1.decode("utf-8"))
        print("Squash completed. Please check your new git log now.")

    except Exception as e:
        print("ERROR: gits squash command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
