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


import gits_logging
from subprocess import PIPE
import subprocess


def gits_undo(args):
    """
    Function that moves files from working directory to the staging directory.
    Only tracked files will be considered for any upcoming files.
    """
    try:
        subprocess_command = list()
        subprocess_command.append("git")
        subprocess_command.append("checkout")
        file_names_list = args.file_names
        total_files = len(file_names_list)
        if total_files != 0:
            for i in range(0, total_files):
                subprocess_command.append(file_names_list[i])
            process = subprocess.Popen(
                subprocess_command, stdout=PIPE, stderr=PIPE)
            stdout, stderr = process.communicate()

    except Exception as e:
        gits_logging.gits_logger.error("gits undo command caught an exception")
        gits_logging.gits_logger.error("{}".format(str(e)))
        print("ERROR: gits undo command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
