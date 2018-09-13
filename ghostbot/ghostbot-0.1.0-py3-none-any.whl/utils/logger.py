import logging
from ghostbot.utils.os import FileSystem
from ghostbot.utils.json import Json


class Logger(object):
    LOGGER_JSON = "settings/logger.json"
    DEFAULT_FORMAT = "%(asctime)s [%(levelname)-8s] %(message)s"
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL

    def __init__(self, name):
        self.configure()
        self._logger = logging.getLogger(name)

    def configure(self):
        path = FileSystem.join(FileSystem.abspath(".."), self.LOGGER_JSON)
        if FileSystem.exists(path):
            config = Json.load(path)
            logging.config.dictConfig(config)
        else:
            logging.basicConfig(level="DEBUG", format=self.DEFAULT_FORMAT)

    def level(self, level):
        self._logger.setLevel(level)

    def debug(self, message, *args):
        self._logger.debug(message.format(*args))

    def info(self, message, *args):
        self._logger.info(message.format(*args))

    def warning(self, message, *args):
        self._logger.warning(message.format(*args))

    def error(self, message, *args):
        self._logger.error(message.format(*args))

    def critical(self, message, *args):
        self._logger.critical(message.format(*args))
