# -*- coding: utf-8 -*-
# ===============================================================
#  @author: huangchi@zhiyitech.cn
#  @date: 2018/8/31 上午9:24
#  @brief: 报表
# ===============================================================

import logging
from pandas import DataFrame
from datetime import date, timedelta

from ..common import util, constants
from ..core.mail import Mail
from ..core.task_dao import TaskDao

email_address = constants.EmailAddress

test = constants.TEST


class Report:
    def __init__(self, redis_config, mysql_config, mail_config):
        self.dao = TaskDao(redis_config, mysql_config)
        self.redis_client = self.dao.redis_client
        self.mail = Mail(mail_config)
        self.yesterday, self.two_days_ago = None, None
        self.keys = self.match_keys()

    def match_keys(self):
        """获取指定的keys"""
        # 获取前两天的日期
        today = date.today()
        yesterday = today + timedelta(days=-1)
        two_days_ago = today + timedelta(days=-2)
        self.yesterday = yesterday.strftime(constants.DATE_FMT)
        self.two_days_ago = two_days_ago.strftime(constants.DATE_FMT)
        # 匹配key
        keys = self.redis_client.keys(f'*{self.yesterday}*')
        keys.extend(self.redis_client.keys(f'*{self.two_days_ago}*'))
        return keys

    def report(self):
        """发送报表"""
        # 存储监控信息
        for key in self.keys:
            try:
                self.dao.store_monitor_info(key.decode())
            except Exception as e:
                logging.exception(e)
        # 获取昨日的所有任务
        tasks = self.dao.get_tasks(self.yesterday)
        if len(tasks) == 0:
            return
        # 获取昨日任务维度下的整体统计信息
        task_statistic = self.dao.sum_by_task(self.yesterday)
        df = DataFrame(task_statistic)
        df = df[['bis_name', 'task_name', 'queue_length', 'left', 'success', 'failed', 'retry']]
        html = util.df_to_html('整体统计信息', df)
        # 获取昨日各任务的统计信息
        for task in tasks:
            bis_name = task['bis_name']
            task_name = task['task_name']
            task_statistic = self.dao.get_task_versions(bis_name, task_name, self.yesterday)
            df = DataFrame(task_statistic)
            df = df[['queue_length', 'left', 'success', 'failed', 'retry', 'avg_crawl_time', 'version']]
            html += util.df_to_html(f'业务: {bis_name} 任务: {task_name} 统计信息', df)
        # 发送报表
        if test:
            self.mail.send('爬虫每日统计报表', html, addresses=[email_address.HUANGCHI])
        else:
            self.mail.send('爬虫每日统计报表', html)
