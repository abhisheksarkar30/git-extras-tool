import argparse
import os
import shutil
import subprocess
import distutils
from distutils import dir_util

def copy(src, dest):
    try:
        dir_util.copy_tree(src, dest)
    except distutils.errors.DistutilsFileError as e:
        # If the error was caused because the source wasn't a directory
        shutil.copy(src, dest)

parser = argparse.ArgumentParser("gite udump")
# parser.add_argument("command", help="Category", choices=["udump"])
# parser.add_argument("-u", "--uncommitted", help="Uncommitted File Dump", required=True, action='store_true')
parser.add_argument("-p", help="Dump directory location")
args = parser.parse_args()
destDir = '/UncommittedFiles'
if args.p is not None:
    destDir = args.p
if not os.path.exists(destDir):
    os.makedirs(destDir)
targetFiles = subprocess.getoutput("git status -s").split("\n")
for file in targetFiles:
    fileName = file[3:]
    print(fileName)
    copy(fileName, destDir)
