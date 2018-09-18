# -*- coding:utf-8 -*-
import logging


COLOR_FORMAT = (
    "%(color)s%(asctime)s [%(process)d] [%(thread)d] %(levelname)s : %(message)s%(color_stop)s"
)


class ColorFormatter(logging.Formatter):

    LEVEL_COLORS = {
        logging.DEBUG: '\033[00;32m',  # GREEN
        logging.INFO: '\033[00;36m',  # CYAN
        logging.WARN: '\033[01;33m',  # BOLD YELLOW
        logging.ERROR: '\033[01;31m',  # BOLD RED
        logging.CRITICAL: '\033[01;31m',  # BOLD RED
    }

    COLOR_STOP = '\033[0m'

    def add_color(self, record):
        if getattr(record, "_is_tty", False) and record.levelno > logging.INFO:
            record.color = self.LEVEL_COLORS[record.levelno]
            record.color_stop = self.COLOR_STOP
        else:
            record.color = ""
            record.color_stop = ""

    @staticmethod
    def remove_color(record):
        del record.color
        del record.color_stop

    def format(self, record):
        self.add_color(record)
        s = super(ColorFormatter, self).format(record)
        self.remove_color(record)
        return s


TEXT_FORMATTER = ColorFormatter(fmt=COLOR_FORMAT)