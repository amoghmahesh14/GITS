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


def gits_delete(args):
    """
    Please use this functionality with caution since there would be no going back from this.
    This function will delete a commit from the remote branch.
    This functionality is useful when you have commited a mistake to the remote repo and do not
    want it be visible in your commit history.
    """
    print("Hello from GITS command line tools- GITS reset")
    try:
        process1 = subprocess.Popen(
            ['git', 'checkout', args.branch], stdout=PIPE, stderr=PIPE)
        stdout, stderr = process1.communicate()
        process2 = subprocess.Popen(
            ['git', 'reset', '--hard', "HEAD~" + str(args.count)], stdout=PIPE, stderr=PIPE)
        stdout, stderr = process2.communicate()
        process3 = subprocess.Popen(
            ['git', 'push', '--force'], stdout=PIPE, stderr=PIPE)
        stdout, stderr = process3.communicate()
        print('Last ' + str(args.count) + ' commits have been deleted')
    except Exception as e:
        print("ERROR: gits reset command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False
    return True
