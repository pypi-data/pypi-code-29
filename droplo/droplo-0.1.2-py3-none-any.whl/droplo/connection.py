"""
droplo.connection
~~~~~~~~~~~

This module implements the Droplo Connection handlers.

"""

import requests
import platform
import re
from . import __version__ as droplo_version
from .cache import ShelveCache
from .exceptions import (InvalidTokenError, AuthorizationNeededError, HTTPError)


def get_json(url, access_token='', cache=None, ttl=None):
    if cache is None:
        cache = ShelveCache(access_token)
    cached = cache.get(url)
    if cached is not None:
        return cached

    response = requests.get(url, headers={
        "Authorization": "Bearer {}".format(access_token),
        "User-Agent": "droplo-python-client/%s Python/%s" % (
            droplo_version,
            platform.python_version()
        )
    })
    json_result = response.json()

    if response.status_code == 200:
        expire = ttl or get_max_age(response.headers)
        if expire is not None:
            cache.set(url, json_result, expire)
        return json_result
    elif response.status_code == 401:
        if len(access_token) == 0:
            raise AuthorizationNeededError()
        else:
            raise InvalidTokenError()
    else:
        raise HTTPError(response.status_code, str(json_result['message']))


def get_max_age(headers):
    expire_header = headers.get("Cache-Control", None)
    if expire_header is not None:
        m = re.match("max-age=(\d+)", expire_header)
        if m:
            return int(m.group(1))
    return None
