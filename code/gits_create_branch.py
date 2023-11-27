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
import helper
import subprocess


def create_branch(args):
    """
    Function that creates a new local branch
    from local master after updating local master
    from remote master. The idea here is that the new branch should have all the latest commits.
    """
    try:
        # checkout main/master first
        checkout_master = list()
        checkout_master.append("git")
        checkout_master.append("checkout")
        checkout_master.append(helper.get_trunk_branch_name())
        process1 = subprocess.Popen(checkout_master, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process1.communicate()

        # update with remote
        update_master = list()
        update_master.append("git")
        update_master.append("pull")
        process2 = subprocess.Popen(update_master, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process2.communicate()

        # checkout new branch
        if not args.b:
            print("Name of new branch not provided. Use -b branchName")
            return False
        checkout_feature = list()
        checkout_feature.append("git")
        checkout_feature.append("checkout")
        checkout_feature.append("-b")
        checkout_feature.append(args.b)
        process3 = subprocess.Popen(checkout_feature, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process3.communicate()
        print("Branch created successfully. Currently you are on branch:", args.b)

    except Exception as e:
        print("ERROR: gits create command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
