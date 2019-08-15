import sys
import Utils

# Main class for gite commands
class Gite:
    usage = "usage: gite [-h] command [<args>]"
    naError = usage + "\n" + "gite: error: the following arguments are required: command"
    uError = naError + "\n" + "gite: error: unrecognized arguments: "
    helpDetail = usage
    switcher = {}

    # Populates cli usage help and command vs module  map
    def populate_help_N_switcher(self):
        # Loads configuration of gite commands
        config_list = Utils.file_reader("config.properties")
        template = "   {:10s}\t  {:s}"
        for line in config_list:
            line_args = line.strip().split("|")
            self.helpDetail += "\n" + template.format(line_args[0], line_args[1])
            self.switcher.update({line_args[0]: line_args[2]})

    # Main
    def main(self):
        self.populate_help_N_switcher()
        if len(sys.argv) == 1:
            # No command specified
            print(self.naError)
        elif sys.argv[1] == "-h":
            # Provides cli usage help details
            print(self.helpDetail)
        else:
            # Finds applicable python file for the specified script
            choice = sys.argv[1]
            target_module = self.switcher.get(choice)
            if target_module is None:
                # Command not found
                print(self.uError + choice)
            else:
                # Calls the command based class in a subprocess
                sys.argv.remove(sys.argv[1])
                Utils.fetch_module(target_module)

# Calls the main method to execute the cli tool
if __name__ == "__main__":
    Gite().main()
