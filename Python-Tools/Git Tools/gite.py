import sys
import subprocess

def show_usage():
    template = "   {:10s}\t   {:s}"
    details = usage
    details += "\n" + template.format("udump", "Uncommitted File Dump")
    details += "\n" + template.format("cdump", "Existing commit wise File Dump")
    return details

def throw_req_error():
    return usage + "\n" + naError

def throw_unknown_error(arg):
    return throw_req_error() + "\n" + uError + arg

def class_invoker(clazz):
    return subprocess.getoutput(clazz + " " + " ".join(args[2:]))

usage = "usage: gite [-h] command [<args>]"
naError = "gite: error: the following arguments are required: command"
uError = "gite: error: unrecognized arguments: "
switcher = {
    "-h": show_usage,
    "udump": lambda: class_invoker("UncommittedFileDump.py"),
    "cdump": lambda: class_invoker("CommittedFileDump.py")
}
args = sys.argv
if len(args) == 1:
    print(throw_req_error())
else:
    choice = args[1]
    func = switcher.get(choice, lambda: throw_unknown_error(choice))
    print(func())
