#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__doc__ = """

Logging level
-------------

Custom level for logging.

"""


class LoggingLevel:
    """
    Custom logging level.
    """
    name_to_level = {
        'SLACK': 60,
        'MAIL': 70,
    }

    @staticmethod
    def slack(self, message, *args, **kwargs):
        """
        Custom level for slack logging.
        """
        self._log(LoggingLevel.name_to_level['SLACK'], message, args, **kwargs)

    @staticmethod
    def mail(self, message, *args, **kwargs):
        """
        Custom level for mail logging.
        """
        self._log(LoggingLevel.name_to_level['MAIL'], message, args, **kwargs)
