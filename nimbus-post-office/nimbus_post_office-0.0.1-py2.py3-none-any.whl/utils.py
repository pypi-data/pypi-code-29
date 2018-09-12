# -*- coding:utf-8 -*-
import logging
from django.template import Context, Template
from post_office import mail
from post_office.utils import get_email_template
from post_office.mail import send, send_queued

from exchangelib import (
    DELEGATE,
    Account,
    Message,
    Mailbox,
    Configuration,
    Credentials,
    HTMLBody,
    Body,
)

__all__ = [
    "send_exchange_mail",
    "send_exchange_template_mail",
    "send",
    "send_queued",
    "send_mail",
    "send_mail_template",
    "send_mail_message",
    "send_mail_queued",
]

logger = logging.getLogger(__name__)


def send_exchange_mail(recipients, subject, message=None, html_message=None, sender=None, username="", password="", host="", smtp_addr=""):
    """
    用exchangelib发送exchange邮件
    :param recipients:
    :param subject:
    :param message:
    :param html_message:
    :param sender:
    :param username:
    :param password:
    :param host:
    :param smtp_addr:
    :return:
    """
    credentials = Credentials(
        username=username,
        password=password
    )
    config = Configuration(server=host, credentials=credentials)
    account = Account(primary_smtp_address=smtp_addr,
                      credentials=credentials,
                      config=config,
                      autodiscover=False,
                      access_type=DELEGATE
                      )
    to_recipients = [Mailbox(email_address=recipient) for recipient in recipients]
    body = HTMLBody(html_message) if html_message else Body(message)
    m = Message(
        account=account,
        subject=subject,
        body=body,
        to_recipients=to_recipients,
    )
    re = m.send(save_copy=False)
    return re


def send_exchange_template_mail(recipients, template, context, language="en", sender=None, username="", password="", host="", smtp_addr=""):
    """
    用exchangelib发送post_office中的模板邮件
    :param recipients:
    :param template:
    :param context:
    :param language:
    :param sender:
    :param username:
    :param password:
    :param host:
    :param smtp_addr:
    :return:
    """
    if not context:
        logger.error("send_exchange_template_mail context empty")
        return False

    template_context = Context(context)
    email_template = get_email_template(template, language)
    subject = Template(email_template.subject).render(template_context)
    html_message = Template(email_template.html_content).render(template_context)
    return send_exchange_mail(recipients, subject, None, html_message, sender, username, password, host, smtp_addr)


def send_mail(recipients=None, sender=None, template=None, context=None, subject='',
              message='', html_message='', scheduled_time=None, headers=None,
              priority=None, attachments=None, render_on_delivery=False,
              log_level=None, commit=True, cc=None, bcc=None, language='',
              backend=''):
    """
    封装 post_office 发送邮件的方法
    mail.send()
    :param recipients:
    :param sender:
    :param template:
    :param context:
    :param subject:
    :param message:
    :param html_message:
    :param scheduled_time:
    :param headers:
    :param priority:
    :param attachments:
    :param render_on_delivery:
    :param log_level:
    :param commit:
    :param cc:
    :param bcc:
    :param language:
    :param backend:
    :return:
    """
    re = mail.send(
        recipients=recipients,
        sender=sender,
        template=template,
        context=context,
        subject=subject,
        message=message,
        html_message=html_message,
        scheduled_time=scheduled_time,
        headers=headers,
        priority=priority,
        attachments=attachments,
        render_on_delivery=render_on_delivery,
        log_level=log_level,
        commit=commit,
        cc=cc,
        bcc=bcc,
        language=language,
        backend=backend,
    )
    return re


def send_mail_template(recipients=None, sender=None, template=None, context=None,
                       scheduled_time=None, headers=None,
                       priority=None, attachments=None, render_on_delivery=False,
                       log_level=None, commit=True, cc=None, bcc=None, language='',
                       backend=''):
    """
    发送模版消息
    :param recipients:
    :param sender:
    :param template:
    :param context:
    :param scheduled_time:
    :param headers:
    :param priority:
    :param attachments:
    :param render_on_delivery:
    :param log_level:
    :param commit:
    :param cc:
    :param bcc:
    :param language:
    :param backend:
    :return:
    """
    return send_mail(recipients=recipients,
                     sender=sender,
                     template=template,
                     context=context,
                     scheduled_time=scheduled_time,
                     headers=headers,
                     priority=priority,
                     attachments=attachments,
                     render_on_delivery=render_on_delivery,
                     log_level=log_level,
                     commit=commit,
                     cc=cc,
                     bcc=bcc,
                     language=language,
                     backend=backend,
                     )


def send_mail_message(recipients=None, sender=None, subject='', message='', html_message='',
                      scheduled_time=None, headers=None,
                      priority=None, attachments=None, render_on_delivery=False,
                      log_level=None, commit=True, cc=None, bcc=None, language='',
                      backend=''):
    """
    发送普通消息
    :param recipients:
    :param sender:
    :param subject:
    :param message:
    :param html_message:
    :param scheduled_time:
    :param headers:
    :param priority:
    :param attachments:
    :param render_on_delivery:
    :param log_level:
    :param commit:
    :param cc:
    :param bcc:
    :param language:
    :param backend:
    :return:
    """
    return send_mail(recipients=recipients,
                     sender=sender,
                     subject=subject,
                     message=message,
                     html_message=html_message,
                     scheduled_time=scheduled_time,
                     headers=headers,
                     priority=priority,
                     attachments=attachments,
                     render_on_delivery=render_on_delivery,
                     log_level=log_level,
                     commit=commit,
                     cc=cc,
                     bcc=bcc,
                     language=language,
                     backend=backend,
                     )


def send_mail_queued(processes=1, log_level=None):
    """
    封装 post_office 发送待发送状态(queued)邮件的方法
    mail.send_queued()
    :param processes:
    :param log_level:
    :return:
    """
    re = mail.send_queued(processes, log_level)
    return re

