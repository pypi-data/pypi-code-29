import logging
import logging.config
import re
import datetime
import traceback
from pymongo import MongoClient
from ghostbot import Ghostbot, GhostbotProfile
from ghostbot.utils.os import FileSystem
from ghostbot.utils.json import Json
from ghostbot.utils.string import String


class Logger(object):
    LOGGER_JSON = "logger.json"
    DEFAULT_FORMAT = "%(asctime)s [%(levelname)-8s] %(message)s"
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL

    def __init__(self, name, mongodb=None, job_id=None):
        self.configure()
        self._logger = logging.getLogger(name)
        if mongodb:
            handler = MongoHandler(self._logger, database=mongodb, job_id=job_id)
            if handler.is_available():
                self._logger.addHandler(handler)
            else:
                self.critical("Failed to append MongoHandler: mongodb={}".format(mongodb))

    def configure(self):
        settings_directory = Ghostbot.settings_directory()
        if settings_directory is None:
            settings_directory = GhostbotProfile.settings
        path = FileSystem.join(settings_directory, self.LOGGER_JSON)
        if FileSystem.exists(path):
            config = Json.load(path)
            filename = config["handlers"]["file"]["filename"]
            logs_directory = Ghostbot.logs_directory()
            if logs_directory is None:
                logs_directory = GhostbotProfile.logs
            config["handlers"]["file"]["filename"] = FileSystem.join(logs_directory, filename)
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


class MongoHandler(logging.Handler, logging.Formatter):
    MONGODB_DSN = "mongodb://{host}:{port}/"
    DEFAULT_HOST = "localhost"
    DEFAULT_PORT = 27017
    DEFAULT_DB = "logging"
    DEFAULT_COLLECTION = "logs"
    REGEXP_CODE = "^<\d{1,}> "

    def __init__(self, logger, level=logging.NOTSET, host=DEFAULT_HOST, port=DEFAULT_PORT,
                 database=DEFAULT_DB, collection=DEFAULT_COLLECTION, job_id=None):
        logging.Handler.__init__(self, level)
        self.logger = logger
        self.mongodb = None
        self.db = None
        self.collection = collection
        self.job_id = job_id
        self._connect(host, port, database)

    def is_available(self):
        return self.mongodb is not None and self.db is not None

    def _connect(self, host, port, database):
        try:
            self.mongodb = MongoClient(self.MONGODB_DSN.format(host=host, port=port))
            self.db = self.mongodb[database]
        except Exception as e:
            self.logger.critical("Can't connect mongodb: args={}".format(e.args))

    def emit(self, record):
        if self.is_available():
            try:
                if record.levelname != "DEBUG":
                    collection = self.db[self.collection]
                    collection.insert_one(self._format(record))
            except Exception as e:
                self.handleError(record)
                self.logger.critical("Can't insert mongodb: args={}".format(e.args))
                traceback.print_exc()
        else:
            self.logger.error("MongoHandler is not available")

    def _format(self, record):
        result = {
            "job_id": self.job_id,
            "timestamp": datetime.datetime.now(),
            "level": record.levelname
        }
        message = record.getMessage()
        regexp = re.search(self.REGEXP_CODE, message)
        if regexp:
            result["code"] = int(regexp.group()[1:-2])
            result["message"] = String.subtract(message, regexp.group())
        else:
            result["message"] = message
        if record.exc_info:
            result.update({
                "exception": {
                    "message": str(record.exc_info[1]),
                    "code": 0,
                    "stackTrace": self.formatException(record.exc_info)
                }
            })
        return result

    def close(self):
        if self.is_available():
            self.mongodb.close()
            self.mongodb = None
            self.db = None
        else:
            self.logger.error("MongoHandler is not available")

    def __exit__(self, *args):
        self.close()
