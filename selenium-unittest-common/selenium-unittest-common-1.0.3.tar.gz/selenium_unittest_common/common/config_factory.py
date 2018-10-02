"""Create configuration"""

import configparser

class ConfigFactory():
    """ConfigFactory Class"""
    def __init__(self, config_file):
        """Constructor for ConfigFactory class"""
        self.config_file = config_file

    def create(self):
        """Read the configuration file and create a configuration object"""
        config = configparser.RawConfigParser(allow_no_value=True)
        config.read_file(open(self.config_file))
        return config
