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

from subprocess import Popen, PIPE


def gits_init(args):
    """
    This function allows user to transform current
    directory into a Git repository.
    There are three ways to do it.
    1) Simple git init
         gits init
    2) Initialize with a bare flag
         gits init --bare
    3) Initialize using a preexisting template
         gits init --template path-to-template
    """
    try:
        if args.clone_url:
            process_commands = ["git", "clone", args.clone_url]
        else:
            process_commands = ["git", "init"]
            if args.bare is not False and args.bare is not None:
                process_commands.append("--bare")
            elif args.template is not None:
                process_commands.append("--template")
                process_commands.append(args.template)

        process = Popen(process_commands, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        print(stdout.decode("UTF-8"))

    except Exception as e:
        print("ERROR: gits init command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
