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

import spacy
import tkinter as tk
from tkinter import ttk
from fuzzywuzzy import process
import spacy

nlp = spacy.load("en_core_web_sm")

command_descriptions = {
    "profile": "Change the git account quickly with a single command. Useful for switching between personal and enterprise accounts.",
    "rebase": "Simplified version of git rebase command. Interactively rebase the branch off master, simplifying the process.",
    "stash": "Temporarily save changes in the working directory without committing. Useful for setting aside changes before switching branches.",
    "squash": "Combine multiple related Git commits into a single, cleaner commit. Useful for consolidating small, incremental changes.",
    "viz": "Visualize commit history and branches through a Directed Acyclic Graph (DAG). The graph is stored as a .png file.",
    "reset": "Perform a HARD reset on your branch, making it even with the remote branch. Simplifies the confusion between HARD and SOFT resets.",
    "set upstream": "Set upstream for a local or remote branch. Useful for syncing local and remote branches.",
    "create": "Automatically check out a new branch from local master. Ensures the new branch has all the latest commits before development.",
    "undo": "Update working directory with the last stable commit. Useful when changes after the last commit are problematic.",
    "untrack": "Move files from the staging area to the working directory. Untracked files won't be considered for upcoming commits.",
    "track": "Move files from the working directory to the staging area. Only tracked files are considered for upcoming commits.",
    "delete": "Delete a commit from the remote branch. Use with caution as it permanently removes a commit from history.",
    "sync": "Sync the current branch with upstream master. Ensures the development branch is up-to-date with upstream changes.",
    "switch": "Switch between two branches during implementation. Useful for context switching between different features.",
    "status": "See status about changes in the working directory, staging area, and untracked files.",
    "branch": "List all branches in the repository.",
    "diff": "Display the difference from the last commit. Shows changes made since the last commit.",
    "init": "Transform the current directory into a Git repository or clone an existing repository.",
    "merge": "Merge changes back to the base branch from which you've checked out your personal development branch.",
    "push": "Push local commits to the remote branch. Publishes local changes to the remote repository.",
    "pull": "Pull and merge remote branch into the local branch. Updates the local branch with changes from the remote repository."
}

def suggest_git_command_sarcastic(user_input):
    user_input_doc = nlp(user_input.lower())

    verbs = [token.lemma_ for token in user_input_doc if token.pos_ == "VERB"]
    nouns = [chunk.lemma_ for chunk in user_input_doc.noun_chunks]

    user_keywords = " ".join(verbs + nouns)

    best_match, score = process.extractOne(user_keywords, command_descriptions.keys())

    if score >= 70:
        sarcastic_response = f"Oh, what a coding prodigy! You must know this one already, but try 'gits {best_match}'."
        return sarcastic_response
    else:
        return "Well, your unparalleled brilliance has left me stumped. Could you provide more specific input?"

def suggestion(args):
    global input_entry, output_text  # Declare input_entry and output_text as global variables

    # Create the Tkinter GUI
    root = tk.Tk()
    root.title("Git Command Suggestion")

    label = ttk.Label(root, text="Enter the function you want to perform in a sentence or natural language:")
    label.pack(pady=10)

    input_entry = ttk.Entry(root, width=40)
    input_entry.pack(pady=10)

    # Increase the number of rows in the Entry widget
    input_entry.config(font=('Arial', 12))  # Increase font size
    input_entry.config(width=60, justify='center')  # Adjust width and center text

    def get_suggestion():
        user_input = input_entry.get()
        suggested_command = suggest_git_command_sarcastic(user_input)
        output_text.config(state=tk.NORMAL)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, suggested_command)
        output_text.config(state=tk.DISABLED)

    button = ttk.Button(root, text="Get Suggestion", command=get_suggestion)
    button.pack(pady=10)

    output_text = tk.Text(root, height=5, width=50, wrap=tk.WORD, state=tk.DISABLED)
    output_text.pack(pady=10)

    # Run the Tkinter event loop
    root.mainloop()
