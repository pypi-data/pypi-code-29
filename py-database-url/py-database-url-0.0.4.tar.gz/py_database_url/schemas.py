# -*- coding: utf-8 -*-

from .base import parse


def orator(url=None, prefix=None):
    """
    Function to parser for orator format.
    """

    url = parse(url)

    config = {
        f"{url.scheme}": {
            "driver": url.scheme,
            "host": url.hostname,
            "database": url.path[1:],
            "user": url.username,
            "password": url.password,
            "prefix": prefix or "",
        }
    }

    return config
