from droplo.cache import ShelveCache
import unittest
import time


class TestCache(unittest.TestCase):

    def setUp(self):
        self.cache = ShelveCache("cachetest")

    def test_cache_set_get(self):
        self.cache.set("foo", "bar", 3600)
        self.assertEqual(self.cache.get("foo"), "bar")

    def test_cache_expiration(self):
        self.cache.set("toto", "tata", 2)
        time.sleep(3)
        self.assertIsNone(self.cache.get("toto"))


if __name__ == '__main__':
    unittest.main()
