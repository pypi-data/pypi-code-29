import unittest

import os

from pyfakefs import fake_filesystem_unittest


def test_generator():
    def test(self):
        self.assertTrue(1)

    return test


class TestImportAsOtherName(fake_filesystem_unittest.TestCase):
    def setUp(self):
        self.setUpPyfakefs()


if __name__ == "__main__":
    for i in range(1000):
        test_name = 'test_%i' % i
        test = test_generator()
        setattr(TestImportAsOtherName, test_name, test)
    unittest.main()
