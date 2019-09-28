"""
    This module serves to be the parent level command line interpreter for the Git Extra tool(gite).
    Each command of this tool need to be served by classes in separate specific modules.

        Usage :  gite [-h] command [<args>]

    Any part of this module must not be modified for any new command inclusion to the tool, unless
    facing some exceptional case to change the framework, as it is plug-able in nature.

    Reference of including a new command maybe taken from UncommittedFileDump.py module.
"""

import sys
import Utils

"""
    This class provides the following:-
        1. Overall description for each command
        2. Links respective module for the specified command and execute them as per the provided
            arguments. Validation and execution of arguments of a specific command depends on the
            related module. 
"""


class Gite:
    usage = "usage: gite [-h] command [<args>]"
    naError = usage + "\n gite: error: the following arguments are required: command"
    uError = naError + "\n gite: error: unrecognized arguments: "
    helpDetail = usage
    switcher = {}

    """
        This API forms the help detail of the tool having overall description of each command and
        creates a map of available commands vs its respective module.
    """
    def populate_help_n_switcher(self):
        # Loads command specific module list
        module_list = Utils.load_all_modules_from_dir("commands")
        template = "   {:10s}\t  {:s}"
        for module in module_list:
            command_class = module.Command()
            self.helpDetail += "\n" + template.format(command_class.get_command_code(), command_class.get_command_desc())
            self.switcher.update({command_class.get_command_code(): command_class})

    """
        This is entry point of the tool which flows the control to the related module as per the
        command specified.
    """
    def main(self):
        self.populate_help_n_switcher()
        if len(sys.argv) == 1:
            # No command specified
            print(self.naError)
        elif sys.argv[1] == "-h":
            # Provides cli usage help details
            print(self.helpDetail)
        else:
            # Finds applicable python file for the specified script
            choice = sys.argv[1]
            target_class = self.switcher.get(choice)
            if target_class is None:
                # Command not found
                print(self.uError + choice)
            else:
                # Modifying arguments to pass to command specific submodule
                sys.argv.remove(sys.argv[1])
                # Calling main function of the Command class in the submodule
                target_class.execute()


# Calls the main method to execute the cli tool
if __name__ == "__main__":
    Gite().main()
