# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    singleton_base.py
   Author :       Zhang Fan
   date：         18/09/26
   Description :  使用基类方式, 每次实例化方法都会调用该类的__init__
-------------------------------------------------
"""
__author__ = 'Zhang Fan'


class singleton(object):
    def __new__(cls):  # cls是类的定义而不是实例
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)  # 此处调用的是基类object.__new__
        return cls._instance


if __name__ == '__main__':
    class Test(singleton):
        def __init__(self):
            print('单例类初始化')


    print('即将创建t1实例')
    t1 = Test()
    t1.a = 'a'
    print('即将创建t2实例')
    t2 = Test()
    print(getattr(t2, 'a'))
