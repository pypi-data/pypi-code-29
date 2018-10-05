# -*- coding: utf-8 -*-


import logging


class ColorFormatter(logging.Formatter):
    """Formatter supporting colors."""
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    ORANGE = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHTGRAY = "\033[0;37m"
    DARKGRAY = "\033[1;30m"
    LIGHTRED = "\033[1;31m"
    LIGHTGREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHTBLUE = "\033[1;34m"
    LIGHTPURPLE = "\033[1;35m"
    LIGHTCYAN = "\033[1;36m"
    WHITE = "\033[1;37m"
    NC = "\033[0m"

    COLORS = {
        logging.DEBUG: BLUE,
        logging.INFO: WHITE,
        logging.WARNING: YELLOW,
        logging.ERROR: LIGHTRED,
        logging.CRITICAL: RED,
    }

    def format(self, record):
        """Same as logging formatter except it adds color."""
        color = self.COLORS[record.levelno]
        return "{}{}{}".format(color, logging.Formatter.format(self, record), self.NC)


def setup_logger(name: str, level: int, to_file: bool = False):
    """"""
    logger = logging.getLogger(name)
    logger.setLevel(level)
    formatter = ColorFormatter(fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')

    if to_file:
        file_handler = logging.FileHandler(f'{name}.log')
        # file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    else:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger
