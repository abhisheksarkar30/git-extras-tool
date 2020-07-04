import Utils
from AbstractModule import AbstractCommand


"""
    This API copies only modified(M) or newly added(?) files only.
    
"""


def copy_applicable_files(target_files, destination_dir, structure):
    # Get repository base directory path
    base_dir = Utils.execute_command("git rev-parse --show-toplevel")
    for file in target_files:
        # Copying  only added or modified files
        if file[1] in ('?', 'M'):
            file_start = file.find('-> ')
            file_start = 0 if file_start == -1 else file_start
            file_name = file[file_start + 3:].strip('"')
            print(file_name)
            if structure is False:
                if destination_dir[len(destination_dir)-1] in ('\\', '/'):
                    destination_dir = destination_dir[: len(destination_dir)-1]
                # Create destination folder structure for each file to dump
                local_destination_dir = destination_dir + "/" + file_name[: file_name.rfind("/")]
                # Create destination dir if doesn't exist
                Utils.create_dir(local_destination_dir)
            else:
                local_destination_dir = destination_dir
            file_name = base_dir + "/" + file_name
            Utils.copy(file_name, local_destination_dir)


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
        parser.add_argument("-s", help="File hierarchy structure not required", action='store_true')

    # Entry to command execution
    def main(self, args):
        if args.p is not None:
            # If destination dir explicitly specified
            self.destination_dir = args.p
        # Create destination dir if doesn't exist
        Utils.create_dir(self.destination_dir)
        Utils.execute_command("git config status.relativePaths false")
        Utils.execute_command("git status -s > " + self.destination_dir + "/git-status.txt")
        # Fetch file-names to copy
        target_files = Utils.execute_command("git status -s").split("\n")
        Utils.execute_command("git config status.relativePaths true")
        # Copy all applicable files
        copy_applicable_files(target_files, self.destination_dir, args.s)
