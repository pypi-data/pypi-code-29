import sys

py_version = sys.version_info

is_py2: bool = py_version[0] == 2
is_py3: bool = py_version[0] == 3

if is_py3:
    from bs4 import BeautifulSoup
    from urllib.parse import urlparse

if is_py2:
    from BeautifulSoup import BeautifulSoup
    from urlparse import urlparse
