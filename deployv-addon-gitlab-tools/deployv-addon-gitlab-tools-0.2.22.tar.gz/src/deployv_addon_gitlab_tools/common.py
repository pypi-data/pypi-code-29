# coding: utf-8
import logging
from os import environ


_logger = logging.getLogger('deployv.' + __name__)


def check_env_vars(*args, **kwargs):
    missing = []
    not_required = ['psql_image', 'push_image']
    for key in args:
        if key not in not_required and not (key.upper() in environ and environ[key.upper()]):
            missing.append(key.upper())
    for key in kwargs:
        if not (key.upper() in environ and environ[key.upper()]):
            if kwargs[key]:
                environ[key.upper()] = str(kwargs[key])
            elif key not in not_required:
                missing.append(key.upper())
    assert not missing, (
        "Some environment variables were not found: {keys}".format(
            keys=", ".join(missing)
        ))


def get_main_app():
    if environ.get('INSTALL', False):
        _logger.warning('Deprecation warning: you should not use INSTALL env var, replace it with MAIN_APP instead')
        return environ.get('INSTALL')
    return environ.get('MAIN_APP', False)
