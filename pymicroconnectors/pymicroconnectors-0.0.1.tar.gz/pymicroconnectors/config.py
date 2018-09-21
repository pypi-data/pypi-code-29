"""
Created by ddelizia

Config utility to provide easy access to the app configuration
"""

import logging
import os
from functools import lru_cache

from figgypy import Config as Figgypy


def _configure_logger():
    logger_config = get_config().get('logger')
    if logger_config is not None:
        for key in logger_config:
            level = logging.getLevelName(logger_config.get(key))
            logging.getLogger(key).setLevel(level)

def _select_file():
    file_path = os.environ.get('ENV')
    if file_path is None:
        file_path = 'config/config.yml'
    return file_path

def _get_path(dot_notation):
    return dot_notation.split('.')

@lru_cache(maxsize=1)
def get_config() -> dict:
    return cfg.values

@lru_cache(maxsize=256)
def get_value(dot_notation: str, the_type=None):
    path = _get_path(dot_notation)
    current = get_config()

    for element in path:
        current = current.get(element)

    if type is not None:
        pass

    return current


cfg = Figgypy(config_file=_select_file(),
              decrypt_gpg=False,
              decrypt_kms=False)
_configure_logger()


