import logging
import uuid
import sys

from logging import StreamHandler
from logging.handlers import RotatingFileHandler
from colorlog import ColoredFormatter

if 'flask' in sys.modules:
    import flask


class CustomConsoleHandler(logging.StreamHandler):
    '''
    Custom Console handler
    '''

    def __init__(self, formatter, *args, **kwargs):
        StreamHandler.__init__(self, *args, **kwargs)
        self.addFilter(RequestIdFilter())
        self.setFormatter(formatter)


class CustomFileHandler(RotatingFileHandler):
    '''
    Custom File Handler
    '''

    def __init__(self, file_formatter, *args, **kwargs):
        RotatingFileHandler.__init__(self, *args, **kwargs)
        self.addFilter(RequestIdFilter())
        self.setFormatter(file_formatter)


class RequestIdFilter(logging.Filter):
    '''
    Request Filter to log request id when coming from python
    '''

    def filter(self, record):
        def generate_request_id(original_id=''):
            new_id = uuid.uuid4()

            if original_id:
                new_id = "{},{}".format(original_id, new_id)

            return new_id

        def request_id():
            if 'flask' not in sys.modules:
                return
            if getattr(flask.g, 'request_id', None):
                return flask.g.request_id

            headers = flask.request.headers
            original_request_id = headers.get("X-Request-Id")
            new_uuid = generate_request_id(original_request_id)
            flask.g.request_id = new_uuid
            return new_uuid

        record.request_id = f'({request_id()})' if 'flask'  in sys.modules and flask.has_request_context() else ''
        return True

def init():
    LOGFORMAT = "[%(asctime)s] [%(name)s] [%(levelname)s] (%(request_id)s) - %(message)s"
    COLOR_LOGFORMAT = "%(log_color)s[%(asctime)s] [%(levelname)-5s] (%(request_id)s) [%(name)s:%(lineno)s]%(reset)s - %(log_color)s%(message)s%(reset)s"

    file_formatter = logging.Formatter(LOGFORMAT)
    colored_formatter = ColoredFormatter(COLOR_LOGFORMAT)
    logging.root.addHandler(CustomConsoleHandler(colored_formatter))
    logging.root.setLevel(logging.ERROR)

def change_level(logger, level):
    level = logging.getLevelName(level)
    logging.getLogger(logger).setLevel(level)