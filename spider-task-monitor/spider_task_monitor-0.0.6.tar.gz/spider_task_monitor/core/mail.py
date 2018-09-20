# -*- coding: utf-8 -*-
# ===============================================================
#  author: hehuihui@zhiyitech.com
#  date: 2018/04/18 14:17
#  brief:
# ===============================================================

import time
import smtplib
import logging
from email.mime.text import MIMEText
from email.utils import formataddr

from ..common import constants

email_addresses = constants.EmailAddress

# 默认的收件人列表
default_addresses = [email_addresses.ZEYU, email_addresses.HUIHUI,
                     email_addresses.XIANGYOU, email_addresses.HUANGCHI]


class Mail:
    def __init__(self, mail_config, nickname='spider', time_interval: int=0):
        """
        :param mail_config: 邮件配置，服务器、端口、用户名及密码
        :param nickname: 发件人昵称
        :param time_interval: 发送时间间隔
        """
        self.mail_config = mail_config
        # 昵称
        self.nickname = nickname
        # 发送时间间隔
        self.time_interval = time_interval
        # 上次发送邮件的时间
        self.last_mail_time = None

    def send(self, subject, content, addresses: list=default_addresses,
             cc_addresses: list=None, subtype='html', charset='utf-8'):
        """
        发送邮件
        :param subject: 邮件标题
        :param content: 邮件内容
        :param addresses: 收件人列表
        :param cc_addresses: 抄送人列表
        :param subtype: 邮件格式（例如：plain/html/json等）
        :param charset: 邮件字符编码
        :return: None
        """
        # 若设置了发送时间间隔
        # 判断距上一封邮件的发送时间是否超过 time_interval
        # 若还在 time_interval 内，不发送邮件
        if self.time_interval:
            if not self.last_mail_time:
                self.last_mail_time = int(time.time())
            elif (time.time() - self.last_mail_time) < self.time_interval:
                left_time = int(time.time() - self.last_mail_time)
                logging.debug(f'mail system not ready, left {left_time} seconds...')
                return
            else:
                self.last_mail_time = int(time.time())
        logging.debug('send mail start...')
        # 构造邮件对象
        mail_config = self.mail_config
        user = mail_config['user']
        msg = MIMEText(content, subtype, charset)
        msg['From'] = formataddr([self.nickname, user])
        if addresses:
            msg['To'] = ','.join(addresses)
        if cc_addresses:
            msg['CC'] = ','.join(cc_addresses)
        msg['Subject'] = subject
        server = smtplib.SMTP_SSL('smtp.exmail.qq.com', 465)
        server.login(user, mail_config['password'])
        server.sendmail(user, addresses, msg.as_string())
        server.quit()
        logging.debug('send mail end...')
