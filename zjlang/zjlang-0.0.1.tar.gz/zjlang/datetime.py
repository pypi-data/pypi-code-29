"""
ZJLANG datetime utils functions

author: tim.tang
date: 2018-09-01
"""

from datetime import date as __date
from datetime import datetime as __datetime
from datetime import timedelta as __timedelta
import time


def today(with_time=False):
  if with_time:
    return __datetime.today()
  return __date.today()


def is_leap(year):
  assert 1 <= year <= 9999
  return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def plus_days(days, date=None):
  """
  Plus days to date, days could be negative.
  """
  if date is None:
    date = today()
  else:
    assert isinstance(date, __date) or isinstance(date, __datetime)

  return __timedelta(days=days) + date


def plus_hours(hours, date=None):
  """
  Plus hours to datetime, hours could be negative.
  """
  if date is None:
    date = today(with_time=True)
  else:
    assert isinstance(date, __datetime)

  return __timedelta(hours=hours) + date


def timestamp():
  """
  Get UTC timestamp
  """
  t1 = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
  t2 = str(int(time.time()))

  return t1, t2
