import argparse
import subprocess
import Utils

def copy_files(target_files, destination_dir):
    for file in target_files:
        # Copying  only added or modified files
        if file[1] in ('?', 'M'):
            fileName = file[3:]
            print(fileName)
            Utils.copy(fileName, destination_dir)

# Command based subclass of gite cli tool
class Command:
    destination_dir = '/UncommittedFiles'
    parser = argparse.ArgumentParser("gite udump")

    def __init__(self):
        # Add applicable arguments and parse
        self.parser.add_argument("-p", help="Dump directory location")
        self.args = self.parser.parse_args()
        if self.args.p is not None:
            # If destination dir explicitly specified
            self.destination_dir = self.args.p

    # Entry to command execution
    def main(self):
        # Create destination dir if doesn't exist
        Utils.create_dir(self.destination_dir)
        # Fetch file-names to copy
        targetFiles = subprocess.getoutput("git status -s").split("\n")
        # Copy all applicable files
        copy_files(targetFiles, self.destination_dir)

# Calls the main method to execute the command
if __name__ != "__main__":
    Command().main()
