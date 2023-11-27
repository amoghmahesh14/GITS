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

import os
import subprocess

def run_git_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout.strip()

def colorize_text(text, color, background_color):
    color_code = f"\033[{color};{background_color}m"
    reset_code = "\033[0m"
    return f"{color_code}{text}{reset_code}"

def average_lines_per_commit():
    git_log_command = "git log --numstat --format=%B"
    commit_messages = run_git_command(git_log_command).split('\n\n')

    lines_changed = []
    commit_messages_less_than_20 = 0
    commit_messages_greater_than_50 = 0

    for message in commit_messages:
        for line in message.split('\n'):
            if line.strip() and line.split('\t')[0].isdigit():
                lines_changed.append(int(line.split('\t')[0]))

        message_length = len(message.strip())

        if message_length < 20:
            commit_messages_less_than_20 += 1
        elif message_length > 50:
            commit_messages_greater_than_50 += 1

    if lines_changed:
        average_lines = round(sum(lines_changed) / len(lines_changed))
        return average_lines, commit_messages_less_than_20, commit_messages_greater_than_50
    else:
        return 0, 0, 0

def recommend_average_lines():
    average_lines, less_than_20, greater_than_50 = average_lines_per_commit()

    recommendations = []

    if average_lines > 50:
        recommendations.append(colorize_text("\nRecommendation 1. The average number of lines per commit is high. Consider smaller, more focused commits.", 91, 40))  # Red background
    else:
        recommendations.append(colorize_text("\nRecommendation 1. The average number of lines per commit is within a reasonable range.", 92, 40))  # Green background

    if less_than_20 > greater_than_50:
        recommendations.append(colorize_text("\nRecommendation 2. The commit messages are observed to be not descriptive. Be more descriptive in your commit messages.", 91, 40))  # Red background
    elif greater_than_50 > less_than_20:
        recommendations.append(colorize_text("\nRecommendation 2. The commit messages are observed to be too lengthy. Consider being more concise in your commit messages.", 91, 40))  # Red background

    return '\n'.join(recommendations), average_lines

def gits_rec(args):
    repo_path = os.getcwd()

    recommendation, average_lines = recommend_average_lines()
    print(f"{recommendation}")