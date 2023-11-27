# /usr/bin/python

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


import sys
import argparse
from gits_logging import init_gits_logger
from gits_hello import gits_hello_world
from gits_add import gits_add_func
from gits_commit import gits_commit_func
from gits_set import gits_set_func
from gits_setupstream import upstream
from gits_create_branch import create_branch
from gits_super_reset import super_reset

from gits_rebase import gits_rebase
from gits_reset import gits_reset
from gits_delete import gits_delete

from gits_profile import gits_set_profile
from gits_track import gits_track
from gits_untrack import gits_untrack
from gits_undo import gits_undo
from gits_sync import gits_sync
from gits_push import gits_push
from gits_switch import switch_branch
from gits_merge import merge_branch
from gits_status import gits_status
from gits_diff import gits_diff
from gits_branch import gits_branch
from gits_init import gits_init
from gits_pull import gits_pull
from gits_stash import gits_stash
from gits_stash_apply import gits_stash_apply
from gits_stash_pop import gits_stash_pop
from gits_viz import gits_viz_func
from gits_squash import gits_squash
from gits_stats import gits_stats
from gits_freq import gits_freq
from gits_rec import gits_rec
from gits_suggestion import suggestion

logger_status = init_gits_logger()
if not logger_status:
    print("ERROR: logger not initialised")
    sys.exit(1)

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

gits_hello_subparser = subparsers.add_parser('hello_world')
gits_hello_subparser.set_defaults(func=gits_hello_world)

gits_set_subparser = subparsers.add_parser('set')
gits_set_subparser.add_argument('--parent', help='git parent branch')
gits_set_subparser.set_defaults(func=gits_set_func)

gits_add_subparser = subparsers.add_parser('add')
gits_add_subparser.add_argument('file_names',
                                metavar='N',
                                type=str,
                                nargs='+',
                                help='all file names')
gits_add_subparser.set_defaults(func=gits_add_func)

gits_create_subparser = subparsers.add_parser('create')
gits_create_subparser.add_argument('-b', help="branch name to create")
gits_create_subparser.set_defaults(func=create_branch)

gits_switch_subparser = subparsers.add_parser('switch')
gits_switch_subparser.add_argument('branch_name', help="branch name to switch")
gits_switch_subparser.set_defaults(func=switch_branch)

gits_merge_subparser = subparsers.add_parser('merge')
gits_merge_subparser.add_argument('branch_name', help="branch name to merge")
gits_merge_subparser.set_defaults(func=merge_branch)

gits_upstream_subparser = subparsers.add_parser('upstream')
gits_upstream_subparser.add_argument('--remote',
                                     help='the remote branch name')
gits_upstream_subparser.add_argument('--local',
                                     help="local branch name")
gits_upstream_subparser.add_argument('--upstream',
                                     help="the upstream branch name")
gits_upstream_subparser.set_defaults(func=upstream)

gits_profile_subparser = subparsers.add_parser('profile', help='profie help')
gits_profile_subparser.set_defaults(func=gits_set_profile)
gits_profile_subparser.add_argument('--email',
                                    required=True,
                                    help='email to be used')
gits_profile_subparser.add_argument('--name',
                                    required=True,
                                    help='name to be used')

gits_super_reset_subparser = subparsers.add_parser('super-reset')
gits_super_reset_subparser.add_argument('--name',
                                        help="Name of the repository to super reset")
gits_super_reset_subparser.set_defaults(func=super_reset)

gits_rb_subparser = subparsers.add_parser('rebase', help='sync help')
gits_rb_subparser.set_defaults(func=gits_rebase)

gits_status_subparser = subparsers.add_parser('status', help='sync help')
gits_status_subparser.set_defaults(func=gits_status)

gits_diff_subparser = subparsers.add_parser('diff', help='sync help')
gits_diff_subparser.set_defaults(func=gits_diff)

gits_branch_subparser = subparsers.add_parser('branch', help='sync help')
gits_branch_subparser.set_defaults(func=gits_branch)

gits_reset_subparser = subparsers.add_parser('reset', help='sync help')
gits_reset_subparser.set_defaults(func=gits_reset)
gits_reset_subparser.add_argument(
    '--branch', required=True, help='branch to be used')

gits_reset_subparser = subparsers.add_parser('delete', help='sync help')
gits_reset_subparser.set_defaults(func=gits_delete)
gits_reset_subparser.add_argument(
    '--branch', required=True, help='branch to be used')
gits_reset_subparser.add_argument(
    '--count', required=True, help='Last commits to be deleted')

gits_track_subparser = subparsers.add_parser('track')
gits_track_subparser.add_argument('file_names',
                                  metavar='N',
                                  type=str,
                                  nargs='+',
                                  help='all file names')
gits_track_subparser.set_defaults(func=gits_track)

gits_untrack_subparser = subparsers.add_parser('untrack')
gits_untrack_subparser.add_argument('file_names',
                                    metavar='N',
                                    type=str,
                                    nargs='+',
                                    help='all file names')
gits_untrack_subparser.set_defaults(func=gits_untrack)

gits_undo_subparser = subparsers.add_parser('undo')
gits_undo_subparser.add_argument('file_names',
                                 metavar='N',
                                 type=str,
                                 nargs='+',
                                 help='all file names')
gits_undo_subparser.set_defaults(func=gits_undo)

gits_sync_subparser = subparsers.add_parser('sync')
gits_sync_subparser.add_argument('-source', help="name of the trunk branch")
gits_sync_subparser.set_defaults(func=gits_sync)

gits_push_subparser = subparsers.add_parser('push')
gits_push_subparser.add_argument("--rebase", nargs=1, default=False,
                                 help="do a pull rebase before pushing the changes",
                                 required=False)
gits_push_subparser.set_defaults(func=gits_push)

gits_init_subparser = subparsers.add_parser("init")

gits_init_subparser.add_argument("--bare", action="store_true",
                                 help="intialize an empty git repositories but omit the working directory")
gits_init_subparser.add_argument(
    "--template", help="initialize a git repository using predifined templates")
gits_init_subparser.add_argument(
    "--clone_url", help="url for cloning an already existing repo")
gits_init_subparser.set_defaults(func=gits_init)

gits_pull_subparser = subparsers.add_parser("pull")
gits_pull_subparser.add_argument("--nocommit", action='store_true',
                                 help="fetches the remote contain but does not create a new merge commit",
                                 required=False)
gits_pull_subparser.add_argument("--rebase", action='store_true',
                                 help="uses git rebase to merge with the remote branch",
                                 required=False)
gits_pull_subparser.add_argument("--branch", nargs="?", default=False,
                                 help="you can specify the branch you want to pull",
                                 required=False)
gits_pull_subparser.set_defaults(func=gits_pull)

gits_stash_subparser = subparsers.add_parser("stash")
gits_stash_subparser.set_defaults(func=gits_stash)

gitsh_stash_apply_subparser = subparsers.add_parser("stash_apply")
gitsh_stash_apply_subparser.set_defaults(func=gits_stash_apply)

gitsh_stash_pop_subparser = subparsers.add_parser("stash_pop")
gitsh_stash_pop_subparser.set_defaults(func=gits_stash_pop)

gits_viz_subparser = subparsers.add_parser('viz')
gits_viz_subparser.add_argument('-g', help="flag to visualize branches",required=False,action='store_true')
gits_viz_subparser.add_argument('-f', help="file name for graph output image",required=False)
gits_viz_subparser.add_argument('-s', help="flag to set visualize a simplified graph",required=False,action='store_true')
gits_viz_subparser.set_defaults(func=gits_viz_func)

gits_commit_subparser = subparsers.add_parser('commit')
gits_commit_subparser.add_argument('-m',
                                   required=True,
                                   help='git commit message')


gits_squash_subparser = subparsers.add_parser('squash')
gits_squash_subparser.add_argument('-n',
                                   required=True,
                                   help='number of commits to squash')
gits_squash_subparser.add_argument('-m',
                                   required=True,
                                   help='git squash commit message')

gits_squash_subparser.set_defaults(func=gits_squash)

gits_commit_stats = subparsers.add_parser('stats')
gits_commit_stats.set_defaults(func=gits_stats)

gits_commit_freq = subparsers.add_parser('frequency')
gits_commit_freq.set_defaults(func=gits_freq)

gits_commit_rec = subparsers.add_parser('rec')
gits_commit_rec.set_defaults(func=gits_rec)

gits_commit_rec = subparsers.add_parser('suggest')
gits_commit_rec.set_defaults(func=suggestion)

args = parser.parse_args()
args.func(args)
