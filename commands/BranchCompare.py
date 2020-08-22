"""
This Command class finds the missing commit hash in one main branch but present in its feature branch.
Can be used between two provided branches, or with all branches related to the provided one branch.
"""

import Utils
from AbstractModule import AbstractCommand


def find_remote_branches():
    # List all remote branches
    output = Utils.execute_command(["git", "branch", "--list", "-r"])
    branches = output.decode().strip().split('\n')
    branches = list(map(lambda y: y.strip(), branches))
    return branches


def commit_diffs(parent_branch: str, target_branch: str):
    # To find the missing commit hashes between 2 branches
    output = Utils.execute_command(["git", "rev-list", "--max-count", "50", parent_branch + ".." + target_branch])
    lines = output.decode().strip().split('\n')
    lines = list(filter(lambda x: len(x) > 0, lines))
    return lines


def is_merge_hash(commit_id: str):
    # To get the relationship tree for the given hash
    parent_issue = Utils.execute_command(["git", "cat-file", "-p", commit_id])
    # Commit hash: 1 parent, Merge hash: multiple parent
    count = parent_issue.decode().count("parent")
    return count > 1


def is_valid_branch(branch_name: str, remote_branches):
    # Checking existence/validity of the provided branch
    branch_list = list(filter(lambda x: x == branch_name, remote_branches))
    return len(branch_list) == 1


"""
    Filters any branch which begins with the same name as provided
    Will work iff we follow: Feature Branch Name = PARENT_BRANCH_NAME+SOMETHING,
    e.g. PARENT-BRANCH = ABC_MAIN, FEATURE-BRANCH = ABC_MAIN_ISSUE_007
"""


def find_related_branches(branch_name, remote_branches):
    # Filtering out related branches only
    related_branch = list(filter(lambda x: (x.upper()).startswith(branch_name.upper()), remote_branches))
    related_branch.remove(branch_name)
    return related_branch


def print_diff(target_branch, parent_branch):
    # Identifying commit diffs and not merged commits
    commit_list = commit_diffs(parent_branch, target_branch)
    print("Commit Present in", target_branch, "and missing in ", parent_branch)
    for commit in commit_list:
        if not is_merge_hash(commit):
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
        remote_branches = find_remote_branches()
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
        if not is_valid_branch(self.parent_branch, self.remote_branches):
            print("Invalid Branch Name")
            exit(1)

        related_branches = find_related_branches(self.parent_branch, self.remote_branches)

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
        if not is_valid_branch(self.parent_branch, self.remote_branches):
            print("Invalid Branch Name provided :", self.parent_branch)
            exit(1)

        if not is_valid_branch(self.child_branch, self.remote_branches):
            print("Invalid Branch Name provided :", self.child_branch)
            exit(1)

        print_diff(self.parent_branch, self.child_branch)
