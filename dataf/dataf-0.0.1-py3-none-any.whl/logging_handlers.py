#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__doc__ = """

Logging handlers
----------------

Custom handlers for logging.

"""

import logging
import io

from slackclient import SlackClient


class SlackHandler(logging.Handler):
    """
    Handler for slack.
    Use color dict attr for the message attachments.

    .. code-block:: python

        color = {
            'ERROR': '#F00', (RED)
            'OTHER': '#3AA3E3', (BLUE)
            'SLACK': '#00ff2b', (GREEN)
            'WARNING': '#f07900', (YELLOW)
        }

    :param str token: auth token for slack.
    :param str channel: channel name to post message.
    """
    color = {
        'ERROR': '#F00',
        'OTHER': '#3AA3E3',
        'SLACK': '#00ff2b',
        'WARNING': '#f07900',
    }

    def __init__(self, token, channel, proxies=None):
        logging.Handler.__init__(self)
        self.channel = channel
        self.slack = SlackClient(token, proxies=proxies)

    def emit(self, record):
        """
        Send message on slack channel.
        """
        try:
            file = record.args[0]
            record.args = None
            self._send_file(record, file)
        except IndexError:
            self._send_message(record)

    def _get_attachments(self, record):
        """
        Create attachments for slack message.
        """
        attachments = [{
            'text': self.format(record),
            'color': self.color.get(record.levelname, self.color['OTHER'])
        }]
        return attachments

    def _send_file(self, record, file):
        """
        Send file.

        :param obj record: logging record object.
        :param str file: file path.
        """
        with open(file, 'r') as f:
            self.slack.api_call(
                "files.upload",
                channels=self.channel,
                initial_comment=self.format(record),
                filename=file.split('/')[-1:],
                file=io.StringIO(f.read()),
            )

    def _send_message(self, record):
        """
        Send text message.

        :param obj record: logging record object.
        """
        record.exc_info = None
        record.exc_text = None
        self.slack.api_call(
            "chat.postMessage",
            channel=self.channel,
            attachments=self._get_attachments(record)
        )
