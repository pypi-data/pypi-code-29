# -*- coding: utf-8 -*-

import pytest


def pytest_configure(config):
    """Register the "run" marker."""

    config_line = (
        'atomic: specify a atomic test. '
        'See also:'
    )
    config.addinivalue_line('markers', config_line)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.failed and item.get_closest_marker('atomic'):
        item.parent._previous_failed = True
        item.parent._skip_reason = item.get_closest_marker('atomic').args[0] if item.get_closest_marker('atomic').args else 'This is atomic testsuit!'


def pytest_runtest_setup(item):
    if getattr(item.parent, '_previous_failed', False) and not item.get_closest_marker('electronic'):
        pytest.skip(item.parent._skip_reason)
