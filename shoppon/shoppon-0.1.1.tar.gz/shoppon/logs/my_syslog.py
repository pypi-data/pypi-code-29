import logging
from logging.handlers import SysLogHandler

import syslog


def init():
    syslog.openlog('shoppon')


def get_logger():
    logger = logging.getLogger(__name__)
    logger.addHandler(SysLogHandler())
