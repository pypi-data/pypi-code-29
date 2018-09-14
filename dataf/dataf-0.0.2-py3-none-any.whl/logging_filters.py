#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__doc__ = """

Logging filters
---------------

Custom filters for logging.

"""

import logging


class LvlFilter(logging.Filter):
    """
    Custom filter based on level, log only if level is equal or between two value.

    :param int low: low level value.
    :param int high: high level value.
    """
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def filter(self, record):
        """
        Determine if the specified record is to be logged.

        :param obj record: record obj to log.
        :return: True if record must be logged otherwise False.
        """
        return self.low <= record.levelno <= self.high
