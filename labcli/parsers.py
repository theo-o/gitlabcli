from labcli.utils import print_stuff


class BaseSubParser:
    def __init__(self, main_parser):
        self.main_parser = main_parser
        self.set_vars()
        self.parser = self.main_parser.add_parser(self.name, help=self.help_text)
        self.add_global_args()
        self.add_args()

    def set_vars(self):
        self.name = None
        self.help_text = None

    def add_global_args(self):
        self.parser.add_argument(
            "-c",
            "--config-file",
            help="A configuration file to read",
            metavar="<file>",
            required=False,
        )
        self.parser.add_argument(
            "-s",
            "--server",
            help="Server to authenticate to",
            metavar="<server>",
            required=False,
        )

    def add_args(self):
        self.subparsers = self.parser.add_subparsers(help="Subcommand", dest="subcmd")
        for arg in self.args:
            self.subparsers.add_parser(arg["name"], help=arg["help"])


class ProjectParser(BaseSubParser):
    def set_vars(self):
        self.name = "project"
        self.help_text = "Project"
        self.args = [{"name": "list-owned", "help": "List all projects owned by user"}]


class ProjectManager(object):
    def __init__(self):
        pass

    def list_owned(self, args, config):
        projects = config.conn.projects.list(owned=True)
        print_stuff(projects, "json", None)


class AccountParser(BaseSubParser):
    def set_vars(self):
        self.name = "account"
        self.help_text = "Account"
        self.args = [
            {"name": "list-info", "help": "List account info"},
            {"name": "list-gpg", "help": "List GPG keys"},
            {"name": "list-ssh", "help": "List SSH keys"},
        ]


class AccountManager(object):
    def __init__(self):
        pass

    def list_info(self, args, config):
        info = config.conn.user
        print_stuff(info, "json", None)

    def list_gpg(self, args, config):
        keys = config.conn.user.gpgkeys.list()
        print_stuff(keys, "json", None)

    def list_ssh(self, args, config):
        keys = config.conn.user.keys.list()
        print_stuff(keys, "json", None)
