import hashlib
import time
import os

def inheritors(klass):
    subclasses = set()
    work = [klass]
    while work:
        parent = work.pop()
        for child in parent.__subclasses__():
            if child not in subclasses:
                subclasses.add(child)
                work.append(child)
    return subclasses

# from https://stackoverflow.com/questions/16463582/memoize-to-disk-python-persistent-memoization
# https://stackoverflow.com/posts/47385932/revisions
from diskcache import Cache
cache_dir = "./cache/"
def shelve_it(table_name):
    cache_file = os.path.join(cache_dir, table_name)
    d = Cache(cache_file)

    def decorator(func):
        def new_func(*args, **kwargs):
            cache_key = "\r".join([str(arg) for arg in args])

            if cache_key in d:
                return d[cache_key]


            ret = func(*args, **kwargs)
            d[cache_key] = ret

            return ret

        return new_func

    return decorator

def memoize(func):
    cache = {}
    def new_func(*args, **kwargs):
        cache_key = "\r".join([str(arg) for arg in args])

        if cache_key in cache:
            return cache[cache_key]

        ret = func(*args, **kwargs)
        cache[cache_key] = ret
        return ret

    return new_func

def gethash(v):
    m = hashlib.md5()
    t = str("%s" % time.time()).encode("utf-8")
    h = str(hash(v)).encode("utf-8")

    m.update(t)
    m.update(h)

    return m.hexdigest()
