import logging
import sys
import time

from .db import DB
from .migrate import migrate
from .utils import get_db_from_url
from .version import Version


def config_log(level=None, handlers=None):
    # the root logger for the lib
    root_logger = logging.getLogger("ww.migration")

    if level:
        root_logger.setLevel(level)

    if not handlers:
        log_format = "%(asctime)s - %(name)s - %(levelname)s - %(process)d - %(filename)s:%(funcName)s:%(lineno)d - %(message)s"
        log_formatter = logging.Formatter(log_format)

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(log_formatter)
        console_handler.formatter.converter = time.gmtime

        handlers = [console_handler]

    for handler in handlers:
        root_logger.addHandler(handler)
