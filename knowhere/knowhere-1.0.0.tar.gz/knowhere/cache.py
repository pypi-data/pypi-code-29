import xxhash, math

from shard import Shard
from datetime import datetime, timedelta
from timeloop import Timeloop


class ShardSizeNotPowerOf2(Exception):
    pass

class Cache():
    def __init__(self, shard_size=16, eviction_interval=timedelta(minutes=1)):
        self.shard_size = shard_size
        self.shards = [None]*self.shard_size
        self.eviction_interval = eviction_interval

        if 2 ** int(math.log(self.shard_size, 2) + 0.5) != self.shard_size:
            raise ShardSizeNotPowerOf2()

        for i in range(0, self.shard_size):
            self.shards[i] = Shard()

        self._run_eviction()

    def set(self, key, value, ttl=timedelta(minutes=5)):
        shard = self._get_shard(key)
        shard.set(key, value, ttl)

    def get(self, key):
        shard = self._get_shard(key)
        return shard.get(key)

    def delete(self, key):
        shard = self._get_shard(key)
        return shard.delete(key)

    def flush(self):
        for shard in self.shards:
            shard.flush()

    def _get_shard(self, key):
        hashed_key = xxhash.xxh64(b'{}'.format(key)).intdigest()
        return self.shards[hashed_key & (self.shard_size - 1)]

    def _run_eviction(self):
        tl = Timeloop()

        @tl.job(interval=self.eviction_interval)
        def eviction():
            for shard in self.shards:
                shard.run_eviction()

        tl.start()
        self.tl = tl

    def close(self):
        self.tl.stop()

    def info(self):
        return {
            "shards": [{"id": i, "num_keys": len(self.shards[i].keys)} for i in range(0, self.shard_size)]
        }

    def keys(self):
        keys = []
        for shard in self.shards:
            [keys.append(k) for k in shard.keys]
        return keys
