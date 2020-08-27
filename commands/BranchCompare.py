"""
This Command class finds the missing commit hash in one main branch but present in its feature branch.
Can be used between two provided branches, or with all branches related to the provided one branch.
"""

import Utils
from AbstractModule import AbstractCommand


def print_diff(target_branch, parent_branch):
    # Identifying commit diffs and not merged commits
    commit_list = Utils.commit_diffs(parent_branch, target_branch, "50")
    print("Commit Present in", target_branch, "and missing in ", parent_branch)
    for commit in commit_list:
        if not Utils.is_merge_hash(commit):
            print(commit)


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

    def get_command_code(self):
        return "bcompare"

    def get_command_desc(self):
        return "Compare branches for commit diffs"

    def add_options(self, parser):
        # Add applicable arguments and parse
        parser.add_argument("-p", help="Parent Branch", required=True)
        parser.add_argument("-t", help="Target Branch (N/A, iff to be checked for all related branches)")
        return

    # Entry to command execution
    def main(self, args):
        # Initialization
        Utils.execute_command(["git", "pull"])
        # To remove deleted branches from remote.
        Utils.execute_command(["git", "remote", "prune", "origin"])
        # Fetching master list of remote branches
        remote_branches = Utils.find_remote_branches()
        if args.t is None:
            SingleBranchComparator(args.p, remote_branches).execute()
        else:
            DoubleBranchComparator(args.p, args.t, remote_branches).execute()
        pass


"""
    This API finds diff between all related branches to the one and only provided branch. 
"""


class SingleBranchComparator:
    parent_branch = None
    remote_branches = None

    def __init__(self, branch_name, remote_branches):
        self.parent_branch = "origin/" + branch_name
        self.remote_branches = remote_branches

    def execute(self):
        if not Utils.is_valid_branch(self.parent_branch, self.remote_branches):
            print("Invalid Branch Name")
            exit(1)

        related_branches = Utils.find_related_branches(self.parent_branch, self.remote_branches)

        for branch in related_branches:
            print_diff(branch, self.parent_branch)
            print()


"""
    This API finds diff between the 2 branch names provided, if only.
"""


class DoubleBranchComparator:
    parent_branch = None
    child_branch = None
    remote_branches = None

    def __init__(self, parent_branch, child_branch, remote_branches):
        self.parent_branch = "origin/" + parent_branch
        self.child_branch = "origin/" + child_branch
        self.remote_branches = remote_branches

    def execute(self):
        if not Utils.is_valid_branch(self.parent_branch, self.remote_branches):
            print("Invalid Branch Name provided :", self.parent_branch)
            exit(1)

        if not Utils.is_valid_branch(self.child_branch, self.remote_branches):
            print("Invalid Branch Name provided :", self.child_branch)
            exit(1)

        print_diff(self.parent_branch, self.child_branch)
