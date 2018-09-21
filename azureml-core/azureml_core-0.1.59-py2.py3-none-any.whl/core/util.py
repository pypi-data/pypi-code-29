# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

""" util.py for utilities"""
import logging


class NewLoggingLevel(object):
    """
    A class for setting up logging levels.
    """
    def __init__(self, logger_name, level=logging.WARNING):
        """
        :param: logger_name
        :param: level
        """
        self.logger_name = logger_name
        self.logger = logging.getLogger(logger_name)
        self.old_level = self.logger.level
        self.new_level = level

    def __enter__(self):
        """
        :return: logger
        """
        self.logger.setLevel(self.new_level)
        return self.logger

    def __exit__(self, et, ev, tb):
        """
        :param: et
        :param: ev
        :param: tb
        """
        self.logger.setLevel(self.old_level)
