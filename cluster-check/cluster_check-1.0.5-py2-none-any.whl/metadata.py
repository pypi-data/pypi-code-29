#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
记录元数据盘的使用情况
获取命令：
    zpool get all |grep metadata
    xt1_pool1  metadata_size               372G                        default
    xt1_pool1  metadata_used               6.51G                       default
    xt1_pool2  metadata_size               372G                        default
    xt1_pool2  metadata_used               6.70G                       default
保存后数据形式：
    data           pool      metadata_size  metadata_used  percentage
  2018-1-1       xt1_pool1      372G           6.51G          1.75%
  2018-1-1       xt1_pool2      372G           6.70G          1.80%
'''
from utils import SubProcess
from datetime import datetime
from collections import OrderedDict
import re

class SaveLogError(Exception):
    pass

def main():
    cmd = "zpool get all | grep metadata | awk '{print $1,$2,$3,$4}'"
    sub = SubProcess(cmd)
    data = OrderedDict()
    for line in sub.readlines():
        d = line.rstrip().split(' ')
        pool_name, metadata_type, value = d[0:3]
        if not data.has_key(pool_name):
            data[pool_name] = {}
        data[pool_name].update({metadata_type: value})

    new_data = __format_data(data)
    return new_data


def write_to_log(line):
    '''将数据写入日志中'''
    meta_log = "/var/log/metadata_used.log"
    try:
        with open(meta_log, 'a') as f:
            f.write('%s\n' % line)
    except Exception, e:
        raise SaveLogError()


def __format_data(data):
    '''格式化数据后输出'''
    new_data = []
    today = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    for pool_name, val in data.items():
        metadata_size_val = __get_metadata_value(val['metadata_size'])
        metadata_used_val = __get_metadata_value(val['metadata_used'])
        if metadata_size_val and metadata_used_val:
            percentage = '%0.2f' % ((metadata_used_val / metadata_size_val) * 100)
            new_data.append((today, pool_name, val['metadata_size'], val['metadata_used'], percentage))
    return new_data


def __get_metadata_value(match_str):
    '''匹配metadata_size和metadata_used等值'''
    match = re.match(r"([0-9,.]+)([a-z]+)",
                     match_str,
                     re.I)
    if match:
        val, dw = match.groups()
        return float(val)
    else:
        return None


if __name__ == '__main__':
    main()
