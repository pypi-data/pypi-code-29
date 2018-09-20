import configparser

from zensols.actioncli import Config


class AppConfig(Config):
    def __init__(self, config_file=None, default_section='default',
                 default_vars=None):
        Config.__init__(self, config_file, default_section, default_vars)

    def _create_config_parser(self):
        inter = configparser.ExtendedInterpolation()
        return configparser.ConfigParser(interpolation=inter)
