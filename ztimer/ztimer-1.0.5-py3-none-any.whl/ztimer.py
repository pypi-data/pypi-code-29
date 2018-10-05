# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    ztimer.py
   Author :       Zhang Fan
   date：         18/09/26
   Description :
-------------------------------------------------
"""
__author__ = 'Zhang Fan'

import time
import threading

from zsingleton.singleton_decorator import singleton
from zblocker import BLock_more


class Timer():
    '''
    创建计时器(时间回调,第一次等待时间,循环等待时间
    '''

    def __init__(self, callback, loop_wait_time: int or float, loop_count: None or int = None,
                 close_callback=None, meta=None):
        '''
        初始化计时器
        :param callback: 回调函数
        :param loop_wait_time: 循环等待时间
        :param loop_count: 循环次数, None表示无限循环, 循环次数超出后会自动关闭
        :param meta: 保存一个值, 此值由用户设置, 模块仅仅为用户保存这个值而不会使用或者修改这个值
        '''

        assert hasattr(callback, '__call__'), TypeError("回调函数必须存在__call__属性")
        assert loop_wait_time > 0, '循环等待时间必须大于0'
        assert loop_count is None or loop_count > 0, '循环次数必须设为None或者大于0'
        if not close_callback is None:
            assert hasattr(close_callback, '__call__'), TypeError("销毁回调函数必须存在__call__属性")

        self.callback = callback
        self.loop_wait_time = loop_wait_time
        self.loop_count = loop_count
        self.close_callback = close_callback
        self.meta = meta

        self.__callback_count = 0  # 回调函数的次数
        self.__interval = 0  # 持续时间

        self.__is_run = False
        self.__is_close = True

        self.__join_lock = BLock_more()

    def start(self):
        if self.__is_close:
            self.__is_close = False

            self.__callback_count = 0
            self.__interval = 0

            self.__tm = Timer_Manager()
            self.__tm.add_timer(self)

        self.__is_run = True

    def pause(self):
        self.__is_run = False

    def close(self):
        '''关闭这个计时器'''
        self.pause()

        if not self.__is_close:
            self.__is_close = True

            if not self.close_callback is None:
                self.close_callback(self)

            self.__join_lock.unlock()  # 解锁

    @property
    def is_run(self):
        return self.__is_run and not self.__is_close

    @property
    def is_close(self):
        return self.__is_close

    @property
    def callback_count(self):
        return self.__callback_count

    def join(self):
        '''阻塞等待这个计时器被关闭'''
        if not self.__is_close:
            self.__join_lock.lock()

    def _update(self, interval):
        if self.__is_close or not self.__is_run:
            return

        self.__interval += interval
        while self.__interval >= self.loop_wait_time:
            self.__interval -= self.loop_wait_time
            self.__callback_count += 1
            self.callback(self)

            if self.loop_count and self.__callback_count >= self.loop_count:
                self.close()
                return


@singleton
class Timer_Manager():
    def __init__(self):
        self.__timer_list = []  # 计时器列表

        self.__timer_lock = threading.Lock()

        self.__time_interval = 0.01  # 时间间隔(计时器进度)
        self.__is_run = False
        self.__main_thread_versions = 0  # 主线程版本, 避免偶然情况下会导致同时运行多个__main_thread_fun

    def close(self):
        with self.__timer_lock:
            self.__is_run = False

    @property
    def time_interval(self):
        return self.__time_interval

    @time_interval.setter
    def time_interval(self, interval: int or float):
        if interval < 0.001:
            interval = 0.001
        self.__time_interval = interval

    def add_timer(self, timer: Timer):
        with self.__timer_lock:
            if not self.__is_run:
                self.__is_run = True

                self.__main_thread_versions += 1
                th = threading.Thread(target=self.__main_thread_fun, args=(self.__main_thread_versions,),
                                      name="Timer_Manager_Thread")
                th.setDaemon(False)
                th.start()

            if timer not in self.__timer_list:
                self.__timer_list.append(timer)

    def remove_timer(self, timer: Timer):
        with self.__timer_lock:
            if not self.__is_run:
                return

            if timer in self.__timer_list:
                self.__timer_list.remove(timer)

    def __main_thread_fun(self, main_thread_versions):
        old_time = time.time()

        while main_thread_versions == self.__main_thread_versions:
            with self.__timer_lock:
                time.sleep(self.__time_interval)

                now_time = time.time()
                interval = now_time - old_time
                old_time = now_time

                # 检查版本避免偶然情况下会导致同时调用两次__update
                if self.__is_run and main_thread_versions == self.__main_thread_versions:
                    self.__update(interval)

                if not self.__timer_list:
                    self.__is_run = False

                # 不将__clear_timer_list()放在with self.__timer_lock:之外, 避免偶然情况下错误调用__clear_timer_list()
                if not self.__is_run:
                    self.__clear_timer_list()
                    return

    def __update(self, interval):
        for timer in self.__timer_list:
            if timer.is_close:
                self.__timer_list.remove(timer)  # python中允许在遍历时删除遍历元素
            else:
                timer._update(interval)

    def __clear_timer_list(self):
        for timer in self.__timer_list:
            if not timer.is_close:
                timer.close()

        self.__timer_list.clear()

    def create_timer(self, callback, loop_wait_time: int or float, loop_count=0, close_callback=None, meta=None):
        return Timer(callback, loop_wait_time, loop_count, close_callback, meta)


if __name__ == '__main__':
    def fun1(t: Timer):
        print('回调', t.meta, t.callback_count, time.strftime('  %H:%M:%S', time.localtime()))


    def fun_de(t: Timer):
        print(t.meta, '关闭')


    import time

    t1 = Timer(fun1, 1, 5, close_callback=fun_de, meta='计时器1   ')
    t1.start()

    time.sleep(0.5)
    t2 = Timer(fun1, 1, 2, meta='  计时器2 ')
    t2.start()

    print('等待计时器1结束')
    t1.join()
    print('结束')
