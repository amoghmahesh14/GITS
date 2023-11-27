
# GITS 
### GIT Simplified

![GitHub](https://img.shields.io/github/license/pvinoda/GITS)

[![Build Status](https://travis-ci.com/harshitpatel96/GITS.svg?branch=master)](https://travis-ci.com/harshitpatel96/GITS)
[![codecov](https://codecov.io/gh/harshitpatel96/GITS/branch/master/graph/badge.svg?token=G6RG52G2YO)](https://codecov.io/gh/harshitpatel96/GITS/)
![YouTube Video Views](https://img.shields.io/youtube/views/b5-aySJRoMc)

[![DOI](https://zenodo.org/badge/704961751.svg)](https://zenodo.org/doi/10.5281/zenodo.10023186)

![GitHub issues](https://img.shields.io/github/issues/harshitpatel96/GITS)
![GitHub closed issues](https://img.shields.io/github/issues-closed/harshitpatel96/GITS)

[//]: # (![Lines of code]&#40;https://img.shields.io/tokei/lines/github/harshitpatel96/GITS&#41;)



- [Demo](#demo)
- [About GITS](#about-gits)
- [Motivation](#motivation)
- [Improvements](#improvements)
   + [GITS suggestor](#1-gits-suggestor)
   + [GITS recommender](#2-gits-recommender)
   + [GITS stats command](#3-gits-stats-command)
   + [GITS frequency command](#4-gits-frequency-command)
   + [GITS stash functionality](#5-gits-stash-functionality)
- [Successful Usecases](#successful-usecases)
- [Future Scope](#future-scope)
- [Installation](#installation)
    + [Installation for Linux](#installation-for-linux)
    + [Installation for Windows](#installation-for-windows)
- [Documentation](#documentation)
    + [Functions Implemented](#functions-implemented)
    + [Pydoc Implementation](#pydoc-implementation)
- [How to use](#how-to-use)
    + [Use these Commands to harness the power of GITS](#use-these-commands-to-harness-the-power-of-gits) 
    + [How to judge GITS](#how-to-judge-gits)
- [Technologies Used](#technologies-used)
- [Troubleshooting](#troubleshooting)
- [Project Funding](#project-funding)
- [License](#license)
- [How to Contribute](#how-to-contribute)
- [Team Members](#team-members)
- [Recommended citation](#recommended-citation)


# Demo
# [Link to the Video Demo of GITS](https://youtu.be/ger3luJkSdA)

# Intoduction to GITS and Improvements added

https://github.com/amoghmahesh14/GITS/assets/28365724/13544010-ab76-4adc-a651-058e94e43436

# [Scorecard](https://github.com/amoghmahesh14/GITS/blob/master/PROJ3-selfAssessment.md)

[![](https://github.com/pvinoda/GITS/blob/master/GITSvGIT.jpeg)](https://youtu.be/ger3luJkSdA "GITS demo")

## About GITS
GITS simplifies the often cumbersome and confusing commands of git to provide a user friendly experience to beginners in version control, as well as making it time efficient for proficient users. GITS also adds multiple features on top of git functionalities to provide a richer experience. 


## Motivation
Git is the most popular version control system used by developers all around the world. Given its ubiquity, most newbies find it daunting to understand some of the commands in Git.
We aim to simplify some commands by make them more powerful by combining related commands into one intuitive command. We also alleviate confusion in some commands by making them more intuitive.
We hope that these features will help amateurs as well as experienced developers to use git. 

## Improvements

### 1. GITS suggestor
   We provide a capability where the user can learn the command by giving a textual description of what they want to do in simple english.

### 2. GITS recommender
   This functionlaity provides the user with few recommendations. For instance, it tells the user if the the commit messages are too short historically and to improve upon it. It also suggests if the number of lines per commit is too big. The systems considers the best practises and recommends the user on what can be done better.

### 3. GITS stats command
   Wrapper which provides git statistics like number of commits, number of lines, major contributor etc.

### 4. GITS frequency command
   Provides a graphical representation of commit frequency within the repository.

### 5. GITS stash functionality
   Wrapper of git stash command.

### 6. Fixed failing test cases
   Code cov run workflow was failing as there were few test cases that were failing. Fixed such test cases

## Successful Usecases

### Case Study 1: Improving efficiency using GITS

**Background:**
Aditya, a beginner software engineer wants to start developing a software using version control. 

**The Problem:**
Aditya was becoming frustrated and confused with the cumbersome git commands. He wasted lots of time figuring it out.

**The Solution:**
Aditya started using GITS for his development process. He saved lots of time and started to enjoy using version control.

**The Outcome:**
With GITS, Aditya quickly became a professional user of version control tool and started to develop at a much quicker pace than before.

### Technologies Used
* Python
* Tkinter
* Shell

## Installation
### Installation for Linux
1. Clone GITS Repo
2. From the root directory run the following command
    ```
    pip install -r requirements.txt
    ```
3. Go to configurations directory and run the following command

    If you are working on Linux system with a bash terminal or a Windows system using Windows subsystem for linux:
    ```
    bash project_init.sh
    ```
    If you are working on Linux system with a fish terminal:
    ```
    fish project_init.fish
    ```
4. Source the bashrc file
    ```
    source ~/.bashrc
    ```
    
    Note: Open the .bashrc file in User home directory to make sure that the alias command does not have any white spaces in the path. If so, rename the directory to remove the white spaces and re-run the setup.

### Installation for Windows
1. Clone GITS Repo
2. From the root directory run the following command
    ```
    pip install -r requirements.txt
    ```
3. Currently, this project cannot be run on Windows. You need to make use of WSL to work on this project in Windows 
although this fix would only work for systems running Windows 10. If you are using another version of Windows, using a 
virtual machine might be preferred.

    Please refer this link to enable WSL : https://docs.microsoft.com/en-us/windows/wsl/install-win10


# Documentation
## Functions Implemented
These are the functionalities that we have implemented. The links are updated to point to the individual documentation.

1. [gits profile](https://github.com/pvinoda/GITS/blob/phase2_se23_team71/docs/profile.md)
2. [gits rebase](https://github.com/pvinoda/GITS/blob/phase2_se23_team71/docs/rebase.md)
3. [gits stash](https://github.com/pvinoda/GITS/blob/master/docs/stash.md)
4. [gits squash](https://github.com/pvinoda/GITS/blob/master/docs/squash.md)
5. [gits viz](https://github.com/pvinoda/GITS/blob/master/docs/viz.md)
6. [gits reset](https://github.com/pvinoda/GITS/blob/phase2_se23_team71/docs/reset.md)
7. [gits upstream](https://github.com/pvinoda/GITS/blob/phase2_se23_team71/docs/upstream.md)
8. [gits super reset](https://github.com/pvinoda/GITS/blob/phase2_se23_team71/docs/super_reset.md)
9. [gits commit](https://github.com/pvinoda/GITS/blob/phase2_se23_team71/docs/commit.md)
10. [gits create_branch](https://github.com/pvinoda/GITS/blob/phase2_se23_team71/docs/create_branch.md)
11. [gits logging](https://github.com/pvinoda/GITS/blob/phase2_se23_team71/docs/logging.md)
12. [gits undo](https://github.com/pvinoda/GITS/blob/phase2_se23_team71/docs/undo.md)
13. [gits untrack](https://github.com/pvinoda/GITS/blob/phase2_se23_team71/docs/untrack.md)
14. [gits track](https://github.com/pvinoda/GITS/blob/phase2_se23_team71/docs/track.md)
15. [gits delete](https://github.com/pvinoda/GITS/blob/phase2_se23_team71/docs/delete.md)
16. [gits sync](https://github.com/pvinoda/GITS/blob/phase2_se23_team71/docs/sync.md)
17. [gits switch](https://github.com/pvinoda/GITS/blob/phase2_se23_team71/docs/switch.md)
18. [gits status](https://github.com/pvinoda/GITS/blob/phase2_se23_team71/docs/status.md)
19. [gits branch](https://github.com/pvinoda/GITS/blob/phase2_se23_team71/docs/branch.md)
20. [gits diff](https://github.com/pvinoda/GITS/blob/phase2_se23_team71/docs/diff.md)
21. [gits init](https://github.com/pvinoda/GITS/blob/phase2_se23_team71/docs/init.md)
22. [gits merge](https://github.com/pvinoda/GITS/blob/phase2_se23_team71/docs/merge.md)
23. [gits push](https://github.com/pvinoda/GITS/blob/phase2_se23_team71/docs/push.md)
24. [gits pull](https://github.com/pvinoda/GITS/blob/phase2_se23_team71/docs/pull.md)



## Pydoc Implementation
For easier access of Documentation use pydoc, run the following command, it will take you to a browser where you can view the documentation for all the files and directories.

`cd code`<br>
`python3 -m pydoc -b `


This repository is made for CSC 510 Software Engineering Course at NC State University.


## How to use
### Use these Commands to harness the power of GITS
Use these commands to test GITS

- Create a test repo to test all the functionalities.
- Set the git profile name and email to "dummy_name" and "dummy@name.com" respectively. Once they are done,switch it back to the original ones.
- Create two branches with name: branch1 and branch2.
- Add some dummy text files to branch1. Commit these changes with an appropriate commit message.
- Switch to branch2 and add some text files to this branch.
- Use gits viz command without any arguments to visualize the commit history on the terminal
- Compare and contrast the output with gits viz command with arguments. Understand how the image depicts commit history and branch hierarchy.
- Make multiple changes to the file and use gits commit to understand the power of advanced commit functionalities of gits.
- Use gits GUI tool to execute the above commands.
- Make multiple commits and use gits squash to squash all the commits into one single commit. 



### How to judge GITS

1. Does this improve the way you work with git?
2. Did the process of creating a branch, committing, pushing changes and visualising the branch felt easier? 
3. Has the GUI made it easier for you to interact with your repo?
4. Has advanced commit functionality helped you in committing efficiently? Does this functionality make your commit history more intuitive and understanding


## Troubleshooting
If you encounter issues while using GITS, here are some common problems and their solutions:

### Problem 1: Unable to Start the Application

**Symptoms:** The application doesn't start, or you encounter an error when trying to run it.

**Solution:**
1. Ensure you have met the installation requirements mentioned in the README.
2. Double-check that you have the required versions of Python and all requirements installed.
3. Make sure you have executed the initialization script using `./project_init.sh` to install necessary packages.
4. Check for any error messages in the console output and address them accordingly.
5. Its tricky to install tkinter. Install tkinter specific to the version of python you are using.

## Project Funding
Our project is currently not funded and operates on a volunteer and open-source basis. The improvement of the project relies solely on the dedication of our team and contributions from the open-source community.

## License
The project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) license. 

## How to Contribute?
Please see our CONTRIBUTING.md for instructions on how to contribute to the repository and assist us in improving the project.

## Have Questions or Need Assistance?
If you have any questions, need help, or want to provide feedback about the GITS, feel free to contact us at aditya.a.chitlangia@gmail.com.

Your inquiries and suggestions are always welcome!

## Team Members
- Amogh Mahesh
- Aditya Chitlangia
- Abhishek Arun Sheth
- Sachin Rudrappa Doddaguni

## Recommended Citation
GITS Amogh Mahesh, Aditya Chitlangia, Abhishek Arun Sheth, Sachin Rudrappa Doddaguni. 2023.
[https://github.com/amoghmahesh14/GITS]
