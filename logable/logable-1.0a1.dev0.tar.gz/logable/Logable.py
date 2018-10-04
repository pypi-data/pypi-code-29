import logging

from abc import ABCMeta


class Logable(metaclass=ABCMeta):

    def __init__(self):

        format_log = "%(levelname)-8s:%(name)-21s:[%(asctime)s]  %(message)s"

        self.log = logging.getLogger(self.__class__.__name__)
        self.log.setLevel(level=logging.DEBUG)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(fmt=logging.Formatter(format_log))
        console_handler.setLevel(level=logging.DEBUG)
        self.log.addHandler(console_handler)
