
# GITS 
### GIT Simplified

![GitHub](https://img.shields.io/github/license/pvinoda/GITS)

[![Build Status](https://travis-ci.com/harshitpatel96/GITS.svg?branch=master)](https://travis-ci.com/harshitpatel96/GITS)
[![codecov](https://codecov.io/gh/harshitpatel96/GITS/branch/master/graph/badge.svg?token=G6RG52G2YO)](https://codecov.io/gh/harshitpatel96/GITS/)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10212028.svg)](https://doi.org/10.5281/zenodo.10212028)

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
   + [Fixed Failing Test Cases](#6-fixed-failing-test-cases)
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

# [Scorecard](https://github.com/amoghmahesh14/GITS/blob/master/PROJ3-selfAssessment.md)

# Introduction to GITS and Improvements added

https://github.com/amoghmahesh14/GITS/assets/28365724/13544010-ab76-4adc-a651-058e94e43436

## About GITS
GITS simplifies the often cumbersome and confusing commands of git to provide a user friendly experience to beginners in version control, as well as making it time efficient for proficient users. GITS also adds multiple features on top of git functionalities to provide a richer experience. 


## Motivation
Git is the most popular version control system used by developers all around the world. Given its ubiquity, most newbies find it daunting to understand some of the commands in Git.
We aim to simplify some commands by make them more powerful by combining related commands into one intuitive command. We also alleviate confusion in some commands by making them more intuitive.
We hope that these features will help amateurs as well as experienced developers to use git. 

## Improvements

### 1. GITS Suggestor
The GITS Suggestor is a pivotal feature designed to elevate the user experience. It empowers users to learn and execute commands through    straightforward English descriptions. This functionality is particularly beneficial for beginners grappling with Git commands and serves as a convenient quick reference for proficient users.

### 2. GITS Recommender
Going beyond mere command simplification, the GITS Recommender actively guides users toward best practices. By analyzing historical commit data, it provides insightful recommendations for enhancing commit messages and optimizing the number of lines per commit. This proactive approach fosters adherence to Git best practices, thereby elevating the overall quality of version control.

### 3. GITS Stats Command
The GITS Stats Command acts as a comprehensive wrapper, offering users detailed statistics about their Git repository. This includes vital information such as the number of commits, lines of code, and major contributors. This feature streamlines the process of obtaining crucial repository insights, facilitating informed decision-making for developers.

### 4. GITS Frequency Command
Introducing a graphical representation of commit frequency within the repository, the GITS Frequency Command enhances user understanding of commit patterns over time. This visual aid is instrumental in improving project management and coordination among team members.

### 5. GITS Stash Functionality
Serving as a wrapper for the Git stash command, the GITS Stash Functionality simplifies the process of temporarily saving changes. This enhancement makes the stash feature more accessible and user-friendly, catering to both beginners and experienced developers.

### 6. Fixed Failing Test Cases
The commitment to code quality and reliability is evident in the resolution of failing test cases. By addressing these issues, GITS ensures a more robust and stable codebase, instilling confidence in users regarding the tool's reliability. This dedication to bug resolution significantly contributes to the overall improvement of the GITS project.

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

### Case Study 2: Streamlining Development with GITS Innovations

**Background:**
Abhishek, an experienced software developer, leads a team in a fast-paced development environment. The team faces challenges in maintaining a consistent and optimized version control process.

**The Problem:**
Abhishek and his team often encountered difficulties in ensuring adherence to Git best practices. Commit messages were inconsistent, and optimizing the commit size for better traceability became a cumbersome task. This led to inefficiencies and occasional errors in the development workflow.

**The Solution:**
Incorporating the newly added features, GITS Suggestor and GITS Recommender, Abhishek's team experienced a transformative shift in their development process. The GITS Suggestor provided an accessible interface for both beginners and seasoned developers, allowing them to understand and execute Git commands effortlessly. This eliminated the need for extensive command memorization, saving valuable time.

Moreover, the GITS Recommender took their version control to the next level. By analyzing historical commit data, it offered tailored recommendations to improve commit messages and optimize the size of each commit. This proactive guidance not only enhanced the quality of version control but also promoted consistency and traceability across the team's projects.

**The Outcome:**
With GITS innovations in place, Abhishek's team observed a remarkable increase in efficiency and code quality. Developers, whether new or experienced, found it easier to collaborate seamlessly using version control. The streamlined workflow facilitated faster development cycles, as the GITS Recommender ensured that best practices were consistently followed. The result was a more cohesive and productive development environment, with Abhishek's team delivering high-quality software at an accelerated pace.

## Future Scope
### 1. Integration with Emerging Git Features:
Stay abreast of updates and new functionalities in Git and seamlessly integrate them into GITS. This ensures that users have access to the latest and most advanced version control capabilities.
### 2. Smart Notifications and Alerts:
Implement intelligent notification systems that alert users to potential issues, best practices, or critical updates in their repositories. This feature could contribute to a more proactive and informed version control process.
### 3. User-Configurable Workflows:
Allow users to customize and define their own version control workflows within GITS. This flexibility can cater to diverse project structures and development methodologies.
### 4. Advanced Visualization Techniques:
Evolve the GITS Frequency Command by incorporating more advanced visualization techniques, such as network graphs or interactive visual representations, to offer users a deeper understanding of their project's commit history.

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

1. [gits profile](https://github.com/amoghmahesh14/GITS/blob/master/docs/profile.md)
2. [gits rebase](https://github.com/amoghmahesh14/GITS/blob/master/docs/rebase.md)
3. [gits stash](https://github.com/amoghmahesh14/GITS/blob/master/docs/stash.md)
4. [gits squash](https://github.com/amoghmahesh14/GITS/blob/master/docs/squash.md)
5. [gits viz](https://github.com/amoghmahesh14/GITS/blob/master/docs/viz.md)
6. [gits reset](https://github.com/amoghmahesh14/GITS/blob/master/docs/reset.md)
7. [gits upstream](https://github.com/amoghmahesh14/GITS/blob/master/docs/upstream.md)
8. [gits super reset](https://github.com/amoghmahesh14/GITS/blob/master/docs/super_reset.md)
9. [gits commit](https://github.com/amoghmahesh14/GITS/blob/master/docs/commit.md)
10. [gits create_branch](https://github.com/amoghmahesh14/GITS/blob/master/docs/create_branch.md)
11. [gits logging](https://github.com/amoghmahesh14/GITS/blob/master/docs/logging.md)
12. [gits undo](https://github.com/amoghmahesh14/GITS/blob/master/docs/undo.md)
13. [gits untrack](https://github.com/amoghmahesh14/GITS/blob/master/docs/untrack.md)
14. [gits track](https://github.com/amoghmahesh14/GITS/blob/master/docs/track.md)
15. [gits delete](https://github.com/amoghmahesh14/GITS/blob/master/docs/delete.md)
16. [gits sync](https://github.com/amoghmahesh14/GITS/blob/master/docs/sync.md)
17. [gits switch](https://github.com/amoghmahesh14/GITS/blob/master/docs/switch.md)
18. [gits status](https://github.com/amoghmahesh14/GITS/blob/master/docs/status.md)
19. [gits branch](https://github.com/amoghmahesh14/GITS/blob/master/docs/branch.md)
20. [gits diff](https://github.com/amoghmahesh14/GITS/blob/master/docs/diff.md)
21. [gits init](https://github.com/amoghmahesh14/GITS/blob/master/docs/init.md)
22. [gits merge](https://github.com/amoghmahesh14/GITS/blob/master/docs/merge.md)
23. [gits push](https://github.com/amoghmahesh14/GITS/blob/master/docs/push.md)
24. [gits pull](https://github.com/amoghmahesh14/GITS/blob/master/docs/pull.md)
25. [gits stash apply](https://github.com/amoghmahesh14/GITS/blob/master/docs/stash_apply.md)
26. [gits stash pop](https://github.com/amoghmahesh14/GITS/blob/master/docs/stash_pop.md)
27. [gits rec](https://github.com/amoghmahesh14/GITS/blob/master/docs/recommender.md)
28. [gits suggest](https://github.com/amoghmahesh14/GITS/blob/master/docs/suggestion.md)
29. [gits freq](https://github.com/amoghmahesh14/GITS/blob/master/docs/freq.md)



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
