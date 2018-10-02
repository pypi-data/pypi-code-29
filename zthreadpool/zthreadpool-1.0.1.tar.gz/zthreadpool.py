# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    zthreadpool.py
   Author :       Zhang Fan
   date：         18/09/28
   Description :  线程池
-------------------------------------------------
"""
__author__ = 'Zhang Fan'

import traceback
import threading

from zqueue import Queue
from zblocker import BLock_more


class ThreadPool():
    class _Close_Thread_Pool():
        pass

    def __init__(self, maxcount=10):
        # 初始化线程池(最多同时运行线程数量)
        assert isinstance(maxcount, int) and maxcount > 0, '线程数量必须为整数且大于0'

        self.__max_thread_count = maxcount  # 最大线程数量
        self.__thread_count = 0  # 当前运行线程数量

        self.__is_run = True  # 是否运行中
        self.__is_close = False  #

        self.__queue = Queue()  # 任务队列
        self.__run_count = 0  # 线程运行数量
        self.__join_lock = BLock_more()  # 等待锁

        self.__init_threads()  # 初始线程池

    def __init_threads(self):
        # 初始化线程池
        self.__thread_list = []

        for i in range(self.__max_thread_count):  # 循环创建线程
            th = threading.Thread(target=self.__thread_fun, args=(i,))  # 将线程目标指向内置任务
            th.setDaemon(False)
            th.start()  # 启动这个线程

            self.__thread_list.append(th)  # 将线程添加到列表

    def __thread_fun(self, thread_index):
        self.__thread_count += 1

        while self.__is_run:
            try:
                task = self.__queue.get()  # 阻塞等待任务
            except:  # 管道关闭
                break

            if task is ThreadPool._Close_Thread_Pool:  # 收到结束通知
                break

            self.__run_task(task, thread_index)

        self.__thread_count -= 1

        if self.__thread_count == 0:  # 最后一个线程结束
            self.__join_lock.unlock()

    def __run_task(self, task, thread_index):
        call, args, kwargs, errback = task
        try:
            self._log_info('\033[1;36m线程<%d>执行一个新任务\033[0m' % thread_index)
            call(*args, **kwargs)  # 调用函数
            self._log_info('\033[1;32m线程<%d>执行任务完毕\033[0m' % thread_index)
        except Exception as err:
            if errback is False or errback is None:
                return

            if errback is True:
                self._log_warn('\033[1;35m第<{}>个线程出现错误\n\033[1;31m{}\033[0m'.format(
                    thread_index, traceback.format_exc()), end='')
                return

            try:
                errback(thread_index, err)
                self._log_info('\033[1;32m线程<%d>执行任务完毕\033[0m' % thread_index)
            except Exception as err:
                self._log_info('\033[1;35m第<{}>个线程执行错误回调的时候,产生了另一个错误\n\033[1;31m{}\033[0m'.format(
                    thread_index, traceback.format_exc()), end='')

    def add_task(self, func, *args, err_callback=True, **kwargs):
        '''
        添加一个任务, 任务会等待直到有空闲线程去执行他
        :param func: 回调函数
        :param args: 回调参数
        :param err_callback: 错误回调函数, 如果设为True则打印错误, 如果设为False或者None则忽略错误
            可以设为一个回调函数, 必须接收两个参数(出错线程索引,错误对象), 如果回调函数发生错误, 会打印错误.
        :param kwargs: 回调参数
        :return:
        '''
        assert err_callback is True or err_callback is False or err_callback is None or hasattr(err_callback,
                                                                                                '__call__'), \
            'err_callback必须为True, False, None 或者存在__call__属性'
        assert not self.__is_close, '任务入口已关闭'

        self.__queue.put((func, args, kwargs, err_callback))

    def close(self):
        # 关闭任务入口不允许再添加任务
        if not self.__is_close:
            self.__is_close = True
            for i in range(self.__max_thread_count):
                self.__queue.put(ThreadPool._Close_Thread_Pool)  # 通知结束

    def join(self):
        # 等待所有任务结束
        assert self.__is_close, '必须关闭任务入口'

        if not self.__queue.is_empty():
            self.__join_lock.lock()

    def task(self, err_callback=True):
        '''
        允许使用装饰器来创建任务
        :param err_callback: 错误调用函数, 必须接收两个参数(出错线程索引,错误对象)
        '''

        def _task(func):
            def _func(*args, **kwargs):
                self.add_task(func, *args, err_callback=err_callback, **kwargs)

            return _func

        return _task

    def _log_info(self, *args, **kw):
        print(*args, **kw)

    def _log_warn(self, *args, **kw):
        print(*args, **kw)


if __name__ == '__main__':
    import time
    import threading

    p = ThreadPool(2)


    @p.task()
    def fun(a, c):
        print(a, '开始', time.strftime('  %H:%M:%S', time.localtime()))
        for i in range(c):
            time.sleep(0.01)
        print(a, '  结束', time.strftime('  %H:%M:%S', time.localtime()))


    fun('aa', 100)
    fun('bb', 100)
    fun('cc', 100)
    fun('dd', 100)
    p.close()
    p.join()
    print('--end--')
