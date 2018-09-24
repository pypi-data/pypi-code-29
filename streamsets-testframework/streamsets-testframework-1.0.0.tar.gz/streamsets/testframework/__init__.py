# Copyright 2017 StreamSets Inc.

import logging

import colorlog


formatter = colorlog.ColoredFormatter(
    (
        '%(asctime)s '
        '[%(log_color)s%(levelname)s%(reset)s] '
        '[%(cyan)s%(name)s%(reset)s] '
        '%(message_log_color)s%(message)s'
    ),
    datefmt='%Y-%m-%d %I:%M:%S %p',
    reset=True,
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'bold_yellow',
        'ERROR': 'bold_red',
        'CRITICAL': 'bold_red,bg_white',
    },
    secondary_log_colors={
        'message': {
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'bold_yellow',
            'ERROR': 'bold_red',
            'CRITICAL': 'bold_red,bg_white',
        },
    },
    style='%'
)
handler = logging.StreamHandler()
handler.setFormatter(formatter)
# Handler is added to the streamsets logger to propagate to both
# the SDK and the Test Framework's loggers.
logger = logging.getLogger('streamsets')
logger.addHandler(handler)
