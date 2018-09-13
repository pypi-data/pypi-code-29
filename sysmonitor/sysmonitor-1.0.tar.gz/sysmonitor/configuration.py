"""
Configuration Module

It loads the configuration from a file and loads the default when a missing
configuration is detected
"""
import os
import argparse
import configparser
import logging
import collections
import multiprocessing


_LOGGER = logging.getLogger(__name__)


class SysMonitorAction(argparse.Action):
    """
    Custom actions for sysmonitor

    Use sysmonitor_nargs_pattern for nargs custom patterns
    """
    # pylint: disable=too-few-public-methods
    sysmonitor_nargs_pattern = None

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, values)


class HostAction(SysMonitorAction):
    """
    Custom action for add host arguments

    It disables authentication when user doesn't add a authentication token
    """
    # pylint: disable=too-few-public-methods
    sysmonitor_nargs_pattern = r"^(A{2,3})$"

    def __call__(self, parser, namespace, values, option_string=None):
        if len(values) == 2:
            values.append(False)
        setattr(namespace, self.dest, values)


class CustomArgumentParser(argparse.ArgumentParser):
    """
    Custom argument parser for sysmonitor

    It implements the SysMonitorAction sysmonitor_nargs_pattern field
    """

    def _get_nargs_pattern(self, action):
        if hasattr(action, "sysmonitor_nargs_pattern") and \
                getattr(action, "sysmonitor_nargs_pattern", None):
            return action.sysmonitor_nargs_pattern
        return super(CustomArgumentParser, self)._get_nargs_pattern(action)


class Configuration():
    """Configuration Module"""

    @staticmethod
    def _default_config():
        """Default configuration"""
        return {
            "database": {
                "url": "sqlite:///:memory:",
            },
            "logging": {
                "file": "/var/log/sysmonitor/sysmonitor.log",
                "level": logging.INFO,
                "format": "%%(levelname)s:%%(name)s: %%(message)s"
            },
            "hosts": {
                "query_threads": multiprocessing.cpu_count(),
                "query_time": 300
            }
        }

    @staticmethod
    def _parse_args(parse_cmd, config_file):
        """
        Parse command line arguments (if say so)

        :param bool parse_cmd: If True, it parses command line arguments
        :param string config_file: Configuration file. Used when parse_cmd if False
        :return: Named tuple with arguments
        :rtype: tuple
        """
        _LOGGER.debug("Loading arguments")
        if parse_cmd:
            parser = CustomArgumentParser(description="System Monitor Agent")
            parser.add_argument("-c", "--config", type=str,
                                metavar="configuration_file",
                                help="Configuraton file",
                                default="/etc/sysmonitor/sysmonitor.ini")
            parser.add_argument("--add-host", nargs=3, action=HostAction,
                                metavar=("name", "address",
                                         "[authentication_key]"),
                                help="Add a host to the database.")
            parser.add_argument("--update-host", nargs=3, action=HostAction,
                                metavar=("name", "address",
                                         "[authentication_key]"),
                                help="Update an host address and "
                                     "authentication")
            parser.add_argument("--toggle-host", metavar="name",
                                help="Active or inactive a host")
            parser.add_argument("--delete-host", metavar="name",
                                help="Delete a host")
            parser.add_argument("--without-migration", action="store_true",
                                help="Disable database upgrades")
            return parser.parse_args()
        if not config_file:
            raise AttributeError("Invalid configuration. "
                                 "You must specify the configuration file if "
                                 "not using cmd arguments")
        Config = collections.namedtuple("Configuration",
                                        ["config"])
        return Config(config=config_file)

    def _load(self):
        """
        Load configuration from file and default configurations

        :param bool dolog: It logs if True
        """
        if os.path.exists(self._config_file):
            self._config.read(self._config_file)
            for section, settings in self._default_config().items():
                if not self._config.has_section(section):
                    self._config.add_section(section)
                for setting, value in settings.items():
                    if self._config.get(section, setting, fallback=None) is None:
                        self._config.set(section, setting, str(value))
        else:
            self._config.read_dict(self._default_config())

    def __init__(self, parse_cmd=True, config_file=False):
        """
        Configuration Module.

        :param bool parse_cmd: If True, it parses command line arguments
        :param string config_file: Configuration file. Used when parse_cmd if False
        """
        args = self._parse_args(parse_cmd, config_file)
        self._config_file = args.config
        _LOGGER.debug("Configuration file is %s", self._config_file)
        self._magic = {
            "add_host": args.add_host,
            "update_host": args.update_host,
            "toggle_host": args.toggle_host,
            "delete_host": args.delete_host,
            "without_migration": args.without_migration
        }
        self._config = configparser.SafeConfigParser()
        self._load()

    def reload(self):
        """Reload configuration"""
        _LOGGER.info("Reloading configuration")
        self._load()

    def get(self, section, setting):
        """
        Get a configuration setting

        :param string section: Configuration section
        :param string setting: Required setting to get
        :return: Configuration value
        :rtype: str
        """
        if section not in self._config or setting not in self._config[section]:
            if section == "magic" and setting in self._magic:
                return self._magic[setting]
            raise ValueError("Invalid setting %s on section %s" % (setting,
                                                                   section))
        return self._config.get(section, setting)

    def setlog(self):
        """Set log configuration"""

        logging.basicConfig(level=int(self.get("logging", "level")),
                            filename=self.get("logging", "file") or None,
                            format=self.get("logging", "format"))
        logging.captureWarnings(True)
