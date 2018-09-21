# coding=utf-8
"""
Connection with sentry.io
"""

import inspect
import logging
import sys
import typing

import certifi
import raven
import raven.breadcrumbs
import raven.conf
import raven.handlers.logging

import elib

LOGGER = elib.custom_logging.get_logger('ELIB')


class SentryContext:
    """
    Expose all class public members for Sentry
    """

    def get_context(self) -> dict:
        """
        Returns: dict context for Sentry
        """
        return {
            member: value
            for member, value in inspect.getmembers(self, lambda a: not inspect.ismethod(a))
            if not member.startswith('_')
        }


class Sentry(raven.Client):
    """
    Connection with sentry.io
    """

    def __init__(self, dsn: str, version: str, logger_name: str = None) -> None:
        LOGGER.info('initializing Sentry')
        self.registered_contexts: typing.Dict[str, SentryContext] = {}
        self._version = version
        raven.Client.__init__(
            self,
            f'{dsn}?ca_certs={certifi.where()}',
            release=version,
        )
        if self.is_enabled():
            LOGGER.info('Sentry is ready')
            if logger_name:
                raven.breadcrumbs.register_special_log_handler(logger_name, filter_breadcrumbs)
        else:
            LOGGER.error('Sentry failed to initialize')

    def set_context(self):
        """
        Sets Sentry context

        """
        self.tags_context(
            dict(
                platform=sys.platform,
                version=self._version,
            )
        )
        try:
            self.tags_context(dict(windows_version=sys.getwindowsversion()))
        except AttributeError:
            pass

    def register_context(self, context_name: str, context_provider):
        """Registers a context to be read when a crash occurs; obj must implement get_context()"""
        LOGGER.debug('registering context with Sentry: %s', context_name)
        self.registered_contexts[context_name] = context_provider

    @staticmethod
    def add_crumb(message, category, level):
        """
        Manually add a crumb to the logger

        Args:
            message: message str
            category: category
            level: logging level

        """
        raven.breadcrumbs.record(message=message, category=category, level=level)

    def captureMessage(self, message, **kwargs):  # noqa: N802
        """
        Manually add a message

        Args:
            message: message content
            **kwargs: meh

        """
        self.set_context()
        if kwargs.get('data') is None:
            kwargs['data'] = {}
        if kwargs['data'].get('level') is None:
            kwargs['data']['level'] = logging.DEBUG
        for context_name, context_provider in self.registered_contexts.items():
            self.extra_context({context_name: context_provider.get_context()})
        super(Sentry, self).captureMessage(message, **kwargs)

    def captureException(self, exc_info=None, **kwargs):
        """Captures an exception"""
        self.set_context()

        LOGGER.debug('capturing exception')
        for k, context_provider in self.registered_contexts.items():
            self.extra_context({k: context_provider.get_context()})
        super(Sentry, self).captureException(exc_info, **kwargs)


# noinspection PyUnusedLocal
# pylint: disable=unused-argument
def filter_breadcrumbs(_logger, level, msg, *args, **kwargs):  # pragma: no cover
    """
    Intercepts logging messages

    Args:
        _logger: originating logger
        level: record level
        msg: record message
        *args: logging args
        **kwargs: logging kwargs

    """
    skip_lvl = []
    skip_msg = []

    if level in skip_lvl or msg in skip_msg:
        return False

    if _logger == 'requests':
        return False
    return True
