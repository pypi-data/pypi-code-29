import logging
import sys

APPLICATION_LOG_NAME = 'shortesttrack-sdk'
DEFAULT_FORMATTER = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

LOG_LEVEL = 'INFO'
root_logger = logging.getLogger()
root_logger.setLevel(LOG_LEVEL)

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(DEFAULT_FORMATTER)
root_logger.addHandler(stream_handler)


def getLogger(short_name: str = None, log_level: str = LOG_LEVEL):
    name = _get_qualified_name(short_name)
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    return logger


def _get_qualified_name(name: str) -> str:
    if name:
        return f'{APPLICATION_LOG_NAME}.{name}'

    return APPLICATION_LOG_NAME
