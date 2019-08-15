import argparse
import subprocess
import sys
import Utils

def copy_files(target_files, destination_dir):
    # Get repository base directory path
    base_dir = subprocess.getoutput("git rev-parse --show-toplevel")
    # Copying all files applicable
    for file in target_files:
        # Copying  only added or modified files
        if file[0] in ('M', 'A'):
            fileName = base_dir + "/" + file[file.find("\t") + 1:]
            print(fileName)
            Utils.copy(fileName, destination_dir)

# Command based subclass of gite cli tool
class Command:
    destination_dir = '/CommittedFiles'
    parser = argparse.ArgumentParser("gite cdump")

    def __init__(self):
        # Add applicable arguments and parse
        self.parser.add_argument("-p", help="Dump directory location")
        self.parser.add_argument("-c", help="Commit hash", required=True)
        self.args = self.parser.parse_args()
        if self.args.p is not None:
            # If destination dir explicitly specified
            self.destination_dir = self.args.p

    # Entry to command execution
    def main(self):
        # Create destination dir if doesn't exist
        Utils.create_dir(self.destination_dir)
        # Verifying specified commit id
        Utils.verify_commit(self.args.c)
        # Fetch file-names to copy
        targetFiles = subprocess.getoutput("git diff-tree --no-commit-id --name-status -r " + self.args.c).split("\n")
        # Checking out by commit id
        status = subprocess.getoutput("git checkout " + self.args.c)
        print(status)
        if status.__contains__("Aborting"):
            sys.exit(-1)
        # Copy all applicable files
        copy_files(targetFiles, self.destination_dir)
        # Checking out to the previous branch
        print(subprocess.getoutput("git checkout -"))

# Calls the main method to execute the command
if __name__ != "__main__":
    Command().main()
