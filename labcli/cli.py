# -*- coding: utf-8 -*-

import sys
import argparse

import labcli
from labcli.auth import ConfigParser
from labcli.parsers import ProjectParser, ProjectManager, AccountParser, AccountManager


class LabCLI:

    CLI_HELP = """usage: cli [-h] command

A CLI application for the GitLab API

Commands:
    project
    account

Optional Arguments:
  -h, --help  show this help message and exit"""

    def __init__(self):
        if "--version" in sys.argv:
            self.version()
            exit(0)

        parser = argparse.ArgumentParser(description=labcli.__description__)

        subparsers = parser.add_subparsers(help="A command", dest="cmd")

        ProjectParser(subparsers)
        AccountParser(subparsers)

        args = parser.parse_args()

        if args.cmd is None or not hasattr(self, args.cmd):
            print(f"Invalid command: {args.cmd}")
            parser.print_help()
            exit(1)
        config = ConfigParser(args)
        config.auth()

        if args.cmd not in ["add_global_args", "read_config"]:
            getattr(self, args.cmd)(args, config)
        else:
            print(f"Invalid command: {args.cmd}")
            parser.print_help()
            exit(1)

    def add_global_args(self, aparser):
        aparser.add_argument(
            "-c",
            "--config-file",
            help="A configuration file to read",
            metavar="<file>",
            required=False,
        )
        aparser.add_argument(
            "-s",
            "--server",
            help="Server to authenticate to",
            metavar="<server>",
            required=False,
        )

    def version(self):
        vers = "GitLab CLI version {}".format(labcli.__version__)
        print(vers)

    def project(self, args, config):
        if args.subcmd and hasattr(ProjectManager, args.subcmd.replace("-", "_")):
            func = getattr(ProjectManager(), args.subcmd.replace("-", "_"))
            func(args, config)
        else:
            print(f"Invalid subcommand: {args.subcmd}")
            print(self.CLI_HELP)
            exit(1)

    def account(self, args, config):
        if args.subcmd and hasattr(AccountManager, args.subcmd.replace("-", "_")):
            func = getattr(AccountManager(), args.subcmd.replace("-", "_"))
            func(args, config)
        else:
            print(f"Invalid subcommand: {args.subcmd}")
            print(self.CLI_HELP)
            exit(1)


def main():
    LabCLI()
