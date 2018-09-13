#!/usr/bin/python
# -*- coding: utf-8 -*-
"""磁盘巡检"""
import re
from collections import OrderedDict
from utils import SubProcess

DISK_INFO = ['pool_name', 'raid_name', 'data_type', 'name', 'state', 'read', 'write', 'cksum']
ERROR_DISKS = []
TOTAL = OrderedDict(pool_count=0, raid_count=0, disk_count=0)

def get_disk_info(cmd):
    """获取磁盘信息"""
    pool_name, raid_name = None, None
    sub = SubProcess(cmd)
    for line in sub.readlines():
        # 匹配pool行:'\tpool3                                     ONLINE       0     0     0\n'
        match_pool = __match_line(line, '^\t[\w]*pool[\w]*\s+[A-Z]+\s+\d+\s+\d+\s+\d+$')
        if match_pool:
            TOTAL['pool_count'] += 1
            pool_name = match_pool['name']
            continue

        # 匹配raid行:'\t  raidz2-0                                ONLINE       0     0     0\n'
        match_raid = __match_line(line, '^\t\s+raid.+\s+[A-Z]+\s+\d+\s+\d+\s+\d+$')
        if match_raid:
            TOTAL['raid_count'] += 1
            raid_name = match_raid['name']
            continue

        data_type = "Data Disk"
        # 匹配metadata行：\t  metadata:mirror-2                                ONLINE       0     0     0\n'
        match_metadata = __match_line(line, '^\t\s+raid.+\s+[A-Z]+\s+\d+\s+\d+\s+\d+$')
        if match_metadata:
            data_type = "Metadata Disk"
            continue

        # 匹配磁盘行:'\t    63301357-8a79-4ce1-953e-dbd857cc1e23  ONLINE       0     0     0\n'
        match_disk = __match_line(line, '^\t\s+[\w-]+\s+[A-Z]+\s+\d+\s+\d+\s+\d+.*$')
        if match_disk:
            TOTAL['disk_count'] += 1
            check_disk(match_disk, pool_name, raid_name, data_type)
    return ERROR_DISKS, TOTAL


def check_disk(disk, pool_name, raid_name, data_type):
    """判断是否坏盘"""
    if disk['state'] != "ONLINE" or \
                    disk['read'] != '0' or \
                    disk['write'] != '0' or \
                    disk['cksum'] != '0':
        disk['pool_name'] = pool_name
        disk['raid_name'] = raid_name
        disk['data_type'] = data_type
        ERROR_DISKS.append(disk)


def __match_line(line, pattern):
    match = re.match(pattern, line)
    res = OrderedDict()
    if match:
        mg = match.group().strip('\t').strip('\n')
        match_list = [e for e in mg.split(' ') if e != '']
        if len(match_list) >= 5:
            for index, key in enumerate(DISK_INFO[3:]):
                res[key] = match_list[index]
    return res
