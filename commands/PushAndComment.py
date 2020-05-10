import Utils
import configparser
import sys
from AbstractModule import AbstractCommand

"""
    This is the command based subclass of gite CLI tool.
    Every command execution class should be named as Command, extend AbstractCommand and at-least
    should override each and every methods as below:
        1. get_command_code
        2. get_command_desc
        3. add_options
        4. main
"""


def load_props():
    config = configparser.RawConfigParser()
    config.read(sys.path[0] + '/gite.properties')
    return dict(config.items('JIRA'))


class Command(AbstractCommand):

    def get_command_code(self):
        return "pushc"

    def get_command_desc(self):
        return "Push and comment"

    def add_options(self, parser):
        # Add applicable arguments and parse
        parser.add_argument("-f", help="Forced push", action='store_true')
        return

    # Entry to command execution
    def main(self, args):
        commit_list = Utils.execute_command("git cherry -v").split("\n")
        keys = load_props()
        jira_base = keys['jira.url']
        jira_cred = keys['jira.user'] + ":" + keys['jira.pass']
        base_comment = "==============Automated Comment==============\n"
        base_comment += "Repository : " + Utils.execute_command("git config --get remote.origin.url") + "\n"
        base_comment += "Branch : " + Utils.execute_command("git branch --show-current") + "\n"
        result = Utils.execute_command("git push" if len(sys.argv) == 1 else "git push -f")
        print(result)
        # Checking for successful push to remote
        if result.find("rejected") != -1 or result.find("exit code 1") != -1:
            print("Push failed")
            return
        for commit in commit_list:
            print("\n" + commit)
            comment = base_comment + "Commit Details :\n" + commit + "\n" + "Related files :\n"
            first_space_index = commit.find(" ")
            second_space_index = commit.find(" ", first_space_index + 1)
            commit_id = commit[first_space_index + 1: second_space_index]
            commit_msg = commit[second_space_index + 1:].strip()
            if commit_msg.find(":") == -1:
                print("No jira issue id mentioned")
                continue
            jira_id = commit_msg[: commit_msg.find(":")].strip()
            if jira_id.find("-") == -1:
                print("No jira issue id mentioned")
                continue
            jira_url = jira_base + "rest/api/2/issue/" + jira_id + "/comment"
            comment = (comment + Utils.execute_command("git diff-tree --no-commit-id --name-status -r " +
                        commit_id)).replace('\n', '\\n').replace('\t', '\\t')
            # Form the jira comment message
            jira_command = "curl -u " + jira_cred + " -X POST --data \"{\\\"body\\\": \\\"" + comment + \
                           "\\\"}\" -H \"Content-Type: application/json\" " + jira_url
            # print(jira_command)
            # Fire REST call for submitting the comment
            print(Utils.execute_command(jira_command))
