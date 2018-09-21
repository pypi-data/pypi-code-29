# coding=utf-8

import sys

import raven
import raven.breadcrumbs
from mockito import ANY, mock, verify, verifyStubbedInvocationsAreUsed, when

from elib.sentry import Sentry, SentryContext


class DummyContext(SentryContext):
    """
    Dummy testing context
    """
    string = 'string'
    integer = 1


def test_init(caplog):
    when(raven.Client).set_dsn(...)
    when(Sentry).is_enabled().thenReturn(True)
    sentry = Sentry('dsn', 'version')
    assert sentry._version == 'version'
    assert 'Sentry is ready' in caplog.text
    verifyStubbedInvocationsAreUsed()


def test_init_with_logger(caplog):
    when(raven.Client).set_dsn(...)
    when(Sentry).is_enabled().thenReturn(True)
    when(raven.breadcrumbs).register_special_log_handler(ANY, ANY)
    when(raven.breadcrumbs).register_special_log_handler('some logger', ANY)
    sentry = Sentry('dsn', 'version', 'some logger')
    assert sentry._version == 'version'
    assert 'Sentry is ready' in caplog.text
    verify(raven.Client).set_dsn(...)
    verify(Sentry, atleast=1).is_enabled()
    verify(raven.breadcrumbs, atleast=1).register_special_log_handler('some logger', ANY)


def test_init_failed(caplog):
    when(raven.Client).set_dsn(...)
    when(Sentry).is_enabled().thenReturn(False)
    sentry = Sentry('dsn', 'version')
    assert sentry._version == 'version'
    assert 'Sentry failed to initialize' in caplog.text
    verifyStubbedInvocationsAreUsed()


def test_add_context():
    dummy_context = DummyContext()
    when(raven.Client).set_dsn(...)
    when(Sentry).is_enabled().thenReturn(True)
    sentry = Sentry('dsn', 'version')
    sentry.register_context('dummy', dummy_context)
    assert 'dummy' in sentry.registered_contexts
    assert sentry.registered_contexts['dummy'] is dummy_context
    verifyStubbedInvocationsAreUsed()


def test_set_context():
    when(raven.Client).set_dsn(...)
    when(Sentry).is_enabled().thenReturn(True)
    sentry = Sentry('dsn', 'version')
    assert 'tags' not in sentry.context
    sentry.set_context()
    assert sentry.context['tags']
    assert sentry.context['tags'] == {
        'platform': sys.platform,
        'version': 'version',
        'windows_version': sys.getwindowsversion(),
    }
    verifyStubbedInvocationsAreUsed()


def test_set_context_missing_win_version():
    when(raven.Client).set_dsn(...)
    when(Sentry).is_enabled().thenReturn(True)
    when(sys).getwindowsversion().thenRaise(AttributeError)
    sentry = Sentry('dsn', 'version')
    assert 'tags' not in sentry.context
    sentry.set_context()
    assert sentry.context['tags']
    assert sentry.context['tags'] == {
        'platform': sys.platform,
        'version': 'version',
    }
    verifyStubbedInvocationsAreUsed()


def test_capture_message():
    when(raven.Client).set_dsn(...)
    when(Sentry).is_enabled().thenReturn(True)
    when(raven.Client).capture('raven.events.Message', message='message', data={'level': 10})
    sentry = Sentry('dsn', 'version')
    sentry.captureMessage('message')
    verifyStubbedInvocationsAreUsed()


def test_capture_message_with_data():
    when(raven.Client).set_dsn(...)
    when(Sentry).is_enabled().thenReturn(True)
    when(raven.Client).capture(
        'raven.events.Message',
        message='message',
        data={'dummy': 'data', 'int': 1, 'level': 10}
    )
    data = {
        'dummy': 'data',
        'int': 1
    }
    sentry = Sentry('dsn', 'version')
    sentry.captureMessage('message', data=data)
    verifyStubbedInvocationsAreUsed()


def test_capture_message_with_level():
    when(raven.Client).set_dsn(...)
    when(Sentry).is_enabled().thenReturn(True)
    when(raven.Client).capture('raven.events.Message', message='message', data={'level': 100})
    data = {
        'level': 100,
    }
    sentry = Sentry('dsn', 'version')
    sentry.captureMessage('message', data=data)
    verifyStubbedInvocationsAreUsed()


def test_capture_message_with_context_provider():
    when(raven.Client).set_dsn(...)
    when(Sentry).is_enabled().thenReturn(True)
    when(raven.Client).capture('raven.events.Message', message='message', data={'level': 10})
    sentry = Sentry('dsn', 'version')
    dummy_context = DummyContext()
    sentry.register_context('dummy', dummy_context)
    sentry.captureMessage('message')
    verifyStubbedInvocationsAreUsed()


def test_capture_exception():
    when(raven.Client).set_dsn(...)
    when(Sentry).is_enabled().thenReturn(True)
    exc_info = mock()
    when(raven.Client).capture('raven.events.Exception', exc_info=exc_info)
    sentry = Sentry('dsn', 'version')
    sentry.captureException(exc_info)
    verifyStubbedInvocationsAreUsed()


def test_capture_exception_with_context_provider():
    when(raven.Client).set_dsn(...)
    when(Sentry).is_enabled().thenReturn(True)
    exc_info = mock()
    when(raven.Client).capture('raven.events.Exception', exc_info=exc_info)
    sentry = Sentry('dsn', 'version')
    dummy_context = DummyContext()
    sentry.register_context('dummy', dummy_context)
    sentry.captureException(exc_info)
    verifyStubbedInvocationsAreUsed()


def test_breadcrumbs():
    message = mock()
    category = mock()
    level = mock()
    when(raven.Client).set_dsn(...)
    when(Sentry).is_enabled().thenReturn(True)
    sentry = Sentry('dsn', 'version')
    when(raven.breadcrumbs).record(message=message, category=category, level=level)
    sentry.add_crumb(message, category, level)
    verifyStubbedInvocationsAreUsed()
