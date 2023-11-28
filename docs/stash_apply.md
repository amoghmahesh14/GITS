# About gits stash apply
The `git stash apply` command in Git serves the purpose of reapplying changes that have been stashed using the `git stash` command. When you stash changes, Git saves your modifications in a temporary area, allowing you to switch to a different branch or perform other tasks without committing the changes immediately. The `git stash apply` command is then used to bring back those stashed changes to your working directory. It allows you to reintegrate the saved changes without removing them from the stash. This operation can be particularly useful when you want to continue working on a feature or bugfix that was temporarily set aside. The command is executed in the context of the current branch, and it ensures that the stashed changes are applied to the files in your working directory, updating your codebase accordingly.

# Location of Code
The code that implements the abovementioned gits functionality is located [here](https://github.com/amoghmahesh14/GITS/blob/master/code/gits_stash_apply.py).

# Code Description
The gits stash aaply applies the top most available stash on the stack to the current working branch. If there is an error while applying stash it is displayed to the user, so that it can be resolved.

## Functions
1. gits_stash_apply(args):
The `gits_stash_apply` function is a Python script that simplifies Git stash application management. It allows users to readily apply their latest stashed changes and simplify their work process.

# How to run it? (Small Example)
Use the command in following way to apply your stashed changes.
```
$ gits stash_apply

```