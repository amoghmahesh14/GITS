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


def upstream(args):
    """
    Function that modifies the upstream repository.
    It will set upstream for a local branch to a remote branch.
    It can also be used to set upstream for a remote branch to
    the original branch in case of a forked repo.
    """
    try:
        # Case of adding upstream to a local branch.
        if args.remote and args.local:
            local_to_remote_command = list()
            local_to_remote_command.append("git")
            local_to_remote_command.append("branch")
            local_to_remote_command.append(
                "--set-upstream-to=origin/" + args.remote)
            local_to_remote_command.append(args.local)
            # print(local_to_remote_command)
            process = subprocess.Popen(local_to_remote_command,
                                       stdout=PIPE, stderr=PIPE)
            stdout, stderr = process.communicate()

        # Case of adding upstream to the remote repo.
        # It will be tracking a forked repo then.
        elif args.upstream:

            # first we have to check if the upstream is set or not
            check_upstream_command = list()
            check_upstream_command.append("git")
            check_upstream_command.append("config")
            check_upstream_command.append("remote.upstream.url")

            process1 = subprocess.Popen(check_upstream_command,
                                        stdout=PIPE, stderr=PIPE)
            stdout, stderr = process1.communicate()

            print(stdout)
            # if this exists we need to update with the
            # newly given value as follows
            if stdout:
                remote_upstream_command = list()
                remote_upstream_command.append("git")
                remote_upstream_command.append("remote")
                remote_upstream_command.append("set-url")
                remote_upstream_command.append("upstream")
                remote_upstream_command.append(args.upstream)

                process2 = subprocess.Popen(remote_upstream_command,
                                            stdout=PIPE, stderr=PIPE)
                stdout, stderr = process2.communicate()

            # else we just add the new value
            else:
                remote_upstream_command = list()
                remote_upstream_command.append("git")
                remote_upstream_command.append("remote")
                remote_upstream_command.append("add")
                remote_upstream_command.append("upstream")
                remote_upstream_command.append(args.upstream)

                process3 = subprocess.Popen(remote_upstream_command,
                                            stdout=PIPE, stderr=PIPE)
                stdout, stderr = process3.communicate()

    except Exception as e:
        print("ERROR: gits commit command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
