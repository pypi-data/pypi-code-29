# -*- coding: utf-8 -*-
# ===============================================================
#  @author: huangchi@zhiyitech.cn
#  @date: 2018/8/29 下午2:19
#  @brief: 监控
# ===============================================================

import time
import json

from ..common import constants, util
from ..core.mail import Mail

from ..core.task_dao import TaskDao

redis_key_prefixes = constants.RedisKeyPrefix
redis_keys = constants.RedisKey
key_delimiter = constants.KEY_DELIMITER


class DataResult:
    SUCCESS = 'success'
    FAILED = 'failed'
    RETRY = 'retry'


class Monitor:
    def __init__(self, bis_name, task_name, redis_config, mail_config):
        """
        初始化监控
        :param bis_name:        业务名
        :param task_name:       任务名
        :param redis_config:    redis的配置
        :param mail_config:     邮件的配置
        """
        if key_delimiter in bis_name or key_delimiter in task_name:
            raise Exception(f'业务名或任务名中不能包含{key_delimiter}')
        self.bis_name = bis_name
        self.task_name = task_name
        self.dao = TaskDao(redis_config, mysql_config=None)
        self.redis_client = self.dao.redis_client
        self.mail = Mail(mail_config, time_interval=5 * 60)
        self.task_config_key = self.cons_config_key()

    @staticmethod
    def cons_version():
        """构造当前时间的版本号"""
        return time.strftime(constants.VERSION_FMT, time.localtime())

    def cons_config_key(self):
        """构造配置key"""
        return redis_keys.TASK_CONFIG.format(bis_name=self.bis_name, task_name=self.task_name)

    def cons_monitor_key(self, version):
        """构造监控key"""
        # 检查版本号的格式是否正确
        time.strptime(version, constants.VERSION_FMT)
        # 构造监控key
        monitor_key = f'{redis_key_prefixes.TASK_MONITOR}hash{key_delimiter}{self.bis_name}{key_delimiter}' \
                      f'{self.task_name}{key_delimiter}{version}'
        return monitor_key

    def init_config(self, failure_rate_up: float=.0, avg_time_up: float=5.0, warn_addresses: list=None):
        """初始化任务的配置信息"""
        self.redis_client.hset(self.task_config_key, 'failure_rate_up', failure_rate_up)
        self.redis_client.hset(self.task_config_key, 'avg_time_up', avg_time_up)
        if warn_addresses:
            self.redis_client.hset(self.task_config_key, 'warn_addresses', json.dumps(warn_addresses))

    def create(self, version, queue_length: int):
        """初始化监控"""
        monitor_key = self.cons_monitor_key(version)
        if self.redis_client.hgetall(monitor_key):
            return
        # 初始化监控
        self.redis_client.hsetnx(monitor_key, 'bis_name', self.bis_name)
        self.redis_client.hsetnx(monitor_key, 'task_name', self.task_name)
        self.redis_client.hsetnx(monitor_key, 'version', version)
        self.redis_client.hsetnx(monitor_key, 'queue_length', queue_length)
        self.redis_client.hsetnx(monitor_key, 'left', queue_length)
        # 设置过期时间
        self.redis_client.expire(monitor_key, 2 * 24 * 3600)
        # 对上一版本的任务的报警
        self.warning(version)
        # 设置last_version
        self.redis_client.hset(self.task_config_key, 'last_version', version)

    def send(self, version, data: int=1, data_result=DataResult.SUCCESS, crawl_time=None):
        """
        发送监控信息
        :param version:
        :param data: 爬取的种子数，默认1
        :param data_result: 爬取结果，默认 success
        :param crawl_time: 爬取时间，默认None
        :return:
        """
        # 判断监控是否已初始化
        monitor_key = self.cons_monitor_key(version)
        if not self.redis_client.hgetall(monitor_key):
            raise Exception('Please init your monitor first!')
        # 发送监控信息
        self.redis_client.hincrby(monitor_key, data_result, data)
        if data_result == DataResult.SUCCESS or data_result == DataResult.FAILED:
            self.redis_client.hincrby(monitor_key, 'left', -data)
        if crawl_time:
            self.redis_client.hincrbyfloat(monitor_key, 'crawl_time', crawl_time)

    def incr_queue_length(self, version, queue_length: int):
        """更新队列长度"""
        monitor_key = self.cons_monitor_key(version)
        self.redis_client.hincrby(monitor_key, 'queue_length', queue_length)
        self.redis_client.hincrby(monitor_key, 'left', queue_length)

    def warning(self, version):
        """对上一版本的任务的报警"""
        # 获取任务的配置信息
        task_config = self.redis_client.hgetall(self.task_config_key)
        # 未配置任务的配置信息
        if not task_config:
            return
        # 未配置收件人
        if not task_config.get(b'warn_addresses'):
            return
        # 初次爬取
        if not task_config.get(b'last_version'):
            self.redis_client.hset(self.task_config_key, 'last_version', version)
            return
        # 获取上一个版本的任务信息
        last_version = task_config[b'last_version'].decode()
        monitor_key = self.cons_monitor_key(last_version)
        last_task = self.redis_client.hgetall(monitor_key)
        if not last_task:
            return
        content = util.task_detect(last_task, task_config)
        # 无报警信息
        if content == '':
            return
        # 报警
        subject = f'业务：{self.bis_name}, 任务：{self.task_name}, 版本：{last_version} 检测结果'
        warn_addresses = json.loads(task_config[b'warn_addresses'])
        self.mail.send(subject, content, addresses=warn_addresses)
