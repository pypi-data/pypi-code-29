# -*- coding: utf-8 -*-
"""
Various input-based release history classes

ReleaseLogFile
   Read history from a disk file
ReleaseLogURL
   Read history from a URL
"""

from releaselogparser import ReleaseLog
from sys import version_info

class ReleaseLogFile(ReleaseLog):
    """Read history log entries from a disk file.
    Usage:

      hist = ReleaseLogFile(fmt, file [, args...])

    Arguments:

    fmt    - History format
    file   - Name of the file to read history from
    args   - Additional keyword arguments. See ReleaseLog for a description
             of these.
    """
    
    def __new__(cls, type, file, **kwargs):
        return ReleaseLog.__new__(cls, type, open(file, 'r'), **kwargs)


class ReleaseLogURL(ReleaseLog):
    """Read history log entries from a URL.
    Usage:

      hist = ReleaseLogURL(fmt, url [, args...])

    Arguments:

    fmt    - History format
    url    - URL to read history from
    args   - Additional keyword arguments. See ReleaseLog for a description
             of these.

    Note: URL must return Content-Type: text/plain
    """
    def __new__(cls, type, url, **kwargs):
        if version_info[0] > 2:
            from urllib.request import urlopen
        else:
            from urllib2 import urlopen
        return ReleaseLog.__new__(cls, type, urlopen(url), **kwargs)


    
