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
    return subprocess.getoutput(command)


def divide_chunks(source_list, chunk_size):
    # looping till end of list
    for index in range(0, len(source_list), chunk_size):
        yield source_list[index:index + chunk_size]
