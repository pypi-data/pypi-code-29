# coding=utf-8
"""
Convenience functions to manage logging
"""

import logging as base
import logging.handlers as base_handlers
import sys
import typing
from pathlib import Path

from . import _constants
from .click_handler import ClickHandler


def _str_to_level(level: typing.Union[str, int]):
    if isinstance(level, str):
        return _constants.LEVELS[level.upper()]

    return level


def set_handler_level(
        logger: typing.Union[base.Logger, str],
        handler_name: str,
        level: typing.Union[str, int]
):
    """
    Sets output level for console handlers

    Args:
        logger: name of the logger to update
        handler_name: name of the handler (available by default: "ch", "fh"
        level: desired level
    """
    if isinstance(logger, base.Logger):
        logger = logger.name
    _constants.LOGGERS[logger][handler_name].setLevel(_str_to_level(level))


# pylint: disable=too-many-arguments
def _setup_file_logging(logger: base.Logger,
                        logger_name: str,
                        rotate_logs: bool,
                        rotate_log_when: str,
                        rotate_log_backup_count: int,
                        file_level,
                        file_format,
                        **_):
    file_path = Path(f'{logger_name}.log').absolute()
    if rotate_logs:
        file_handler: typing.Union[
            base_handlers.TimedRotatingFileHandler,
            base.FileHandler
        ] = base_handlers.TimedRotatingFileHandler(
            filename=str(file_path),
            when=rotate_log_when,
            backupCount=rotate_log_backup_count,
            encoding='utf8',
        )
    else:
        if file_path.exists():
            file_path.unlink()
        file_handler = base.FileHandler(
            filename=str(file_path),
            encoding='utf8'
        )

    file_handler.setLevel(_str_to_level(file_level))
    file_handler.setFormatter(base.Formatter(file_format))

    logger.addHandler(file_handler)
    if rotate_logs:
        logger.debug(f'added rotating file logging handler: {file_path}')
    else:
        logger.debug(f'added file logging handler: {file_path}')

    return file_handler


# pylint: disable= unused-argument
def get_logger(
        logger_name: str,
        log_to_file: bool = False,
        use_click_handler: bool = False,
        rotate_logs: bool = False,
        rotate_log_when: str = 'midnight',
        rotate_log_backup_count: int = 7,
        console_level=base.ERROR,
        file_level=base.DEBUG,
        console_format=_constants.DEFAULT_CONSOLE_FORMAT,
        file_format=_constants.DEFAULT_FILE_FORMAT,
) -> base.Logger:
    """
    Set up the logger

    :param logger_name: name of the logger
    :param log_to_file: path to log file [optional]
    :param use_click_handler: use click handler for console output
    :param rotate_logs: whether or not to rotate the log
    :param rotate_log_when: when log rotation should occur
    :param rotate_log_backup_count: number of log files to keep
    :param console_level: level for console logging
    :param file_level: level for file logging
    :param console_format: console formatter string
    :param file_format: file formatter string

    :return: logger object
    """
    if logger_name in _constants.LOGGERS:
        return _constants.LOGGERS[logger_name]['logger']

    logger = base.getLogger(logger_name)
    # if _constants.ROOT_LOGGER is None:
    #
    #     _constants.ROOT_LOGGER = logger
    # else:
    #     logger = _constants.ROOT_LOGGER.getChild(logger_name)

    logger.setLevel(base.DEBUG)

    if use_click_handler:
        console_handler: typing.Union[ClickHandler, base.StreamHandler] = ClickHandler()
    else:
        console_handler = base.StreamHandler(sys.stdout)
    console_handler.setLevel(_str_to_level(console_level))
    console_handler.setFormatter(base.Formatter(console_format))

    logger.addHandler(console_handler)
    logger.debug('added console logging handler')

    _constants.LOGGERS[logger.name] = {
        'logger': logger,
        'ch': console_handler,
    }

    if log_to_file:
        file_handler = _setup_file_logging(
            logger,
            logger_name,
            rotate_logs,
            rotate_log_when,
            rotate_log_backup_count,
            file_level,
            file_format
        )
        _constants.LOGGERS[logger.name]['fh'] = file_handler

    return logger


def get_elib_logger() -> object:
    """
    Returns ELIB's logger
    """
    return ELIB_LOGGER


def _remove_all_handlers_from_logger(logger: base.Logger):
    for handler in logger.handlers:
        logger.removeHandler(handler)


def set_root_logger(logger_name: typing.Union[base.Logger, str]):
    """
    Sets the root logger

    This will attache the root logger handlers to all other loggers available


    Args:
        logger_name: name of the root logger
    """
    if isinstance(logger_name, base.Logger):
        logger_name = logger_name.name

    _constants.ROOT_LOGGER = _constants.LOGGERS[logger_name]['logger']
    for this_logger_name in _constants.LOGGERS:
        if this_logger_name == logger_name:
            continue

        this_logger = _constants.LOGGERS[this_logger_name]['logger']
        if isinstance(this_logger, base.Logger):
            _remove_all_handlers_from_logger(this_logger)
            if _constants.ROOT_LOGGER:
                for handler in _constants.ROOT_LOGGER.handlers:
                    this_logger.addHandler(handler)


def get_root_logger():
    """
    Returns: current root logger
    """
    if _constants.ROOT_LOGGER is None:  # pragma: no cover
        raise ValueError('no root logger set')
    return _constants.ROOT_LOGGER


ELIB_LOGGER = get_logger('ELIB')
