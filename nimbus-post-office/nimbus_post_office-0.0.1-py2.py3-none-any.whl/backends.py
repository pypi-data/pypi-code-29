# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
import os
import sys
import json
import smtplib
import ssl
import threading
import logging
from django.conf import settings
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.mail.backends.base import BaseEmailBackend
from post_office.compat import string_types

from exchangelib import (
    DELEGATE,
    Account,
    Message,
    Mailbox,
    Configuration,
    Credentials,
    HTMLBody,
    Body,
    FileAttachment,
    ItemAttachment,
)

__all__ = [
    "create_attachments",
    "ExchangeEmailBackend",
]


logger = logging.getLogger(__name__)


def get_setting(key, default=None):
    return getattr(settings, key, default)


def create_attachments(attachment_files):
    attachments = []
    for filename, content in attachment_files.items():
        attachment = FileAttachment(name=filename, content=content)
        attachments.append(attachment)
    return attachments


class ExchangeEmailBackend(BaseEmailBackend):
    """

    EMAIL_HOST="xxx.xxx.com"
    EMAIL_PORT=None
    EMAIL_HOST_USER="domain\\username"
    EMAIL_HOST_PASSWORD="password"
    EMAIL_EX_SMTP_ADDRESS="email@xxx.com"
    EMAIL_EX_SERVICE_ENDPOINT=None
    EMAIL_EX_AUTH_TYPE=None
    EMAIL_EX_VERSION=None
    EMAIL_EX_FULLNAME=None
    EMAIL_EX_AUTODISCOVER=False

    EMAIL_USE_SSL=True
    EMAIL_USE_TLS=False
    EMAIL_TIMEOUT=30
    """

    def __init__(self, host=None, port=None, username=None, password=None,
                 smtp_address=None, service_endpoint=None, auth_type=None, version=None,
                 fullname=None, autodiscover=False,
                 fail_silently=False, use_tls=None, use_ssl=None, timeout=None,
                 **kwargs):
        super(ExchangeEmailBackend, self).__init__(fail_silently=fail_silently, **kwargs)
        self.host = host or settings.EMAIL_HOST
        self.port = port or settings.EMAIL_PORT
        self.username = settings.EMAIL_HOST_USER if username is None else username
        self.password = settings.EMAIL_HOST_PASSWORD if password is None else password
        self.smtp_address = settings.EMAIL_EX_SMTP_ADDRESS if smtp_address is None else smtp_address
        self.service_endpoint = settings.EMAIL_EX_SERVICE_ENDPOINT if service_endpoint is None else service_endpoint
        self.auth_type = settings.EMAIL_EX_AUTH_TYPE if auth_type is None else auth_type
        self.version = settings.EMAIL_EX_VERSION if version is None else version
        self.fullname = settings.EMAIL_EX_FULLNAME if fullname is None else fullname

        self.autodiscover = settings.EMAIL_EX_AUTODISCOVER if autodiscover is None else autodiscover

        self.use_tls = settings.EMAIL_USE_TLS if use_tls is None else use_tls
        self.use_ssl = settings.EMAIL_USE_SSL if use_ssl is None else use_ssl
        self.timeout = settings.EMAIL_TIMEOUT if timeout is None else timeout
        self.connection = None
        self._lock = threading.RLock()

    def open(self):
        if self.connection:
            # Nothing to do if the connection is already open.
            return True
        try:
            credentials = Credentials(username=self.username, password=self.password)
            config = Configuration(credentials=credentials,
                                   server=self.host,
                                   has_ssl=self.use_ssl,
                                   service_endpoint=self.service_endpoint,
                                   auth_type=self.auth_type,
                                   version=self.version,
                                   )
            self.connection = Account(
                primary_smtp_address=self.smtp_address,
                fullname=self.fullname,
                access_type=DELEGATE,
                autodiscover=self.autodiscover,
                credentials=credentials,
                config=config,
            )
            return True
        except smtplib.SMTPException:
            if not self.fail_silently:
                raise

    def close(self):
        # if self.connection is None:
        #     return
        # self.connection = None
        pass

    def send_messages(self, email_messages):
        if not email_messages:
            return
        with self._lock:
            new_conn_created = self.open()
            if not self.connection:
                # We failed silently on open().
                # Trying to send would be pointless.
                return
            num_sent = 0
            for message in email_messages:
                sent = self._send(message)
                if sent:
                    num_sent += 1
            if new_conn_created:
                self.close()
        return num_sent

    def _send(self, email_message):
        """A helper method that does the actual sending."""
        subject = email_message.subject
        from_email = email_message.from_email
        message = email_message.body
        headers = email_message.extra_headers

        # Check whether email has 'text/html' alternative
        alternatives = getattr(email_message, 'alternatives', ())
        for alternative in alternatives:
            if alternative[1].startswith('text/html'):
                html_message = alternative[0]
                break
        else:
            html_message = ''

        body = HTMLBody(html_message) if html_message else Body(message)
        # text_body = Body(message)
        sender = Mailbox(email_address=from_email)
        to_recipients = [Mailbox(email_address=to) for to in email_message.to]
        cc_recipients = [Mailbox(email_address=to) for to in email_message.cc]
        bcc_recipients = [Mailbox(email_address=to) for to in email_message.bcc]
        attachment_files = dict([(name, content) for name, content, _ in email_message.attachments])
        attachments = create_attachments(attachment_files)
        reply_to = None
        message = Message(
            account=self.connection,
            # folder=self.account.sent,
            # headers=headers,
            subject=subject,
            # text_body=text_body,
            body=body,
            # sender=sender,
            to_recipients=to_recipients,
            cc_recipients=cc_recipients,
            bcc_recipients=bcc_recipients,
            # reply_to=reply_to,
        )
        if attachments:
            message.attach(attachments)
        re = message.send(save_copy=False)
        return re



