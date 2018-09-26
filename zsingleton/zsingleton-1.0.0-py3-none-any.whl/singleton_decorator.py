# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    singleton.py
   Author :       Zhang Fan
   date：         18/09/26
   Description :  使用装饰器方式, 只有第一次使用实例化方法才会调用__init__
-------------------------------------------------
"""
__author__ = 'Zhang Fan'


def singleton(cls):  # cls是类的定义而不是实例
    def instance(*args, **kw):
        if not hasattr(cls, '_instance'):
            cls._instance = cls(*args, **kw)
        return cls._instance

    return instance


if __name__ == '__main__':
    @singleton
    class Test():
        def __init__(self):
            print('单例类初始化')


    print('即将创建t1实例')
    t1 = Test()
    t1.a = 'a'
    print('即将创建t2实例')
    t2 = Test()
    print(getattr(t2, 'a'))
