# Gite
![](https://img.shields.io/badge/Release-V1.0.0-blue.svg) ![](https://img.shields.io/badge/Build-Stable-green.svg) [![License: MPL 2.0](https://img.shields.io/badge/License-MPL%202.0-brightgreen.svg)](https://opensource.org/licenses/MPL-2.0) ![](https://img.shields.io/badge/By-Abhishek%20Sarkar-red.svg?style=social&logo=appveyor)

------------


Hi, git users!

As we know **git** is already a powerful tool for version controlling. Yet, while we do our regular git activities, we feel sometimes that some features are ***good to have***  for many, if not for all, for convenience of work. **gite** brings you those features.

## Prerequisites

You should have a Python v3.0+ installed in your machine. If having multiple versions currently, all submodules of python should point to v3.0+.

## Setup

At first, clone/download this repository to your local machine.

### Windows
 1. Add the directory location of the cloned/downloaded version of this repository to user/system *PATH*.
 2. Add *.PY* to *PATHEXT*

### Linux (Un-tested)
1. Add the directory location of the cloned/downloaded version of this repository to *.bashrc* / *.bash_profile*

## Integration with git
On adding git-custom file path of this project to system *PATH*, this extra feature tool can be used as a part of git CLI, where 'git custom' = 'gite' is as mentioned below.

## Usage

### Windows
From any location, open **cmd** and hit 
 - ***gite -h*** to see available commands with their feature set and feature descriptions.
 - ***gite \<command> -h*** to see arguments available against the specified command.
 - ***gite \<command> [args]*** to execute the command successfully.
 - ***git custom \<command> [args]*** to execute the command successfully.

### Linux (Un-tested)
From any location, open **teminal** and hit 
 - ***./gite.py -h*** to see available commands with their feature set and feature descriptions.
 - ***./gite.py \<command> -h*** to see arguments available against the specified command.
 - ***./gite.py \<command> [args]*** to execute the command successfully.
 - ***git custom \<command> [args]*** to execute the command successfully.

## Features
Following are the features currently available in the tool

### cdump
We may require to have a backup of modifed/uncommitted files during your development to swap your current task or due to some other reason. This command will copy all those files and will dump to your specified location maintaining the relative folder structure of each file.

*usage: gite cdump -c \<commit-hash> [-p \<dump-location>]*

### udump
We may require to have a backup of committed files of a specific *commit hash* during your development. This command will copy all those files of the specified commit state of the repository and will dump to your specified location.

*usage: gite udump [-p \<dump-location>] [-s]*

### fhdump
We may require to have a backup of entire history of a particular file. This command will copy all those versions of the specified file of the repository and will dump to your specified location.

*usage: gite fhdump -f \<file-path> [-p \<dump-location>]*


### hddump
We may require to have consecutive file change/diff dump of a particular file. This command will fetch all the consecutive change history/diff of the specified file of the repository and will dump to your specified location.

*usage: gite hddump -f \<file-path> [-p \<dump-location>]*

### comment
We may require to have comments of commits to be logged in its respective JIRA issue, after they have been pushed to remote. This command serves this feature which needs jira credentials in the file 'gite.properties' and comment must be in this syntax: *ABC-1 : Sample comment*

*usage: gite comment -c \<commit-ids-comma-separated>*

### pushc
We may require to have comments of commits to be logged in its respective JIRA issue, while pushing them to remote. This command serves this feature which needs jira credentials in the file 'gite.properties' and comment must be in this syntax: *ABC-1 : Sample comment*

*usage: gite pushc [-f]*

