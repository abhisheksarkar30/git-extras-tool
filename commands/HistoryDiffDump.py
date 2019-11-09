import sys
from builtins import print

import Utils
from AbstractModule import AbstractCommand

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
    destination_dir = '/HistoryDiff'

    def get_command_code(self):
        return "hddump"

    def get_command_desc(self):
        return "History version wise diff Dump"

    def add_options(self, parser):
        # Add applicable arguments and parse
        parser.add_argument("-p", help="Dump directory location")
        parser.add_argument("-f", help="File path", required=True)

    # Entry to command execution
    def main(self, args):
        target_file_path = Utils.execute_command("git ls-files --full-name " + args.f)
        target_filename = target_file_path[target_file_path.rfind("/") + 1:]
        if target_file_path.__contains__("fatal"):
            print(target_file_path)
            sys.exit(-1)
        if args.p is not None:
            # If destination dir explicitly specified
            self.destination_dir = args.p
        # Create destination dir if doesn't exist
        Utils.create_dir(self.destination_dir)
        # Fetch history info
        info_list = Utils.execute_command("git log --pretty=format:\"%h %an\" " + args.f).split("\n")
        count = info_list.__len__()
        for index, obj in enumerate(info_list[:info_list.__len__() - 1]):
            print(obj)
            #  Retrieving each version content
            new_commit_id = obj[0:obj.find(" ")]
            old_obj = info_list[index + 1]
            old_commit_id = old_obj[0:old_obj.find(" ")]
            destination_file_path = self.destination_dir + "/" + target_filename + "_" + old_commit_id + "_" + \
                str(count - 1) + "-" + new_commit_id + "_" + str(count) + ".txt"
            count -= 1
            # print("git diff " + old_commit_id + " " + new_commit_id + " -- \"" + args.f + "\" > \"" +
            #       destination_file_path + "\"")
            print(Utils.execute_command("git diff " + old_commit_id + " " + new_commit_id + " -- \"" + args.f
                                        + "\" > \"" + destination_file_path + "\""))
