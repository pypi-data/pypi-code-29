# -*- encoding:utf-8 -*-

from __future__ import absolute_import
import redis


class XdeRedis:
    '''
    redis操作类
    '''

    def __init__(self, host, port, prefix='', dbindex=0):
        self.handle = redis.StrictRedis(host, port, dbindex)
        self.prefix = prefix

    def ping(self):
        '''
        ping
        :return:
        '''
        return self.handle.ping()

    def set(self, key, value, prefix=None):
        '''
        set
        '''
        if prefix is None:
            return self.handle.set(self.prefix + key, value)
        else:
            return self.handle.set(prefix + key, value)

    def setex(self, key, value, timeout, prefix=None):
        '''
        set带过期时间
        '''
        if prefix is None:
            return self.handle.setex(self.prefix + key, timeout, value)
        else:
            return self.handle.setex(prefix + key, timeout, value)

    def get(self, key, prefix=None):
        '''
        get
        '''
        if prefix is None:
            return self.handle.get(self.prefix + key)
        else:
            return self.handle.get(prefix + key)

    def delete(self, key, prefix=None):
        '''
        delete
        '''
        if prefix is None:
            return self.handle.delete(self.prefix + key)
        else:
            return self.handle.delete(prefix + key)

    def ttl(self, key, prefix=None):
        '''
                    获取过期时间
        '''
        if prefix is None:
            return self.handle.ttl(self.prefix + key)
        else:
            return self.handle.ttl(prefix + key)

    def expire(self, key, timeout, prefix=None):
        '''
                    设置过期时间
        '''
        if prefix is None:
            return self.handle.expire(self.prefix + key, timeout)
        else:
            return self.handle.expire(prefix + key, timeout)

    def incr(self, key, amount=1, prefix=None):
        '''
                    增加某键值，一般用于计数
        '''
        if prefix is None:
            return self.handle.incr(self.prefix + key, amount)
        else:
            return self.handle.incr(prefix + key, amount)

    def decr(self, key, amount=1, prefix=None):
        '''
                    减少某键值，一般用于计数
        '''
        if prefix is None:
            return self.handle.decr(self.prefix + key, amount)
        else:
            return self.handle.decr(prefix + key, amount)

    def exists(self, key, prefix=None):
        '''
                    获取某键是否存在
        '''
        if prefix is None:
            return self.handle.exists(self.prefix + key)
        else:
            return self.handle.exists(prefix + key)

    def rpush(self, key, value, prefix=None):
        '''
                    添加进列表尾部
        '''
        if prefix is None:
            return self.handle.rpush(self.prefix + key, value)
        else:
            return self.handle.rpush(prefix + key, value)

    def lpush(self, key, value, prefix=None):
        '''
                    添加进列表头部
        '''
        if prefix is None:
            return self.handle.lpush(self.prefix + key, value)
        else:
            return self.handle.lpush(prefix + key, value)

    def rpop(self, key, prefix=None):
        '''
                    从列表尾部弹出一元素
        '''
        if prefix is None:
            return self.handle.rpop(self.prefix + key)
        else:
            return self.handle.rpop(prefix + key)

    def lpop(self, key, prefix=None):
        '''
                    从列表头部弹出一元素
        '''
        if prefix is None:
            return self.handle.lpop(self.prefix + key)
        else:
            return self.handle.lpop(prefix + key)

    def llen(self, key, prefix=None):
        '''
                    获取队列长度
        '''
        if prefix is None:
            return self.handle.llen(self.prefix + key)
        else:
            return self.handle.llen(prefix + key)

    def lrange(self, key, start, end, prefix=None):
        '''
                    遍历列表
        '''
        if prefix is None:
            return self.handle.lrange(self.prefix + key, start, end)
        else:
            return self.handle.lrange(prefix + key, start, end)

    def ltrim(self, key, start, end, prefix=None):
        '''
                    从列表头部剪切指定位置元素
        '''
        if prefix is None:
            return self.handle.ltrim(self.prefix + key, start, end)
        else:
            return self.handle.ltrim(prefix + key, start, end)

    def setprefix(self, prefix):
        '''
                    设置前缀
        '''
        self.prefix = prefix


if __name__ == '__main__':
    r = XdeRedis('192.168.1.38', '6479', '', 1)

    print(r.set('test', '111'))
    print(r.get('test'))

    r2 = XdeRedis('192.168.1.38', '6479', 'test_', 1)
    print(r2.set('test2', '222'))
    print(r2.get('test2'))

    print(r2.delete('test2'))

    print(r.setex('test3', '333', 600))

    print(r.ttl('test3'))

    print(r.expire('test3', 1000))

    print(r.incr('test4', 1))

    print(r.decr('test4'))

    print(r.exists('test4'))

    print(r.rpush('test5_queue', 3))

    print(r.llen('test5_queue'))

    print(r.lrange('test5_queue', 0, 10))

    print(r.ltrim('test5_queue', 0, 2))