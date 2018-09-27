# -*- coding: utf-8 -*-
# ===============================================================
#  @author: huangchi@zhiyitech.cn
#  @date: 2018/9/11 上午8:34
#  @brief: 
# ===============================================================

import csv
import json
import redis
import hashlib
from functools import wraps
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def task_detect(task, task_config):
    """
    监控任务的检测，对任务是否已完成，任务完成质量的检测
    :param task: 任务信息
    :param task_config: 任务的配置信息
    :return: content，报警信息，若检测通过返回空字符串
    """
    content = ''
    # 任务是否完成的检测
    queue_length = int(task[b'queue_length'])
    left = int(task[b'left'])
    if left < 0:
        # 数据异常
        content += f'Abnormal data:: left: {left}<br />'
    else:
        if left > 0:
            content += f'任务未完成:: {left} left<br />'
        # 失败率检测
        if task_config.get(b'failure_rate_up') and task.get(b'failed'):
            failure_rate = float(task[b'failed']) / (queue_length - left)
            failure_rate_up = float(task_config[b'failure_rate_up'])
            if failure_rate > failure_rate_up:
                content += f'失败率超标:: {round(failure_rate, 2)} > {failure_rate_up}<br />'
        # 爬取时长检测
        if task_config.get(b'avg_time_up') and task.get(b'crawl_time'):
            avg_time = float(task[b'crawl_time']) / (queue_length - left)
            avg_time_up = float(task_config[b'avg_time_up'])
            if avg_time > avg_time_up:
                content += f'爬取时长超标:: {round(avg_time, 2)} > {avg_time_up}'
    return content


def get_avg_crawl_time(value):
    """获取任务监控的平均爬取时间"""
    crawl_time = value.get('crawl_time')
    if not crawl_time:
        return value
    crawl_time = float(crawl_time)
    value.pop('crawl_time')
    # 总爬取次数
    total_crawl_num = int(value.get('success', 0)) + int(value.get('failed', 0)) + int(value.get('retry', 0))
    if total_crawl_num == 0:
        return value
    value['avg_crawl_time'] = crawl_time / total_crawl_num
    return value


def get_dict_hash(data):
    """将字典进行hash"""
    data = json.dumps(data).encode()
    md5_code = hashlib.md5(data).hexdigest()
    return md5_code


def get_redis_conn(redis_config):
    """获取redis连接池"""
    return redis.Redis(connection_pool=redis.ConnectionPool(**redis_config))


def get_mysql_conn(mysql_config, sql_engine_config):
    """获取mysql连接池"""
    uri = 'mysql+pymysql://{user}:{passwd}@{host}:{port}/{db}?charset={charset}'.format(**mysql_config)
    engine = create_engine(uri, **sql_engine_config)
    session = sessionmaker(bind=engine)
    return session


def get_session_fmt(keys):
    """将keys转化为sqlalchemy的session对象可读的预定义格式化字符串"""
    return ','.join(f'`{key}`=:{key}' for key in keys)


def export_as_csv(filename, *data):
    """以csv导出文件"""
    if len(data) == 0:
        return
    writer = csv.DictWriter(open(filename, 'a+'), fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)


def sql_engine():
    """调用sqlalchemy连接进行mysql交互的装饰器"""
    def decorator(func):
        @wraps(func)
        def wrapper(cls, *args, **kwargs):
            """
            :param cls: 当前类型的实例
            :param args:
            :param kwargs:
            :return:
            """
            # 开启会话
            session = cls.mysql_client()
            try:
                result = func(cls, *args, session=session, **kwargs)
                # 提交事务
                session.commit()
                return result
            except Exception as e:
                # 异常事务回滚
                session.rollback()
                raise e
            finally:
                # 关闭会话，收回连接
                session.close()
        return wrapper
    return decorator


def df_to_html(caption, df):
    """DataFrame 对象转化为 table"""
    caption = '<caption>{}</caption>'.format(caption)
    html = ['<table border=1 style="font-family:Arial">\n', caption, '<tr>']
    for column in df.columns:
        html.append('<th>' + column + '</th>')
    html.append('</tr>\n')
    for row in df.values:
        tr = ['<tr>']
        for col in row:
            tr.append('<td>' + str(col) + '</td>')
        tr.append('</tr>\n')
        html.append(''.join(tr))
    html.append('</table>\n')
    return ''.join(html)
