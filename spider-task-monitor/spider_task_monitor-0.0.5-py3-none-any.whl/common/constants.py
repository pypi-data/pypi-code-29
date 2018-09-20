# -*- coding: utf-8 -*-
# ===============================================================
#  @author: huangchi@zhiyitech.cn
#  @date: 2018/8/29 上午8:57
#  @brief: 
# ===============================================================

import os

# 是否为测试/开发环境
TEST = int(os.getenv('TEST', 0))
# flag 标识
FLAG = os.getenv('FLAG')
# redis key 分隔符
KEY_DELIMITER = '___'
# 版本号的格式
DATE_FMT = '%Y/%m/%d'
VERSION_FMT = f'{DATE_FMT} %H:%M'
# 存放监控key的db
REDIS_DB = 14


class Sql:
    INSERT = 'insert into `{tb}` ({columns}) values ({fmt}) '
    INSERT_IGNORE = 'insert ignore into `{tb}` ({columns}) values ({fmt}) '


class TBName:
    TASK_MONITOR = 'task_monitor'


class RedisKeyPrefix:
    TASK_MONITOR = '(task_monitor)'


class RedisKey:
    # 不同任务配置信息的键
    TASK_CONFIG = f'{RedisKeyPrefix.TASK_MONITOR}hash_task_config_{{bis_name}}_{{task_name}}'


class EmailAddress:
    """邮箱地址"""
    ZEYU = 'zeyu@zhiyitech.cn'
    HUIHUI = 'huihui@zhiyitech.cn'
    XIANGYOU = 'liheyou@zhiyitech.cn'
    HUANGCHI = 'huangchi@zhiyitech.cn'
