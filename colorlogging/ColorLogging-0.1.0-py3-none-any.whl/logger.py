#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  colorlogging/logger.py
#  v.0.1.0
#  Developed in 2018 by Travis Kessler <travis.j.kessler@gmail.com>
#
#  A simple Python logger with colored log levels
#

# Python stdlib imports
from inspect import currentframe, getframeinfo
import logging
import time
import copy
import os

# 3rd party imports
import colorama

# Log format (for stream output and file content)
LOG_FORMAT = '[%(asctime)s] [%(call_loc)s] [%(levelname)s] %(message)s'

# File format (timestamp.log)
FILE_FORMAT = '{}.log'.format(str(time.time()).split('.')[0])

# Colorama colors for log levels
COLORS = {
    logging.DEBUG: colorama.Fore.GREEN,
    logging.INFO: colorama.Fore.CYAN,
    logging.WARN: colorama.Fore.YELLOW,
    logging.ERROR: colorama.Fore.RED,
    logging.CRITICAL: colorama.Fore.LIGHTRED_EX
}


class ColorFormatter(logging.Formatter):
    '''
    Logging formatter for coloring log level in output stream
    '''

    def format(self, record, *args, **kwargs):
        if record.levelno not in COLORS.keys():
            raise ValueError(
                '{} not available for coloring'.format(record.levelname)
            )
        record_n = copy.copy(record)
        record_n.levelname = '{}{}{}'.format(
            COLORS[record_n.levelno],
            record_n.levelname,
            colorama.Style.RESET_ALL
        )
        return super(ColorFormatter, self).format(record_n, *args, **kwargs)


class ColorLogger:
    '''
    Color logger: colors log levels in output stream
    '''

    def __init__(self, log_dir='logs', set_level='debug', use_color=True):
        '''
        *log_dir*   -   name of directory to save logs
        *set_level* -   minimum level to stream/save (default == 'debug')
        *use_color* -   True == use color formatting, False == don't
        '''

        colorama.init()
        self.__logger = logging.Logger(__name__)
        s_handler = logging.StreamHandler()
        if use_color:
            s_handler.setFormatter(ColorFormatter(LOG_FORMAT, '%H:%M:%S'))
        else:
            s_handler.setFormatter(logging.Formatter(LOG_FORMAT, '%H:%M:%S'))
        if not os.path.exists(log_dir):
            os.mkdir(log_dir)
        f_handler = logging.FileHandler(
            os.path.join(log_dir, FILE_FORMAT)
        )
        f_handler.setFormatter(logging.Formatter(LOG_FORMAT, '%H:%M:%S'))
        self.__logger.addHandler(s_handler)
        self.__logger.addHandler(f_handler)
        self.__log_fns = {
            'debug': self.__logger.debug,
            'info': self.__logger.info,
            'warn': self.__logger.warning,
            'error': self.__logger.error,
            'crit': self.__logger.critical
        }
        self.set_level(set_level)

    def set_level(self, level):
        '''
        Set the ColorLogger's minimum log level to *level*
        '''

        levels = {
            'debug': logging.DEBUG,
            'info': logging.INFO,
            'warn': logging.WARN,
            'error': logging.ERROR,
            'crit': logging.CRITICAL
        }
        if level not in levels.keys():
            raise ValueError('{} is not a valid log level'.format(level))
        self.__logger.setLevel(levels[level])

    def log(self, level, message):
        '''
        Log a *message* at log level *level*
        '''

        if level not in self.__log_fns.keys():
            raise ValueError('{} not a valid logging level'.format(level))

        call_loc = {'call_loc': '{}:{}'.format(
            getframeinfo(currentframe().f_back).function,
            getframeinfo(currentframe().f_back).lineno
        )}

        self.__log_fns[level](message, extra=call_loc)
