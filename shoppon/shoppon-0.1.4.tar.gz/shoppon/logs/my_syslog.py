# coding: utf-8
import logging
from logging.handlers import SysLogHandler

import syslog


def init():
    # 指定syslog的programname
    syslog.openlog('shoppon')


def get_logger():
    logger = logging.getLogger(__name__)
    logger.addHandler(SysLogHandler())
