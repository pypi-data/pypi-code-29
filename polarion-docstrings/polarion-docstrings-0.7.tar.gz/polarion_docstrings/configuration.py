# -*- coding: utf-8 -*-
"""
Loads configuration.
"""

from __future__ import absolute_import, unicode_literals

import io
import os

import yaml

DEFAULT_CONF = os.path.join(os.path.abspath(os.path.dirname(__file__)), "polarion_tools.yaml")
PROJECT_CONFS = ("polarion_tools.yaml", "conf/polarion_tools.yaml")
USER_CONF = os.path.expanduser("~/.config/dump2polarion.yaml")


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
    default_conf = {}

    project_root = find_vcs_root(".")
    if project_root is None:
        return default_conf

    for pconf in PROJECT_CONFS:
        try:
            with io.open(os.path.join(project_root, pconf), encoding="utf-8") as input_file:
                return yaml.load(input_file)
        except EnvironmentError:
            pass

    return default_conf


def _get_user_conf():
    """Loads configuration from user config file."""
    try:
        with io.open(USER_CONF, encoding="utf-8") as input_file:
            return yaml.load(input_file)
    except EnvironmentError:
        pass

    return {}


def get_config(default_only=False):
    """Loads configuration.

    Args:
        default_only: bool if only default config will be loaded (for easier testing)
    """
    with io.open(DEFAULT_CONF, encoding="utf-8") as input_file:
        config_settings = yaml.load(input_file)

    if default_only:
        return config_settings

    # merge with project configuration
    project_conf = _get_project_conf()
    config_settings.update(project_conf)

    # merge with user configuration
    user_conf = _get_user_conf()
    config_settings.update(user_conf)

    return config_settings
