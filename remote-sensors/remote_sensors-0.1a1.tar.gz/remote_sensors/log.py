"""Logger module."""
import logging.config
import os
import sys


LOGGING_CONFIG_DEFAULTS = dict(
    version=1,
    disable_existing_loggers=False,

    loggers={
        'remote_sensors': {
            'level': os.getenv('LOGGING_LEVEL', 'INFO'),
            'handlers': ['console']
        },
        'error': {
            'level': 'INFO',
            'handlers': ['error_console'],
            'propagate': True,
            'qualname': 'error'
        },
    },
    handlers={
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'generic',
            'stream': sys.stdout
        },
        'error_console': {
            'class': 'logging.StreamHandler',
            'formatter': 'generic',
            'stream': sys.stderr
        },
    },
    formatters={
        'generic': {
            'format': '[%(processName)s - %(threadName)s - %(module)s - %(funcName)s] [%(levelname)s] %(message)s',  # noqa
            'class': 'logging.Formatter',
        },
    }
)

logging.config.dictConfig(LOGGING_CONFIG_DEFAULTS)

logger = logging.getLogger('remote_sensors')

error_logger = logging.getLogger('error')
