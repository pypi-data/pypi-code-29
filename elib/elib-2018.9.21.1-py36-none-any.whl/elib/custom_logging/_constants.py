# coding=utf-8
"""
Logging constants
"""
import logging as base
import typing

DEFAULT_CONSOLE_FORMAT = '%(relativeCreated)08d ms ' \
                         '%(levelname)8s ' \
                         '%(name)s ' \
                         '%(message)s'
# noinspection SpellCheckingInspection
DEFAULT_FILE_FORMAT = '%(asctime)s %(levelname)8s %(name)s ' \
                      '%(process)d %(processName)s ' \
                      '%(thread)d %(threadName)s ' \
                      '%(pathname)s[%(lineno)d].%(funcName)s: ' \
                      '%(message)s'
LOGGERS: dict = {}
ROOT_LOGGER: typing.Optional[base.Logger] = None
# noinspection SpellCheckingInspection
LEVELS = {
    'DEBUG': base.DEBUG,
    'INFO': base.INFO,
    'WARNING': base.WARN,
    'WARN': base.WARN,
    'ERROR': base.ERROR,
    'ERR': base.ERROR,
    'CRITICAL': base.CRITICAL,
    'CRIT': base.CRITICAL,
}
