import os
from configparser import SafeConfigParser, Error
from gitlab import Gitlab

HOME_DIR = os.path.expanduser("~")
FILE_PATHS = ["gitlabcli.conf",
              os.path.join(HOME_DIR, "gitlabcli.conf")]


class ConfigError(Exception):
    pass


class ConfigFileNotFoundError(ConfigError):
    pass


class ConfigDataError(ConfigError):
    pass


class ConfigParser():

    def __init__(self, args):
        self.config_path = None
        if args.config_file and os.path.isfile(args.config_file):
            self.config_path = args.config_file
        else:
            for path in FILE_PATHS:
                if os.path.isfile(path):
                    self.config_path = path
                    break

        if self.config_path is None:
            raise ConfigFileNotFoundError("Cannot find configuration file")
        try:
            self._config = SafeConfigParser()
            self._config.read(self.config_path)
        except Error:
            raise ConfigDataError("Cannot read configuration file")

        if args.server is None:
            try:
                self.server = self._config.get("global", "default")
            except Exception:
                raise ConfigDataError("Cannot get server from config file")
        else:
            if not self._config.has_section(args.server) and \
                    args.server != "default":
                raise ConfigDataError("Configuration file does not have"
                                      f" section {args.server}")

        try:
            self.url = self._config.get(self.server, "url")
        except Exception:
            raise ConfigDataError(f"Cannot get url from section {self.server}")

        self.timeout = 60
        try:
            self.timeout = self._config.getint("global", "timeout")
        except Exception:
            pass
        try:
            self.timeout = self._config.getint(self.server, "timeout")
        except Exception:
            pass

        self.private_token = None
        try:
            self.private_token = self._config.get(self.server, "private_token")
        except Exception:
            pass

        self.oauth_token = None
        try:
            self.oauth_token = self._config.get(self.server, "oauth_token")
        except Exception:
            pass

        self.per_page = 10
        try:
            self.per_page = self._config.getint("global", "per_page")
        except Exception:
            pass

        try:
            self.per_page = self._config.getint(self.server, "per_page")
        except Exception:
            pass

        if self.per_page is None or self.per_page > 50 or self.per_page < 1:
            raise ConfigDataError("Invalid per_page")

    def auth(self):
        self.conn = Gitlab(self.url, private_token=self.private_token,
                           oauth_token=self.oauth_token,
                           timeout=self.timeout, per_page=self.per_page)
        self.conn.auth()
