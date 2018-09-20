#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__doc__ = """

Test logging handlers
---------------------

Test suite for logging_handlers.

"""

import logging
from unittest import TestCase, mock

from slackclient import SlackClient

from dataf import SlackHandler


class TestSlackHandler(TestCase):
    """
    Tests for SlackHandler classe.
    """
    @classmethod
    def setUpClass(cls):
        cls.handler = SlackHandler('TestToken', '#channel')

    @property
    def _record(self):
        """
        Create a logging record.

        :param kwargs: optional record args.
        :return: logging record object.
        """
        record_attr = {
            'name': 'test_record',
            'level': 'ERROR',
            'pathname': '/test/path',
            'msg': 'This is a test record.',
        }
        record = logging.makeLogRecord(record_attr)
        return record

    def test_init(self):
        """
        Test __init__ method.
        """
        self.assertEqual(self.handler.channel, '#channel')
        self.assertIsInstance(self.handler.slack, SlackClient)

    @mock.patch('dataf.logging_handlers.SlackClient')
    def test_init_slack_client(self, mock):
        """
        Test __init__ method SlackClient call.
        """
        proxies = {'http': {'vpprx': 0000}, 'https': {'vpprx': 0000}}
        token = 'TestToken'
        SlackHandler(token, '#channel', proxies)
        mock.assert_called_with(token, proxies=proxies)

    def test_get_attachments(self):
        """
        Test _get_attachments method.
        """
        attachments = self.handler._get_attachments(self._record)
        expected_res = [{
            'text': self.handler.format(self._record),
            'color': self.handler.color.get(self._record.levelname, self.handler.color['OTHER'])
        }]
        self.assertEqual(attachments, expected_res)

    @mock.patch('dataf.logging_handlers.SlackClient.api_call')
    def test_send_message(self, mock):
        """
        Test _send_message method remove exc_info and exc_text from record
        and call api_call method from SlackClient.
        """
        record = self._record
        record.exc_info = 'exc_info'
        record.exc_text = 'exc_text'
        self.handler._send_message(record)
        mock.assert_called_with(
            'chat.postMessage', channel='#channel',
            attachments=self.handler._get_attachments(record)
        )
        self.assertIsNone(record.exc_info)
        self.assertIsNone(record.exc_text)

    @mock.patch('dataf.logging_handlers.io.StringIO', return_value='data')
    @mock.patch('builtins.open', new_callable=mock.mock_open, read_data='data')
    @mock.patch('dataf.logging_handlers.SlackClient.api_call')
    def test_send_file(self, mock, mock_f, mock_io):
        """
        Test _send_file method.
        """
        file = '/file/path'
        record = self._record
        self.handler._send_file(record, file)
        mock_f.assert_called_with(file, 'r')
        mock_io.assert_called_with('data')
        mock.assert_called_with(
            'files.upload',
            channels='#channel',
            initial_comment=self.handler.format(record),
            filename=file.split('/')[-1:],
            file='data',
        )

    @mock.patch('dataf.logging_handlers.SlackHandler._send_file')
    def test_emit_with_file(self, mock):
        """
        Test emit method with fiel.
        """
        file = '/file/path'
        record = self._record
        record.args = [file]
        self.handler.emit(record)
        mock.assert_called_with(record, file)
        self.assertIsNone(record.args)

    @mock.patch('dataf.logging_handlers.SlackHandler._send_message')
    def test_emit_without_file(self, mock):
        """
        Test emit method without file.
        """
        record = self._record
        self.handler.emit(record)
        mock.assert_called_with(record)
