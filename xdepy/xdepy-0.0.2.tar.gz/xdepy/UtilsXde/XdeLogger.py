# -*- encoding:utf-8 -*-

from __future__ import absolute_import

import os
import time
import datetime
import dateutil


class XdeLogger:
    '''
    日志操作类
    '''

    def __init__(self, dir):
        self.dir = dir

    def writeIn(self, file, data):
        if not os.path.exists(os.path.dirname(file)):
            os.makedirs(os.path.dirname(file))
        with open(file, 'a+', encoding='utf-8') as f:
            f.write(data)

    def write(self, data):
        local_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        local_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        file_path = os.path.join(self.dir, local_date + '.log')
        self.writeIn(file_path, local_time + '\t' + str(data) + '\n')
        print(local_time + '\t' + str(data) + '\n')


if __name__ == '__main__':
    logger = XdeLogger('logs')
    logger.write("test")