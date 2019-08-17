import Utils
from AbstractModule import AbstractCommand


"""
    This API copies only modified(M) or newly added(?) files only.
    
"""


def copy_applicable_files(target_files, destination_dir):
    for file in target_files:
        # Copying  only added or modified files
        if file[1] in ('?', 'M'):
            file_start = file.find('-> ')
            file_start = 0 if file_start == -1 else file_start
            file_name = file[file_start + 3:].strip('"')
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
    destination_dir = '/UncommittedFiles'

    def get_command_code(self):
        return "udump"

    def get_command_desc(self):
        return "Uncommitted File Dump"

    def add_options(self, parser):
        # Add applicable arguments and parse
        parser.add_argument("-p", help="Dump directory location")

    # Entry to command execution
    def main(self, args):
        if args.p is not None:
            # If destination dir explicitly specified
            self.destination_dir = args.p
        # Create destination dir if doesn't exist
        Utils.create_dir(self.destination_dir)
        # Fetch file-names to copy
        target_files = Utils.execute_command("git status -s").split("\n")
        # Copy all applicable files
        copy_applicable_files(target_files, self.destination_dir)
