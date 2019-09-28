import sys
import Utils
from AbstractModule import AbstractCommand


"""
    This API finds the base repository directory to form the file absolute path.
    It copies only modified(M) or newly added(A) files only.
"""


def copy_applicable_files(target_files, destination_dir):
    # Get repository base directory path
    base_dir = Utils.execute_command("git rev-parse --show-toplevel")
    # Copying all files applicable
    for file in target_files:
        # Copying only added or modified files
        if file[0] in ('M', 'A'):
            file_name = base_dir + "/" + file[file.find("\t") + 1:]
            print(file_name)
            Utils.copy(file_name, destination_dir)


"""
    This is the command based subclass of gite CLI tool.
    Every command execution class should be named as Command, extend AbstractCommand and at-least
    should override each and every methods as below:
        1. get_command_code
        2. get_command_desc
        3. add_options
        4. main
"""


class Command(AbstractCommand):
    destination_dir = '/CommittedFiles'

    def get_command_code(self):
        return "cdump"

    def get_command_desc(self):
        return "Existing commit wise File Dump"

    def add_options(self, parser):
        # Add applicable arguments and parse
        parser.add_argument("-p", help="Dump directory location")
        parser.add_argument("-c", help="Commit hash", required=True)

    # Entry to command execution
    def main(self, args):
        if args.p is not None:
            # If destination dir explicitly specified
            self.destination_dir = args.p
        # Create destination dir if doesn't exist
        Utils.create_dir(self.destination_dir)
        # Verifying specified commit id
        Utils.verify_commit(args.c)
        # Fetch file-names to copy
        target_files = Utils.execute_command("git diff-tree --no-commit-id --name-status -r " + args.c).split("\n")
        # Checking out by commit id
        status = Utils.execute_command("git checkout " + args.c)
        print(status)
        if status.__contains__("Aborting"):
            sys.exit(-1)
        # Copy all applicable files
        copy_applicable_files(target_files, self.destination_dir)
        # Checking out to the previous branch
        print(Utils.execute_command("git checkout -"))
