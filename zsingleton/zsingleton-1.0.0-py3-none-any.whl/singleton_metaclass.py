# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    singleton_metaclass.py
   Author :       Zhang Fan
   date：         18/09/26
   Description :  使用类的metaclass设置元类, 只有第一次使用实例化方法才会调用__init__
-------------------------------------------------
"""
__author__ = 'Zhang Fan'


class singleton(type):
    def __call__(self, *args, **kwargs):  # 每次调用实例化函数会转到这里
        if not hasattr(self, '_instance'):
            self._instance = super().__call__(*args, **kwargs)
        return self._instance


if __name__ == '__main__':
    class Test(metaclass=singleton):
        def __init__(self):
            print('单例类初始化')


    print('即将创建t1实例')
    t1 = Test()
    t1.a = 'a'
    print('即将创建t2实例')
    t2 = Test()
    print(getattr(t2, 'a'))
