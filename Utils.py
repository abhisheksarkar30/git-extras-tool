import importlib
import pkgutil
import os
import shutil
import subprocess
import sys
from distutils import dir_util


# Copy each file or all files recursively from a folder
def copy(src, destination_dir):
    try:
        if os.path.isfile(src):
            shutil.copy(src, destination_dir)
        else:
            dir_util.copy_tree(src, destination_dir)
    except Exception as e:
        print("Unable to copy: " + str(e))


# Create dir if doesn't exist
def create_dir(destination_dir):
    if not os.path.exists(destination_dir):
        try:
            os.makedirs(destination_dir)
        except Exception as e:
            print("Unable to create target dir: " + str(e))
            sys.exit(-1)


# Verify specified commit id
def verify_commit(commit_id):
    commit_check = subprocess.getoutput("git cat-file -t " + commit_id)
    if commit_check != "commit":
        print(commit_check)
        sys.exit(-1)


# Calls the specified python class in a subprocess
def script_invoker(script, args):
    return subprocess.getoutput(script + ".py " + " ".join(args))


# Import module dynamically
def fetch_module(module):
    return importlib.import_module(module)


# Get list of modules in a directory
def load_all_modules_from_dir(directory):
    module_list = []
    directory = sys.path[0] + "/" + directory
    for importer, package_name, _ in pkgutil.iter_modules([directory]):
        if package_name not in sys.modules:
            module_list.append(importer.find_module(package_name).load_module(package_name))
    return module_list


# Read lines from a file into a list
def file_reader(file_name):
    try:
        file = open(sys.path[0] + "/" + file_name, "r")
        lines = file.readlines()
        # Check for empty file
        if not lines:
            raise ValueError("No content found")
    except (FileNotFoundError, ValueError) as e:
        print("Unable to load file: " + str(e))
        sys.exit(-1)
    return lines


# Execute specified command in a subprocess
def execute_command(command):
    return subprocess.getoutput(command) if isinstance(command, str) else subprocess.check_output(command)


# Divides a list in chunks of specified size
def divide_chunks(source_list, chunk_size):
    # looping till end of list
    for index in range(0, len(source_list), chunk_size):
        yield source_list[index:index + chunk_size]


def find_remote_branches():
    # List all remote branches
    output = execute_command(["git", "branch", "--list", "-r"])
    branches = output.decode().strip().split('\n')
    branches = list(map(lambda y: y.strip(), branches))
    return branches


def commit_diffs(parent_branch: str, target_branch: str, max_limit: str):
    # To find the missing commit hashes between 2 branches
    output = execute_command(["git", "rev-list", "--max-count", max_limit, parent_branch + ".." + target_branch])
    lines = output.decode().strip().split('\n')
    lines = list(filter(lambda x: len(x) > 0, lines))
    return lines


def is_merge_hash(commit_id: str):
    # To get the relationship tree for the given hash
    parent_issue = execute_command(["git", "cat-file", "-p", commit_id])
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
