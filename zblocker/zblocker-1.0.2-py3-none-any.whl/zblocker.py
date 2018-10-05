# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    zblocker.py
   Author :       Zhang Fan
   date：         18/09/28
   Description :  阻塞器
-------------------------------------------------
"""
__author__ = 'Zhang Fan'

from threading import Lock as base_lock


class BLock():
    '''阻塞器'''

    def __init__(self):
        self.__is_lock = False
        self.__lock = base_lock()
        self.__lock.acquire()

    def lock(self, show_lock_err=False):
        '''
        调用此方法的一个线程会被阻塞
        :param show_lock_err: 如果一个线程已锁定的状态下,另一个线程申请锁定,在show_lock_err为True时会报错,为False时后者不会阻塞
        '''
        if self.__is_lock:
            if not show_lock_err:
                return
            raise AssertionError('一个线程已阻塞')

        self.__is_lock = True
        self.__lock.acquire()  # 阻塞
        self.__is_lock = False

    def unlock(self):
        if self.__is_lock:
            self.__lock.release()

    @property
    def locked(self):
        return self.__is_lock


class BLock_more():
    '''多人阻塞器'''

    def __init__(self):
        self.__lock = base_lock()
        self.__lock.acquire()
        self.__lock_count = 0

        self.__join_lock = base_lock()

    def lock(self):
        '''任何线程调用此方法都会被阻塞'''
        if self.__lock_count == 0:
            self.__join_lock.acquire()

        self.__lock_count += 1
        with self.__lock:  # 阻塞
            self.__lock_count -= 1

        if self.__lock_count == 0:
            if self.__join_lock.locked():
                self.__join_lock.release()

            self.__lock.acquire()

    def unlock(self):
        '''解除所有调用lock()线程的阻塞'''
        if self.__lock_count > 0:
            self.__lock.release()

    def locker_count(self):
        '''有多少线程阻塞中'''
        return self.__lock_count

    def join(self):
        '''阻塞直到所有调用lock()的线程解除阻塞'''
        if self.__lock_count > 0:
            self.__join_lock.acquire()
            self.__join_lock.release()


if __name__ == '__main__':
    print('测试单人阻塞器')


    def fun():
        for i in range(5):
            time.sleep(1)
            a.unlock()


    import threading
    import time

    a = BLock()
    threading.Thread(target=fun).start()

    for i in range(5):
        print('开始锁定', i, time.strftime('%H:%M:%S', time.localtime()))
        a.lock()  # 阻塞
        print('  解除', i, time.strftime('%H:%M:%S', time.localtime()))

    print('结束\n\n')

if __name__ == '__main__':
    print('测试多人阻塞器')


    def fun1(value):
        print('阻塞', value)
        a.lock()
        print('  解除', value)


    def fun2():
        print('--2秒后解除所有阻塞--', time.strftime('%H:%M:%S', time.localtime()))
        time.sleep(2)
        print('--即将解除所有阻塞--', time.strftime('%H:%M:%S', time.localtime()))
        a.unlock()


    import threading
    import time

    a = BLock_more()

    for i in range(5):
        threading.Thread(target=fun1, args=(i,)).start()
    threading.Thread(target=fun2).start()

    a.join()
    print('结束')
