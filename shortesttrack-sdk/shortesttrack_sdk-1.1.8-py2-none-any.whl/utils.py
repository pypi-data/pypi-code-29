import sys
import logging

import requests

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


def do_post(url, headers, body: dict = None) -> requests.Response:
    body = body if body else {}
    root_logger.info(f'request POST: {url} {body}')
    root_logger.debug(f'request POST: {url} {headers} {body}')

    response = requests.post(url=url, headers=headers, json=body)
    root_logger.info(f'response: {response.status_code} {response.content}')

    if response.status_code not in (200, 201):
        raise Exception(response.status_code)

    return response


def do_get(url, headers) -> requests.Response:
    root_logger.info(f'request GET: {url}')
    root_logger.debug(f'request GET: {url} {headers}')

    response = requests.get(url, headers=headers)
    root_logger.info(f'response: {response.status_code} {response.content}')

    if response.status_code not in (200, 201):
        raise Exception(response.status_code)

    return response
