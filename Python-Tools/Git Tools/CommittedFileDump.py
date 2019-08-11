import argparse
import distutils
import os
import shutil
import subprocess
import sys
from distutils import dir_util


def copy(src, dest):
    try:
        dir_util.copy_tree(src, dest)
    except distutils.errors.DistutilsFileError as e:
        # If the error was caused because the source wasn't a directory
        shutil.copy(src, dest)


parser = argparse.ArgumentParser("gite cdump")
# parser.add_argument("command", help="Category", choices=["udump"])
# parser.add_argument("-u", "--uncommitted", help="Uncommitted File Dump", required=True, action='store_true')
parser.add_argument("-p", help="Dump directory location")
parser.add_argument("-c", help="Commit hash", required=True)
args = parser.parse_args()
destDir = '/CommittedFiles'
if args.p is not None:
    destDir = args.p
if not os.path.exists(destDir):
    os.makedirs(destDir)
commitCheck = subprocess.getoutput("git cat-file -t " + args.c)
if commitCheck != "commit":
    print(commitCheck)
    sys.exit()
targetFiles = subprocess.getoutput("git diff-tree --no-commit-id --name-status -r " + args.c).split("\n")
print(subprocess.getoutput("git checkout " + args.c))
for file in targetFiles:
    if file[0] in ('M', 'A'):
        fileName = file[file.find("\t")+1:]
        print(fileName)
        copy(fileName, destDir)
print(subprocess.getoutput("git checkout -"))
