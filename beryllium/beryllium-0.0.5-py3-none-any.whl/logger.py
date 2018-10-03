# -*- coding:utf-8 -*-

import logging
from logging.handlers import TimedRotatingFileHandler
import os


def get_logger(log_file_name):
    """
    日志文件
    :param log_file_name:
    :return:
    """
    # os.mkdir()
    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.DEBUG)
    handler = TimedRotatingFileHandler(filename=os.path.join("logs", "log_%s" % log_file_name),
                                       when="h", interval=1, backupCount=7)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(formatter)
    logger.addHandler(handler)
    logger.addHandler(console)
    logger.info("Start print log")
    return logger
