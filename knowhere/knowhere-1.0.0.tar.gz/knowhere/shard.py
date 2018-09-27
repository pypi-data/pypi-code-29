import random

from datetime import datetime
from threading import Thread, Lock

class Value():
    pass

class Shard():
    def __init__(self):
        self.store = {}
        self.mx = Lock()
        self.keys = set([])

    def _set(self, key, value, ttl):
        ob = Value()
        ob.expire_at = datetime.now() + ttl
        ob.val = value
        self.store[key] = ob
        self.keys.add(key)

    def set(self, key, value, ttl):
        self.mx.acquire()
        try:
            self._set(key, value, ttl)
        finally:
            self.mx.release()

    def get(self, key):
        self.mx.acquire()
        ob = self.store.get(key)
        self.mx.release()

        if ob is None:
            return None

        if ob.expire_at < datetime.now():
            self.mx.acquire()
            self._delete(key)
            self.mx.release()
            return None

        return ob.val

    def _delete(self, key):
        del self.store[key]
        self.keys.remove(key)

    def delete(self, key):
        self.mx.acquire()
        if self.store.get(key):
            self._delete(key)
        self.mx.release()

    def flush(self):
        self.mx.acquire()
        self.store = {}
        self.keys = set([])
        self.mx.release()

    def run_eviction(self):
        now = datetime.now()
        rand_keys_len = 20

        self.mx.acquire()

        while True:
            del_keys_len = 0

            all_keys = self.store.keys()

            keys = random.sample(set(all_keys), rand_keys_len) if len(all_keys) >= rand_keys_len else all_keys
            for key in keys:
                if self.store[key].expire_at < now:
                    self._delete(key)
                    del_keys_len += 1

            if del_keys_len <= 4:
                break

        self.mx.release()
