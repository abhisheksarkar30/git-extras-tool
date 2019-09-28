from abc import ABC, abstractmethod
import argparse


"""
    This is the command based parent abstract class of gite CLI tool.
    Every command execution class should be named as Command, extend AbstractCommand and at-least
    should override each and every methods as below:
        1. get_command_code
        2. get_command_desc
        3. add_options
        4. main
"""


class AbstractCommand(ABC):

    """
        This API is to define the command which will trigger the current command implementation.
    """

    @abstractmethod
    def get_command_code(self):
        pass

    """
        This API describes the feature provided by the current command implementation. 
    """

    @abstractmethod
    def get_command_desc(self):
        pass

    """
        This API adds options to the command.
    """

    @abstractmethod
    def add_options(self, parser):
        pass

    """
        This API performs the business logic process.
    """

    @abstractmethod
    def main(self, args):
        pass

    """
        This API parses the argument and invokes main of the current command implementation.
    """

    def execute(self):
        parser = argparse.ArgumentParser("gite " + self.get_command_code())
        self.add_options(parser)
        self.main(parser.parse_args())
