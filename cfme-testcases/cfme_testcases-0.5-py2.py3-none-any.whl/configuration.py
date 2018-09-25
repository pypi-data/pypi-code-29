# -*- coding: utf-8 -*-
"""
Configuration loading.
"""

from __future__ import absolute_import, unicode_literals

from cfme_testcases import consts
from dump2polarion import configuration

CONF_DEFAULTS = {"pytest_collect": consts.PYTEST_CMD}


def get_config(conf_file_name):
    """Loads configuration."""
    dump2polarion_config = configuration.get_config(conf_file_name) if conf_file_name else {}

    config = {}
    config.update(CONF_DEFAULTS)
    # merge default and dump2polarion configuration
    config.update(dump2polarion_config)

    return config
