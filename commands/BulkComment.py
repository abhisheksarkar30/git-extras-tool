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
        return "comment"

    def get_command_desc(self):
        return "Bulk jira comment"

    def add_options(self, parser):
        # Add applicable arguments and parse
        parser.add_argument("-c", help="Commit IDs comma separated", required=True)
        return

    # Entry to command execution
    def main(self, args):
        commit_list = args.c.split(",")
        keys = load_props()
        jira_base = keys['jira.url']
        jira_cred = keys['jira.user'] + ":" + keys['jira.pass']
        base_comment = "==============Automated Comment==============\n"
        base_comment += "Repository : " + Utils.execute_command("git config --get remote.origin.url") + "\n"
        base_comment += "Branch : " + Utils.execute_command("git branch --show-current") + "\n"
        for commit in commit_list:
            commit_id = commit.strip()
            print("\nCommit ID : " + commit_id)
            commit_msg = Utils.execute_command("git show-branch --no-name " + commit_id)
            if commit_msg.find("fatal") != -1:
                print(commit_msg)
                continue
            if commit_msg.find(":") == -1:
                print("No jira issue id mentioned")
                continue

            jira_id = commit_msg[: commit_msg.find(":")].strip()
            if jira_id.find("-") == -1:
                print("No jira issue id mentioned")
                continue
            jira_url = jira_base + "rest/api/2/issue/" + jira_id + "/comment"
            file_list = list(Utils.execute_command("git diff-tree --no-commit-id --name-status -r "
                                                   + commit_id).split("\n"))
            chunk_list = list(Utils.divide_chunks(file_list, 50))

            for chunk in chunk_list:
                comment = base_comment + "Commit Details :\n" + commit_id + " " + commit_msg + "\n"
                comment = (comment + "Related files :\n" + "\n".join(chunk)).replace('\n', '\\n').replace('\t', '\\t')
                comment = comment.replace("&", "and")
                # Form the jira comment message
                jira_command = "curl -u " + jira_cred + " -X POST --data \"{\\\"body\\\": \\\"" + comment + \
                               "\\\"}\" -H \"Content-Type: application/json\" " + jira_url
                # print(jira_command)
                # Fire REST call for submitting the comment
                print(Utils.execute_command(jira_command))
