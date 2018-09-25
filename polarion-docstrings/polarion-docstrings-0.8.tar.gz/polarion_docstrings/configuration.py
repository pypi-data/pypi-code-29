# -*- coding: utf-8 -*-
"""
Loads configuration.
"""

from __future__ import absolute_import, unicode_literals

import glob
import io
import os

import yaml

DEFAULT_CONF = os.path.join(os.path.dirname(os.path.abspath(__file__)), "polarion_tools.yaml")
PROJECT_CONF_DIRS = ("conf", ".")
PROJECT_CONF = "polarion_tools*.yaml"


def find_vcs_root(path, dirs=(".git",)):
    """Searches up from a given path to find the project root."""
    prev, path = None, os.path.abspath(path)
    while prev != path:
        if any(os.path.exists(os.path.join(path, d)) for d in dirs):
            return path
        prev, path = path, os.path.abspath(os.path.join(path, os.pardir))
    return None


def _get_project_conf():
    """Loads configuration from project config file."""
    config_settings = {}

    project_root = find_vcs_root(".")
    if project_root is None:
        return config_settings

    for conf_dir in PROJECT_CONF_DIRS:
        conf_dir = conf_dir.lstrip("./")
        joined_dir = os.path.join(project_root, conf_dir) if conf_dir else project_root
        joined_glob = os.path.join(joined_dir, PROJECT_CONF)
        conf_files = glob.glob(joined_glob)
        if conf_files:
            break
    else:
        conf_files = []

    for conf_file in conf_files:
        try:
            with io.open(conf_file, encoding="utf-8") as input_file:
                loaded_settings = yaml.load(input_file)
        except EnvironmentError:
            pass
        else:
            config_settings.update(loaded_settings)

    return config_settings


def get_config():
    """Loads configuration.

    Args:
        default_only: bool if only default config will be loaded (for easier testing)
    """
    with io.open(DEFAULT_CONF, encoding="utf-8") as input_file:
        config_settings = yaml.load(input_file)

    # merge with project configuration
    project_conf = _get_project_conf()
    config_settings.update(project_conf)

    return config_settings
