# -*- coding: utf-8 -*-
# ===============================================================
#  @author: huangchi@zhiyitech.cn
#  @date: 2018/9/11 上午8:24
#  @brief: 
# ===============================================================

import json
import logging

from ..common import util, config

# 已初始化的redis连接池
redis_clients = dict()
# 已初始化的mysql连接池
mysql_clients = dict()


class RedisPosition:
    HEAD = 'head'
    TAIL = 'tail'


class Dao:
    """
    持久层基类
    包含 python - mysql，python - redis 的交互
    """
    def __init__(self, redis_config=None, mysql_config=None, redis_key=None):
        self.redis_key = redis_key
        self.redis_client = self._init_redis_client_(redis_config)
        self.mysql_client = self._init_mysql_client_(mysql_config)

    @staticmethod
    def _singleton_(_class, cls):
        """
        构造单例
        当需要将类型设置为单例模式时，重写当前类型的__new__方法
        并调用<code>Dao._singleton_(_class, cls)</code>, 获取返回值即可
        :param _class: 类的类型
        :param cls: 类的实例
        :return:
        """
        if not cls._instance:
            _class._instance = object.__new__(cls)
        return cls._instance

    @staticmethod
    def _init_redis_client_(redis_config):
        """获取redis连接池"""
        if not redis_config:
            return
        # 判断是否已初始化过该连接
        config_md5_code = util.get_dict_hash(redis_config)
        redis_client = redis_clients.get(config_md5_code)
        # 初始化redis连接
        if not redis_client:
            redis_client = util.get_redis_conn(redis_config)
            redis_clients.setdefault(config_md5_code, redis_client)
        return redis_client

    @staticmethod
    def _init_mysql_client_(mysql_config):
        """获取mysql连接池"""
        if not mysql_config:
            return
        # 判断是否已初始化过该连接
        config_md5_code = util.get_dict_hash(mysql_config)
        mysql_client = mysql_clients.get(config_md5_code)
        # 初始化mysql连接
        if not mysql_client:
            mysql_client = util.get_mysql_conn(mysql_config, config.sql_engine_config)
            mysql_clients.setdefault(config_md5_code, mysql_client)
        return mysql_client

    @util.sql_engine()
    def store(self, sql, tb_name, *data, session):
        """
        mysql数据存储
        :param sql: 预定义sql语句，一般为 lib.constants.Sql 中定义的sql语句
        :param tb_name: 数据表名
        :param data: 待存储的数据列表，元素类型为dict
        :param session: 数据库连接，由装饰器生成
        :return: 受影响的行数
        """
        logging.debug('store mysql start...')
        if len(data) == 0:
            return len(data)
        # 获取列
        columns = ','.join([f'`{key}`' for key in data[0].keys()])
        # 占位符
        fmt = ','.join([':' + key for key in data[0].keys()])
        # 格式化sql
        sql = sql.format(tb=tb_name, columns=columns, fmt=fmt)
        # 存储
        cursor = session.execute(sql, data)
        logging.debug('store mysql end...')
        return cursor.rowcount

    @util.sql_engine()
    def get(self, sql, session):
        """从mysql中获取数据，获取到的数据类型为dict"""
        logging.debug('query mysql start...')
        cursor = session.execute(sql)
        values = cursor.fetchall()
        values = [dict(value) for value in values]
        logging.debug(f'query mysql end, get {len(values)} records.')
        return values

    def get_seed(self, position=RedisPosition.HEAD):
        """
        从redis中获取一个种子
        若队列中无元素，则会无限期阻塞至拿到元素为止
        :param position:    拿取种子的位置，分两种
                            head（头）与 tail（尾）
                            'head' 移出并获取列表的第一个元素
                            'tail' 移除并获取列表最后一个元素
        :return: redis key中的一个元素，并进行 json.loads() 操作
        """
        seed = None
        if position == RedisPosition.HEAD:
            redis_key, seed = self.redis_client.blpop(self.redis_key)
        elif position == RedisPosition.TAIL:
            redis_key, seed = self.redis_client.brpop(self.redis_key)
        if seed:
            seed = json.loads(seed)
        return seed

    def push_seed(self, *seeds, position=RedisPosition.TAIL):
        """
        将种子放入队列中
        seeds 中的元素类型需为 str，若为其它类型（如dict）
        则在取出种子后 json.loads(seed) 时会出错
        :param seeds: 待存入的种子列表
        :param position: 插入位置，默认队尾（right push）
        :return: None
        """
        if len(seeds) == 0:
            return
        if position == RedisPosition.HEAD:
            self.redis_client.lpush(self.redis_key, *seeds)
        elif position == RedisPosition.TAIL:
            self.redis_client.rpush(self.redis_key, *seeds)

    def push_seed_from_mysql(self, sql):
        """从mysql中获取数据存入redis中"""
        data = self.get(sql)
        length = len(data)
        if length == 0:
            return
        data = [json.dumps(value) for value in data]
        self.push_seed(*data)
        return length
