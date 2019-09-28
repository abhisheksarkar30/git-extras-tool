# Gite

Hi, git users!
As we know **git** is already a powerful tool for version controlling. Yet, while we do our regular git activities, we feel sometimes that some features are ***good to have***  for many, if not for all, for convenience of work. **gite** brings you those features.



## Setup

At first, clone/download this repository to your local machine.

### Windows
 1. Add the directory location of the cloned/downloaded version of this repository to user/system *PATH*.
 2. Add *.PY* to *PATHEXT*

### Linux (Un-tested)
1. Add the directory location of the cloned/downloaded version of this repository to *.bashrc* / *.bash_profile*

## Usage

### Windows
From any location, open **cmd** and hit 
 - ***gite -h*** to see available commands with their feature set and feature descriptions.
 - ***gite \<command> -h*** to see arguments available against the specified command.
 - ***gite \<command> [args]*** to execute the command successfully.

### Linux (Un-tested)
From any location, open **teminal** and hit 
 - ***./gite.py -h*** to see available commands with their feature set and feature descriptions.
 - ***./gite.py \<command> -h*** to see arguments available against the specified command.
 - ***./gite.py \<command> [args]*** to execute the command successfully.

## Features
Following are the features currently available in the tool

### cdump
We may require to have a backup of modifed/uncommitted files during your development to swap your current task or due to some other reason. This command will copy all those files and will dump to your specified location.
*usage: gite cdump -c \<commit hash> [-p \<path>]*

### udump
We may require to have a backup of committed files of a specific *commit hash* during your development. This command will copy all those files of the specified commit state of the repository and will dump to your specified location.
*usage: gite udump [-p \<path>]*
