import collections

class Cache:
    def __init__(self, maxlen):
        self.maxlen = maxlen
        self.cache = collections.OrderedDict()

    def __contains__(self, key):
        return key in self.cache

    def __getitem__(self, key):
        value = self.cache.pop(key)
        self.cache[key] = value
        return value

    def __len__(self):
        return len(self.cache)

    def __setitem__(self, key, value):
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.maxlen:
                self.cache.popitem(last=False)
        self.cache[key] = value

    def clear(self):
        self.cache.clear()

    def get(self, key, fallback=None):
        try:
            return self[key]
        except KeyError:
            return fallback

    def pop(self, key):
        return self.cache.pop(key)

    def remove(self, key):
        try:
            self.pop(key)
        except KeyError:
            pass


# class Cache:
#     def __init__(
#             self,
#             *,
#             leniency=0,
#             maxage=None,
#             maxlen=None,
#             shrink_delay=None,
#         ):
#         self.leniency = leniency
#         self.maxage = maxage
#         self.maxlen = maxlen
#         self.shrink_delay = shrink_delay
#         self.last_shrink = time.time()

#         self._dict = {}
#         self._recency = {}

#     def __contains__(self, key):
#         return key in self._dict

#     def __getitem__(self, key):
#         self._shrink()
#         if self.maxage is not None:
#             if (time.time() - self._recency[key]) > self.maxage:
#                 self.remove(key)
#                 raise KeyError(key)
#         value = self._dict[key]
#         self._maintain(key)
#         return value

#     def __setitem__(self, key, value):
#         self._shrink()
#         self._dict[key] = value
#         self._maintain(key)

#     def _maintain(self, key):
#         self._recency[key] = time.time()

#     def _shrink(self):
#         if self.shrink_delay is not None:
#             if time.time() - self.last_shrink > self.shrink_delay:
#                 return

#         now = time.time()
#         self.last_shrink = now

#         if self.maxlen is None:
#             pop_count = 0
#         else:
#             pop_count = len(self._dict) - self.maxlen
#             pop_count = max(0, pop_count)
#             if pop_count < self.maxlen * self.leniency:
#                 pop_count = 0

#         if pop_count == 0 and self.maxage is None:
#             return

#         keys = sorted(self._recency.keys(), key=self._recency.get)

#         if pop_count > 0:
#             for key in itertools.islice(keys, 0, pop_count):
#                 self.remove(key)

#         if self.maxage is not None:
#             for key in itertools.islice(keys, pop_count, None):
#                 last_used = self._recency[key]
#                 age = now - last_used
#                 if age > self.maxage:
#                     self.remove(key)

#     def clear(self):
#         self._dict.clear()
#         self._recency.clear()

#     def get(self, key, fallback=None):
#         try:
#             return self[key]
#         except KeyError:
#             return fallback

#     def remove(self, key):
#         try:
#             self._dict.pop(key)
#         except KeyError:
#             pass

#         try:
#             self._recency.pop(key)
#         except KeyError:
#             pass
