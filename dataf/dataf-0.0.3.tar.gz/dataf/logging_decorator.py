#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__doc__ = """

Logging decorator
-----------------

Suite of decorator for logging.

"""

from functools import wraps


def simple_logger(level, *, start=None, end=None, err=None, log_err=False):
    """
    Decorator for logging before and after function execution.
    Decorated function must be method in class with logger attribute.
    Log with exception level if decorated func raise an exception.

    :param str level: level of logger.
    :param str start: string to log before function exec, default: None.
    :param str end: string to log after function exec, default: None.
    :param str err: string to log if exception is raised, default: 'func_name error'.
    :param bool log_err: log error if True, default: False.
    """
    def _decorator(func):
        @wraps(func)
        def _wrapper(cls, *args, **kwargs):
            try:
                if start is not None:
                    getattr(cls.logger, level)(start)
                result = func(cls, *args, **kwargs)
                if end is not None:
                    getattr(cls.logger, level)(end)
                return result
            except Exception:
                if log_err is True:
                    nonlocal err
                    if err is None:
                        err = "{} error".format(func.__name__)
                    cls.logger.exception(err, exc_info=True)
                raise
        return _wrapper
    return _decorator


def lambda_logger(level, *, start=None, end=None, err=None, log_err=False):
    """
    Decorator for logging before and after function execution with callable as
    message, usefull if  you want to use decorated function params in logging message..
    Decorated function must be method in class with logger attribute.
    Log with exception level if decorated func raise an exception.
    class (cls) or instance (self) is always pass as cls parameter.

    :param str level: level of logger.
    :param func start: string to log before function exec, default: None.
    :param func end: string to log after function exec, default: None.
    :param func err: string to log if exception is raised, default: 'func_name error'.
    :param bool log_err: log error if True, default: False.
    """
    def _decorator(func):
        @wraps(func)
        def _wrapper(cls, *args, **kwargs):
            try:
                if start is not None:
                    getattr(cls.logger, level)(start(*args, cls=cls, **kwargs))
                result = func(cls, *args, **kwargs)
                if end is not None:
                    getattr(cls.logger, level)(end(*args, cls=cls, **kwargs))
                return result
            except Exception:
                if log_err is True:
                    nonlocal err
                    if err is None:
                        def err(*_, **__): return "{} error".format(func.__name__)
                    cls.logger.exception(
                        err(*args, cls=cls, **kwargs), exc_info=True
                    )
                raise
        return _wrapper
    return _decorator
