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


def gits_reset(args):
    """'Reset' intuitively means a HARD reset.
    This functionality does a HARD reset on your branch, and makes it even with the remote branch.
    This aims to simplify the confusion between HARD and the SOFT reset."""
    print("Hello from GITS command line tools- GITS reset")
    try:
        process1 = subprocess.Popen(
            ['git', 'checkout', args.branch], stdout=PIPE, stderr=PIPE)
        stdout, stderr = process1.communicate()
        # print(stdout)
        process2 = subprocess.Popen(
            ['git', 'reset', '--hard', args.branch], stdout=PIPE, stderr=PIPE)
        stdout, stderr = process2.communicate()
        print("Current branch reset successful.")
    except Exception as e:
        print("ERROR: gits reset command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False
    return True
