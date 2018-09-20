#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__doc__ = """

Test logging level
------------------

Test suite for logging_level.

"""

import logging
from unittest import TestCase, mock

from dataf import LoggingLevel


class TestLoggingLevel(TestCase):
    """
    Test for LoggingLevel class.
    """
    def test_slack(self):
        """
        Test slack method.
        """
        logging.addLevelName(60, 'SLACK')
        logging.Logger.slack = LoggingLevel.slack
        logger = logging.getLogger(__name__)
        with self.assertLogs(logger, 'SLACK'):
            logger.slack('test')

    def test_mail(self):
        """
        Test mail method.
        """
        logging.addLevelName(70, 'MAIL')
        logging.Logger.mail = LoggingLevel.mail
        logger = logging.getLogger(__name__)
        with self.assertLogs(logger, 'MAIL'):
            logger.mail('test')
