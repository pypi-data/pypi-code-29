"""Utilities."""
# -- XXX This module must not use translation as that causes
# -- a recursive loader import!
from __future__ import absolute_import, unicode_literals
import pytz
import datetime


def timezone_to_tz(timezone=None):
    if timezone is None:
        timezone = "Asia/Shanghai"
    tz = pytz.timezone(timezone)
    return tz


def make_aware(value):
    """Force datatime to have timezone information."""
    # if getattr(settings, 'USE_TZ', False):
    #     # naive datetimes are assumed to be in UTC.
    #     if timezone.is_naive(value):
    #         value = timezone.make_aware(value, timezone.utc)
    #     # then convert to the Django configured timezone.
    #     default_tz = timezone.get_default_timezone()
    #     value = timezone.localtime(value, default_tz)
    return value


def now(timezone=None):
    """Return the current date and time."""
    tz = timezone_to_tz(timezone=timezone)
    return datetime.datetime.now(tz)


def is_database_scheduler(scheduler):
    """Return true if Celery is configured to use the db scheduler."""
    if not scheduler:
        return False
    from kombu.utils import symbol_by_name
    from .schedulers import DatabaseScheduler
    return (
        scheduler == 'cbeat' or
        issubclass(symbol_by_name(scheduler), DatabaseScheduler)
    )


def timezone_to_tz(timezone="UTC"):
    if timezone is None:
        timezone = "UTC"
    tz = pytz.timezone(str(timezone))
    return tz
