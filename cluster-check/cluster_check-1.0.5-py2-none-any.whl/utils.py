#!/usr/bin/python
# -*- coding: utf-8 -*-
"""工具包"""
import psutil
import subprocess
from subprocess import PIPE, check_output
from datetime import datetime, timedelta


class SubProcess(object):
    """执行命令类"""

    def __init__(self, cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True):
        self.cmd = cmd
        self.process = subprocess.Popen(self.cmd,
                                        stdin=stdin,
                                        stdout=stdout,
                                        stderr=stderr,
                                        shell=shell
                                        )

    def readlines(self):
        lines = self.process.stdout.readlines()
        self.process.stdout.close()
        return lines

    def read(self):
        line = self.process.stdout.read()
        self.process.stdout.close()
        return line


class ProcessInfo(object):
    """进程相关信息"""

    def __init__(self, **kwargs):
        self.pid = kwargs.get("pid", None)
        self.pname = kwargs.get("pname", None)
        self._proc = None
        self._get_proc()

    def _get_proc(self):
        """优先通过ID获取进程，其次通过名称"""
        if self.pid:
            try:
                self._proc = psutil.Process(self.pid)
            except Exception, e:
                print e.message
        else:
            if self.pname:
                for proc in psutil.process_iter():
                    try:
                        if proc.name().lower() == self.pname.lower():
                            self._proc = proc
                            self.pid = self._proc.pid
                    except Exception, e:
                        print e.message

    def memory(self):
        if self._proc:
            rss, vss = self._proc.memory_info()
            return rss
        else:
            return None

    def memory_percent(self):
        if self._proc:
            return self._proc.memory_percent()
        else:
            return None

    def status(self):
        if self._proc:
            return self._proc.status()
        else:
            return None


class SystemInfo(object):
    memory = psutil.virtual_memory()

    def memory_available(self):
        available = SystemInfo.memory.available / 1024.0 ** 3
        return float("%.2f" % available)

    def memory_percent(self):
        mem = psutil.virtual_memory()
        return float("%.2f" % mem.percent)

    def disk_percent(self, part_name):
        disk = psutil.disk_usage(part_name)
        return float("%.2f" % disk.percent)

    def get_serial_num(self):
        """获取序列号"""
        try:
            cmd = "dmidecode -t 1 | grep Serial | xargs echo | tr -d '\n'"
            sub = SubProcess(cmd)
            line = sub.read()
            return line.split(':')[1].strip()
        except Exception, e:
            # print 'Get serial number error!!!'
            return None


def get_before_day(n):
    """获取前几天的日期"""
    return datetime.now() - timedelta(days=n)


system_info = SystemInfo()

if __name__ == '__main__':
    # sub = SubProcess("ls")
    # print sub.readlines()
    # process = ProcessInfo(pname='pycharm')
    # print process.memory()
    # print process.status()
    # print process.pid
    # print process.pname
    # print process.memory_percent()
    system_info = SystemInfo()
    print system_info.memory_available()
