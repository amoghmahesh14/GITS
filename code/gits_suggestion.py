import spacy
from fuzzywuzzy import process

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

# Function to suggest git command based on user input using detailed descriptions with a sarcastic touch
def suggest_git_command_sarcastic(user_input):
    user_input_doc = nlp(user_input.lower())

    # Extract lemmatized verbs and nouns from user input
    verbs = [token.lemma_ for token in user_input_doc if token.pos_ == "VERB"]
    nouns = [chunk.lemma_ for chunk in user_input_doc.noun_chunks]

    # Combine verbs and nouns for matching
    user_keywords = " ".join(verbs + nouns)

    # Find the most similar command based on user keywords
    best_match, score = process.extractOne(user_keywords, command_descriptions.keys())

    if score >= 70:
        sarcastic_response = f"Oh, what a coding prodigy! You must know this one already, but try 'gits {best_match}'."
        return sarcastic_response
    else:
        return "Well, your unparalleled brilliance has left me stumped. Could you provide more specific input?"

def suggestion(args):
    user_input = input("Enter the function you want to perform in a sentence or natural language: ")
    suggested_command = suggest_git_command_sarcastic(user_input)
    print(suggested_command)
