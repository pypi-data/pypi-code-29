"""
ZJLANG http utils function

author: tim.tang
date: 2018-09-06
"""

import urllib.parse as parse

# http delegate to requests module
import requests


def get(url, **keywords):
  """
  Request http GET method.
  """
  return requests.get(url, **keywords)


def post(url, **keywords):
  """
  Request http POST method.
  """
  return requests.post(url, **keywords)


def urlencode(string, safe=''):
  """
  Encode url query string.

  : ' ' to '+', no safe for '/'
  """
  return parse.quote_plus(string, safe=safe)


def urldecode(string):
  return parse.unquote_plus(string)
