#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
极道存储巡检
"""
import os
import re
import socket
from disk import get_disk_info, DISK_INFO
import metadata
from utils import SubProcess, \
    ProcessInfo, \
    get_before_day, system_info

# 主机名称
HOSTNAME = socket.gethostname()


def check_zpool_status(cmd):
    """查看坏盘"""
    content = ["CHECK ZPOOL STATUS"]
    error_disks, total = get_disk_info(cmd)
    if total['pool_count'] == 0 or total['disk_count'] == 0:
        content.append("Match pool or disk error, Please view your disk status manually!!!")
        return

    if error_disks:
        serial_no = system_info.get_serial_num()
        if serial_no:
            content.append("Serial No: {}".format(serial_no))
        else:
            content.append("Get serial number error!!!")

        for d in error_disks:
            values = [d[key] for key in DISK_INFO]
            content.append("{:10s}{:10s}{:10s} {:s}  {:10s}{:3s}{:3s}{:3s}".format(*values))

    __print_output(content)


def check_zpool_iostat(cmd):
    """查看存储池读写负载"""
    # cmd = "zpool iostat 1 3 | grep '_pool'"
    content = ["CHECK ZPOOL IOSTAT"]
    sub = SubProcess(cmd)
    for line in sub.readlines():
        line = line.strip('\n')
        line_list = line.split(' ')
        line_list = [x for x in line_list if x]
        if len(line_list) != 7:
            content.append("check error!!!")
            content.append("After separate line, the element count is not 7.")
            break

        bandwidth_read, bandwidth_write = line_list[5:]
        match_read = re.match(r"([0-9,.]+)M", bandwidth_read)
        match_write = re.match(r"([0-9,.]+)M", bandwidth_write)

        if match_read:
            read_value = match_read.groups()[0]
            if float(read_value) > 300:
                content.append(line)
                continue

        if match_write:
            write_value = match_write.groups()[0]
            if float(write_value) > 500:
                content.append(line)
    __print_output(content)


def check_core_dump(path, before_day=3):
    """查看是否存在core dump错误"""
    content = ["CHECK COREDUMP"]
    if not os.path.exists(path):
        print "Directory %s not exists!!!" % path
    else:
        cmd = "find {path} -mtime -{before_day} -ls | grep -v '{path}'".format(
            path=path,
            before_day=before_day
        )
        sub = SubProcess(cmd)
        for line in sub.readlines():
            content.append(line.strip('\n'))
    __print_output(content)


def check_gluster_status(pname):
    """查看glusterfs进程"""
    content = ["GLUSTER STATUS"]
    process = ProcessInfo(pname=pname)
    if not process.pid:
        content.append("Process '{}' not exists!!!".format(pname))

    if process.status() in ["zombie", "dead"]:
        content.append("Process '{}' is dead or zombie!!!".format(pname))

    percent = process.memory_percent()
    if percent and percent > 60:
        content.append("Process '{}' memory usage percentage: {:.1f}%".format(pname, percent))
    __print_output(content)


def check_nfs_log(log_files, line_num=1000, before_day=3):
    """查看nfs日志"""

    def search_file():
        """执行搜索文件任务"""
        for date in date_list:
            new_cmd = "tail -n {num} {file} | grep '{date}' | {cmd} | tail -n 5".format(
                num=line_num,
                file=file,
                date=date,
                cmd=cmd
            )
            sub = SubProcess(new_cmd)
            for line in sub.readlines():
                content.append(line.strip('\n'))
        __print_output(content)

    # 生成日期
    date_list = [get_before_day(i).strftime("%Y-%m-%d") for i in range(before_day)]
    date_list.reverse()

    for file in log_files:
        if not os.path.exists(file):
            print "Log file {} not exists!!!".format(file)
            continue

        content = ["CHECK NFS LOG <DISCONN>"]
        cmd = "grep DISCONN | grep -v nfs-server"
        search_file()

        content = ["CHECK NFS LOG <disconnected from|Connected to>"]
        cmd = "grep -E 'disconnected from|Connected to' | grep -v nfs-server"
        search_file()

        content = ["CHECK NFS LOG <call_bail>"]
        cmd = "grep call_bail"
        search_file()

        content = ["CHECK NFS LOG <' C ' | ' E '>"]
        cmd = "grep -E ' C | E ' | " \
              "grep -v -E 'Stale file handle|" \
              "rpc actor failed to complete successfully|" \
              "No such file or directory|" \
              "Permission denied|" \
              "Disk quota exceeded|" \
              "dict is invalid|" \
              "remote operation failed'"
        search_file()


def check_system_memory():
    """查看系统内存使用百分比"""
    content = ["SYSTEM FREE MEMORY"]
    if system_info.memory_available() < 1:
        cmd = "free -h"
        sub = SubProcess(cmd)
        content.append(sub.read())
    __print_output(content)


def check_pool_usage():
    """查看存储池使用百分比"""
    content = ["STORAGE POOL USAGE"]
    cmd = "df -h | grep 'pool' | awk '{print $6}'"
    sub = SubProcess(cmd)
    for pool_name in sub.readlines():
        pool_name = pool_name.strip('\n')
        if system_info.disk_percent(pool_name) > 95:
            sub = SubProcess("df -h | grep {}".format(pool_name))
            content.append(sub.read().strip('\n'))
    __print_output(content)


def check_metadata_usage():
    """查看存储元盘使用情况"""
    content = ["STORAGE POOL METADATA USAGE"]
    data = metadata.main()
    for d in data:
        line = "%s %s  metadata_size: %s  metadata_used: %s  percentage: %s%%" % d
        try:
            metadata.write_to_log(line)
            if float(d[4]) > 90:
                content.append(line)
        except metadata.SaveLogError, e:
            content.append("Save metadata log error!!!")
        except Exception, e:
            content.append("Get metadata usage error!!!")
    __print_output(content)


def __print_output(contents):
    """打印输出内容"""
    if len(contents) < 2:
        return
    title = "{} {}".format(HOSTNAME, contents[0])
    print title.center(80, '=')
    for line in contents[1:]:
        print line


def main():
    check_pool_usage()
    check_metadata_usage()
    check_zpool_status("zpool status")
    check_zpool_iostat("zpool iostat 1 3 | grep '_pool'")
    check_core_dump('/var/crash', 4)
    check_gluster_status('glusterfs')
    check_nfs_log(['/var/log/glusterfs/nfs.log', '/var/log/glusterfs/nfs.log.1'], 20000, 4)
    check_system_memory()


if __name__ == '__main__':
    main()
