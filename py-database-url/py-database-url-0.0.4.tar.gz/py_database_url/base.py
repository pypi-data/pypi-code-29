import os

try:
    # Python 3
    from urllib.parse import urlparse

except ImportError:
    # Python 2
    from urlparse import urlparse


DEFAULT_ENV = "DATABASE_URL"


def parse(url=None):
    """
    Parses a database URL.
    """

    if url:
        return urlparse(url)

    url = os.environ.get(DEFAULT_ENV)
    return urlparse(url)
