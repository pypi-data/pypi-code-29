# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    zqueue.py
   Author :       Zhang Fan
   date：         18/09/27
   Description :
-------------------------------------------------
"""
__author__ = 'Zhang Fan'

from threading import Lock

from zblocker import BLock_more


class queue_close():
    pass


class Queue():
    '''先进先出队列'''

    def __init__(self, maxsize=None):
        '''
        初始化一个队列
        :param maxsize:最大允许放入数量
        '''
        self.__maxsize = maxsize  # 设置后不允许修改,否则可能会出现无法预知的错误
        self.__obj_list = []  # 保存数据的对象
        self.__obj_count = 0  # 对象数量

        self.__close = False  # 是否关闭了队列

        self.__put_lock = Lock()  # put锁
        self.__get_lock = Lock()  # get锁
        self.__join_lock = BLock_more()  # 等待锁

        self.__get_lock.acquire()  # 锁定get

    def put(self, obj, show_close_err=True):
        '''
        放入一个数据, 如果队列已满则阻塞
        :param obj: 要放入的数据
        :param show_close_err: show_close_err为True时, 如果队列已关闭会报错
        :return: 正常放入数据返回True, 队列关闭时返回False或报错
        '''
        assert not self.__close, '队列已关闭'
        self.__put_lock.acquire()  # 获取写入权限

        if self.__close:
            self._unlock_putlock()  # 释放写入权限
            if not show_close_err:
                return False
            raise AssertionError('队列已关闭')

        self._put(obj)

        if self.__obj_count == 1:  # 第一次产生队列
            self._unlock_getlock()  # 释放读取权限
        if self.__maxsize and self.__obj_count == self.__maxsize:  # 存在最大值并且达到最大值
            return True  # 不释放写入权限

        self._unlock_putlock()  # 释放写入权限
        return True

    def get(self, show_close_err=True):
        '''
        取出一个数据, 如果没有数据则阻塞
        :param show_close_err: show_close_err为True时, 如果队列已关闭会报错
        :return: 正常获取数据返回该数据, 队列关闭时返回zqueue.queue_close类或报错
        '''
        '''获取一个数据,如果队列已关闭会报错'''
        self.__get_lock.acquire()  # 获取读取权限

        if self.__close:
            self._unlock_getlock()  # 释放读取权限
            if not show_close_err:
                return queue_close
            raise AssertionError('队列已关闭')

        obj = self._get()

        if self.__maxsize and self.__obj_count == self.__maxsize - 1:  # 存在最大值并且刚从最大值降下来
            self._unlock_putlock()  # 释放写入权限
        if self.__obj_count == 0:  # 无队列
            self.__join_lock.unlock()  # 释放等待锁
            return obj  # 不释放读取权限

        self._unlock_getlock()  # 释放读取权限
        return obj

    def qsize(self):
        return self.__obj_count

    @property
    def count(self):
        '''获取队列数量'''
        return self.__obj_count

    def empty(self):
        return self.__obj_count == 0

    def is_empty(self):
        '''如果队列为空返回True,不为空返回False'''
        return self.__obj_count == 0

    def full(self):
        return not self.__maxsize or self.__obj_count == self.__maxsize

    def is_full(self):
        '''判断队列是否已满'''
        return not self.__maxsize or self.__obj_count == self.__maxsize

    @property
    def is_close(self):
        return self.__close

    def join(self):
        # 等待队列关闭或所有数据被取出
        if not self.__close and self.__obj_count > 0:
            self.__join_lock.lock()

    def close(self):
        # 关闭队列
        if not self.__close:
            self.__close = True
            self.__join_lock.unlock()
            self._unlock_putlock()
            self._unlock_getlock()

    def _put(self, obj):
        self.__obj_list.append(obj)  # 放到最后
        self.__obj_count += 1

    def _get(self):
        return self._get_fifo()

    def _get_fifo(self):
        obj = self.__obj_list.pop(0)  # 取出最前
        self.__obj_count -= 1
        return obj

    def _get_lifo(self):
        obj = self.__obj_list.pop()  # 取出最后
        self.__obj_count -= 1
        return obj

    def _unlock_putlock(self):
        if self.__put_lock.locked():
            self.__put_lock.release()

    def _unlock_getlock(self):
        if self.__get_lock.locked():
            self.__get_lock.release()


class LifoQueue(Queue):
    '''后进先出队列'''

    def _get(self):
        return self._get_lifo()  # 取出最后


if __name__ == '__main__':
    def fun_put():
        for i in range(10):
            print('put_start')
            q.put(i)
            print('put', i, '\n')


    def fun_get():
        while True:
            if q.is_empty():
                return

            print('  get_start')
            v = q.get()
            print('  get', v)

            time.sleep(0.3)


    import time
    import threading

    q = Queue(3)

    t1 = threading.Thread(target=fun_put)
    t2 = threading.Thread(target=fun_get)

    t1.start()
    time.sleep(0.5)
    t2.start()

    q.join()
    print('结束')
