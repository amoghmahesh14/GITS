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

import logging
import os
import sys
from pathlib import Path
from logging.handlers import TimedRotatingFileHandler

gits_logger = None


def init_gits_logger():
    """
    Function that initializes gits logger and creates a
    handler to be used consequently
    """
    try:
        global gits_logger
        # format the log entries
        formatter = logging.Formatter(
            '%(asctime)s %(name)s %(levelname)s %(message)s')

        user_home_dir = str(Path.home())
        gits_logs_dir = os.path.join(user_home_dir, ".gits", "logs")

        # checking if logs directory exist or not
        if os.path.isdir(gits_logs_dir):
            # do nothing
            pass
        else:
            print("gits project not initialised, run project_init.sh "
                  "script from configurations to initialize the project")
            sys.exit(1)

        gits_logs_filename = os.path.join(gits_logs_dir, "gits.log")
        handler = TimedRotatingFileHandler(gits_logs_filename,
                                           when='midnight',
                                           backupCount=10)

        handler.setFormatter(formatter)
        gits_logger = logging.getLogger(__name__)
        gits_logger.addHandler(handler)
        gits_logger.setLevel(logging.DEBUG)
        return True
    except Exception as e:
        print("ERROR: Caught exception {}".format(str(e)))
        return False
