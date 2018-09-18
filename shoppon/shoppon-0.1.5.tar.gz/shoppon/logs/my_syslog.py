# coding: utf-8
import logging
from logging import Formatter
from logging import StreamHandler
from logging.handlers import SysLogHandler

try:
    import syslog
except:
    syslog = None


def init():
    # 指定syslog的programname
    syslog.openlog('shoppon')


def get_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(SysLogHandler())
    stream_handler = StreamHandler()
    formatter = Formatter("%(asctime)s [%(module)s] %(message)s")
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger
