# coding: utf-8;
"""
Configuration file handling.
"""
try:
    from ConfigParser import ConfigParser
except ImportError:
    from configparser import ConfigParser


def parse(path=None):
    """
    Read the configuration and return a populated ConfigParser object.

    Places to look for the configuration file, in order:
    * configuration file specified by the EAGLE_CONFIG
      environment variable.
    * $XDG_CONFIG_HOME/eagle.conf
    * ~/.config/eagle.conf

    The first file that is encountered is used.
    """
    if not path:
        path = get_path()
    config = ConfigParser()
    config.read(path)
    return config
