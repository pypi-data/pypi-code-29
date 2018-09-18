import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import (
    SMTPAuthenticationError,
    SMTPDataError,
    SMTPException,
    SMTPHeloError,
    SMTPNotSupportedError,
    SMTPRecipientsRefused,
    SMTPSenderRefused,
)


class MailpapaException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)


class Response(object):
    def __init__(self, source, emails, ok):
        self.source = source
        self.emails = emails
        self.ok = ok

    def save(self, file=None, format="json"):
        if file is None:
            return False

        if not self.ok:
            return False

        if len(self.emails) == 0:
            return False

        emails = []
        for email in self.emails:
            emails.append(email.dict())

        return json.dumps(emails)


class Email(object):
    def __init__(
        self,
        address: str = None,
        name: str = None,
        personal: bool = True,
        position: str = None,
        **kwargs,
    ):
        self.address = address
        self.name = name
        self.personal = personal

        if self.personal:
            self.position = position

    def __repr__(self):
        return f"<Email [ {self.address} ]>"

    def dict(self):
        return {
            "email_address": self.address,
            "name": self.name,
            "position": self.position,
            "personal": self.personal,
        }

    def json(self):
        return json.dumps(self.dict())

    def sendmail(
        self,
        sender: str = None,
        subject: str = None,
        body: str = None,
        html: bool = False,
        config: dict = None,
    ) -> bool:

        message = MIMEMultipart()
        message["From"] = sender
        message["Subject"] = subject
        message["To"] = self.address

        subtype = "plain" if html is None else "html"

        message.attach(MIMEText(body, subtype))

        host = config.get("host", None)
        if host is None:
            raise MailpapaException("Expected Host Parameter")

        port = config.get("port", 587)

        _pass = config.get("password", None)

        server = smtplib.SMTP_SSL(host, int(port))

        try:
            server.ehlo()
            server.login(sender, _pass)
            server.sendmail(message["From"], message["To"], message.as_string())
        except (
            SMTPAuthenticationError,
            SMTPDataError,
            SMTPException,
            SMTPHeloError,
            SMTPNotSupportedError,
            SMTPNotSupportedError,
            SMTPRecipientsRefused,
            SMTPSenderRefused,
        ) as e:
            raise MailpapaException(str(e))

        server.quit()

        return True
