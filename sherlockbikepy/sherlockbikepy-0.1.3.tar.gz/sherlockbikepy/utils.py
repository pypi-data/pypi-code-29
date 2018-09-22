# coding: utf-8

from datetime import datetime
import logging
import hashlib

import requests


LOGGER = logging.getLogger(__name__)


def sha256(value):
    '''
    Get the SHA256 of a string
    '''
    return hashlib.sha256(value.encode('utf-8')).hexdigest()


def timestamp():
    '''
    Get the current date as a timestamp
    '''
    return round(datetime.now().timestamp())


# TODO: Add a bool utc parameter (some dates are explicitely UTC)
def str2dt(datestr):
    '''
    Convert a YYYY-MM-DD H:M:S formatted string (eg: '2018-09-22 14:26:06') to
    a datetime object
    '''
    if datestr is None:
        LOGGER.error("str2dt: Missing input data")
        return
    return datetime.strptime(datestr, '%Y-%m-%d %H:%M:%S')


def request(url, params=None, method='GET'):
    res = requests.request(method, url, params=params)
    if not res.ok:
        LOGGER.error("API call failed: %s", res.text)
        return
    try:
        jres = res.json()
        LOGGER.info("Call was successful: %s", jres)
        status = jres.get("status")
        if status:
            if status != "ok":
                LOGGER.error("Error encountered: %s", jres)
                return
        return {k: v for k, v in jres.items() if k != 'status'}
    except Exception as exc:
        LOGGER.error("Error while parsing response: %s\n%s", exc, res.text)
