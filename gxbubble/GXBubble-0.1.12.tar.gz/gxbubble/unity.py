# -*- coding: utf-8 -*-
#
# This file is part of ProjectBubble.
#
# (c) Giant - MouGuangyi <mouguangyi@ztgame.com>
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#

import os
import _thread
import platform
from gxbubble import (shell, tail)


class Unity:
    __path = ''

    def __init__(self, unity_path):
        self.__path = os.environ.get(unity_path, '')

    def valid(self):
        return os.path.exists(self.__path)

    def run(self, **options):
        if not self.valid():
            raise FileNotFoundError('CANNOT find Unity!')

        parameters = ' '
        log_path = ''
        for k, v in options.items():
            if v in (True, False):
                parameters += (' -' + k) if v else ''
            else:
                parameters += (' -' + k + ' ' + v)
                if k == 'logFile':
                    log_path = v

        # new thread to tail log file
        _thread.start_new_thread(Unity.__tail_thread, (log_path,))

        return shell(self.__path + parameters)

    @staticmethod
    def __tail_thread(tail_file):
        print("wait for tail file ... %s" % tail_file)
        while True:
            if os.path.exists(tail_file):
                print("Start tail file..... %s" % tail_file)
                break

        t = tail.Tail(tail_file)
        t.register_callback(Unity.__unity_log_tail)
        t.follow(s=1)

    @staticmethod
    def __unity_log_tail(txt):
        print(txt)

    @staticmethod
    def __is_windows_system():
        return 'Windows' in platform.system()

    @staticmethod
    def __is_linux_system():
        return "Linux" in platform.system()
