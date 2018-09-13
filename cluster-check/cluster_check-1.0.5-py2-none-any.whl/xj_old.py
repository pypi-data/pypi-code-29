#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
极道存储巡检
"""
import os
import re
import subprocess
from subprocess import PIPE, check_output
import socket
import psutil
from datetime import datetime
from datetime import timedelta
from collections import OrderedDict
import json

HOSTNAME = socket.gethostname()
DISK_INFO = ['pool_name', 'raid_name', 'name', 'state', 'read', 'write', 'cksum']


def execute_cmd(cmd):
    process = subprocess.Popen(cmd,
                               stdin=PIPE,
                               stdout=PIPE,
                               stderr=PIPE,
                               shell=True
                               )
    return process


# 检测zpool的状态
def zpool_status():
    __print_title("CHECK ZPOOL STATUS")
    cmd = "zpool status |" \
          "grep '-' | " \
          "grep -v -E 'http|raid' | " \
          "awk '{print $1, $2, $3, $4, $5}'"
    obj = execute_cmd(cmd)
    lines = obj.stdout.readlines()
    obj.stdout.close()
    output = ''
    for line in lines:
        line_list = line.rstrip().split(' ')
        if len(line_list) < 5:
            continue
        if line_list[1] != 'ONLINE':
            output += line
            continue
        if line_list[2:].count('0') != 3:
            output += line

    if output:
        get_serial_num()
        print output


def get_serial_num():
    try:
        cmd = "dmidecode -t 1 | grep Serial | xargs echo | tr -d '\n'"
        obj = execute_cmd(cmd)
        output = obj.stdout.read()
        obj.stdout.close()
        if output == '':
            raise
        else:
            print output
    except Exception, e:
        print 'Get serial number error!!!'


def zpool_status_new():
    __print_title("CHECK ZPOOL STATUS")
    cmd = "zpool status"
    obj = execute_cmd(cmd)
    lines = obj.stdout.readlines()
    obj.stdout.close()
    total = OrderedDict(pool_count=0, raid_count=0, disk_count=0)
    error_disks = []
    pool_name, raid_name = None, None
    for line in lines:
        # 匹配pool行:'\tpool3                                     ONLINE       0     0     0\n'
        match_pool = __match_line(line, '^\t[\w]*pool\d+\s+[A-Z]+\s+\d+\s+\d+\s+\d+$')
        # 吉因加是下面这行
        # match_pool = __match_line(line, '^\t[\w]*pool[\w]*\s+[A-Z]+\s+\d+\s+\d+\s+\d+$')
        if match_pool:
            total['pool_count'] += 1
            pool_name = match_pool['name']
            continue

        # 匹配raid行:'\t  raidz2-0                                ONLINE       0     0     0\n'
        match_raid = __match_line(line, '^\t\s+raid.+\s+[A-Z]+\s+\d+\s+\d+\s+\d+$')
        if match_raid:
            total['raid_count'] += 1
            raid_name = match_raid['name']
            continue

        # 匹配磁盘行:'\t    63301357-8a79-4ce1-953e-dbd857cc1e23  ONLINE       0     0     0\n'
        # match_disk = __match_line(line, '^\t\s+[a-z0-9-]+\s+[A-Z]+\s+\d+\s+\d+\s+\d+$')
        match_disk = __match_line(line, '^\t\s+[\w-]+\s+[A-Z]+\s+\d+\s+\d+\s+\d+.*$')
        if match_disk:
            total['disk_count'] += 1
            if match_disk['state'] != 'ONLINE':
                match_disk['pool_name'] = pool_name
                match_disk['raid_name'] = raid_name
                error_disks.append(match_disk)
            elif match_disk['read'] != '0' or match_disk['write'] != '0' or match_disk['cksum'] != '0':
                match_disk['pool_name'] = pool_name
                match_disk['raid_name'] = raid_name
                error_disks.append(match_disk)

    if total['pool_count'] == 0 or total['disk_count'] == 0:
        print "Match pool or disk error, Please view your disk status manually!!!"
        return

    if error_disks:
        get_serial_num()
        for d in error_disks:
            values = [d[key] for key in DISK_INFO]
            print "{:10s}{:10s} {:s}  {:10s}{:3s}{:3s}{:3s}".format(*values)


def __match_line(line, pattern):
    match = re.match(pattern, line)
    res = OrderedDict()
    if match:
        mg = match.group().strip('\t').strip('\n')
        match_list = [e for e in mg.split(' ') if e != '']
        if len(match_list) >= 5:
            for index, key in enumerate(DISK_INFO[2:]):
                res[key] = match_list[index]
    return res


# 检测zpool带宽
def zpool_iostat():
    __print_title("CHECK ZPOOL IOSTAT")
    cmd = "zpool iostat 1 3 | grep '_pool'"
    obj = execute_cmd(cmd)
    lines = obj.stdout.readlines()
    obj.stdout.close()
    for line in lines:
        line_list = line.rstrip().split(' ')
        line_list = [x for x in line_list if x]
        if len(line_list) == 7:
            bandwidth_read, bandwidth_write = line_list[5:]
            if 'M' in bandwidth_read:
                match_read = re.match(r"([0-9,.]+)([a-z]+)",
                                      bandwidth_read,
                                      re.I)
                if match_read:
                    num, dw = match_read.groups()
                    if float(num) > 300:
                        print line

            if 'M' in bandwidth_write:
                match_read = re.match(r"([0-9,.]+)([a-z]+)",
                                      bandwidth_write,
                                      re.I)
                if match_read:
                    num, dw = match_read.groups()
                    if float(num) > 500:
                        print line
        else:
            print "check error!!!"
            print "After separate line, the element count < 7."
            break


# 检测目录是否为空, path为检测路径
def core_dump(path="/tmp/aaa", before_day=7):
    __print_title("CHECK COREDUMP")
    if not os.path.exists(path):
        print "Directory %s not exists!!!" % path
        return True
    if os.listdir(path):
        # print ("%s" % HOSTNAME).ljust(50, "-")
        cmd = 'find %s -mtime -%s -ls' % (path, before_day)
        obj = execute_cmd(cmd)
        output = obj.stdout.read()
        obj.stdout.close()
        if output:
            print output


# 检测进程是否存在且正常运行, pname为进程名称
def gluster_status(pname='vda'):
    __print_title("GLUSTER STATUS")
    cmd = '''ps aux | grep %s | grep -v grep | awk '{print $8}' | sort -u'''
    cmd = cmd % pname
    obj = execute_cmd(cmd)
    lines = obj.stdout.readlines()
    obj.stdout.close()
    oneline = ' '.join(line.rstrip() for line in lines)
    if oneline == '':
        print "%s: Process '%s' not exists!!!" % (HOSTNAME, pname)
    else:
        if 'Z' in oneline or 'X' in oneline:
            print '%s %s' % (HOSTNAME, oneline)


# 获取指定进程的cpu、内存使用百分比
def get_process_memory(pname='vda'):
    __print_title("GET PROCESS %s MEMORY USAGE PERCENTAGE" % pname)
    pids = __get_pid(pname)
    for pid in pids:
        process = psutil.Process(pid)
        mem = process.memory_percent()
        if mem > 60:
            err = "Process %s memory usage percentage: %s, " \
                  "use too much memory!!!"
            print err % (pname, "%0.2f" % mem)


# 获取系统内存
def get_system_memory():
    __print_title("SYSTEM FREE MEMORY")
    mem = psutil.virtual_memory()
    # total = mem.total / 1024.0 ** 3
    # used = int(round(mem.total * mem.percent / 100)) / 1024.0 ** 3
    free = mem.free / 1024.0 ** 3
    if free < 1:
        cmd = 'free -h'
        __get_output(cmd)



def __get_pid(name):
    try:
        return map(int, check_output(["pidof", name]).split())
    except Exception, e:
        print "Get process %s error!!!" % name
        return []


# 检查nfs日志
def check_nfs_log(log_files, line_num=1000):
    for ss in ['DISCONN', 'disconnected from|Connected to']:
        __print_title("CHECK NFS LOG <%s>" % ss)
        cmd = "grep %s | grep -v nfs-server" % ss
        __search_log_file(log_files, line_num, cmd)

    __print_title("CHECK NFS LOG <call_bail>")
    cmd = "grep call_bail"
    __search_log_file(log_files, line_num, cmd)

    __print_title("CHECK NFS LOG <' C ' | ' E '>")
    cmd = "grep -E ' C | E ' | " \
          "grep -v -E 'Stale file handle|" \
          "rpc actor failed to complete successfully|" \
          "No such file or directory|" \
          "Permission denied|Disk quota exceeded'"
    __search_log_file(log_files, line_num, cmd)


# search log file
def __search_log_file(log_files, line_num, cmd):
    def get_before_day(n):
        return datetime.now() - timedelta(days=n)

    date_list = [get_before_day(i).strftime("%Y-%m-%d") for i in range(7)]
    date_str = '|'.join(date_list)
    for log_file in log_files:
        if os.path.exists(log_file):
            __get_output(
                "tail -n %s %s | grep -E '%s' | %s" % (
                    line_num, log_file, date_str, cmd))
        else:
            print "Log file %s not exists!!!" % log_file


# 执行命令,获取结果
def __get_output(cmd):
    obj = execute_cmd(cmd)
    output = obj.stdout.read()
    obj.stdout.close()
    if output:
        print output


def __print_title(content):
    # print ">" * 25 + content + "<" * 25
    content = "%s %s" % (HOSTNAME, content)
    print content.center(80, '=')


def main():
    # zpool_status()
    zpool_status_new()
    zpool_iostat()
    core_dump('/var/crash',3)
    gluster_status('glusterfs')
    get_process_memory('glusterfsd')
    check_nfs_log(['/var/log/glusterfs/nfs.log', '/var/log/glusterfs/nfs.log.1'], 10000)
    get_system_memory()


if __name__ == '__main__':
    main()
    # zpool_status()
    # zpool_status_new()
    # get_system_memory()