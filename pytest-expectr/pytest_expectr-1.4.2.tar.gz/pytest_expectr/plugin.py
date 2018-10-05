# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import inspect
import os.path

import pytest


def color(msg, color):
    '''

    :param msg: string
    :param color: string
    :return: string
    '''
    sting_format = {'red': '\033[91m', 'bold': '\033[1m'}
    return '%s%s%s' % (sting_format[color], msg, '\033[0m')


def _log_assert(node, message='None'):
    '''
    :param node: object
    :param message: string
    '''
    # inspect.getframeinfo(frame[0])
    (file_name, line, test_name, contexts) = inspect.stack()[2][1:5]
    context = contexts[0].replace('        ', '')

    if not hasattr(node, 'failed_assert'):
        node.failed_assert = []

    node.failed_assert.append(
        '    def %s():\n        ...\n%s:>     %s%s\n\n%s:%s: %s\n' % (
            color(test_name, 'bold'),
            line, color(context, 'bold'),
            color('E       AssertionError: %s' % message, 'red'),
            color('%s' % file_name, 'red'),
            line, 'AssertionError'
        )
    )


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    asserts_list = outcome.get_result()
    if (call.when == "call") and hasattr(item, 'failed_assert'):
        item.failed_assert.append(
            'Failed Expectations:%s' % len(item.failed_assert)
        )
        asserts_list.longrepr = '\n'.join(item.failed_assert)
        asserts_list.outcome = "failed"


@pytest.fixture
def expect(request):
    'This fixture is used to expect multiple assert'
    def _expect(test_expression, message=''):
        '''
        :param test_expression: boolean
        :param message: string
        '''
        if not test_expression:
            _log_assert(request.node, message)

    return _expect
