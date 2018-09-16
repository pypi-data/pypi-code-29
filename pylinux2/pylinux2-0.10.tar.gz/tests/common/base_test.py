# /usr/bin/env python
# coding=utf-8
import shutil
import unittest

from pylinux.system_file.base_system_file import BaseSystemFile

from tests import context


class BaseTest(unittest.TestCase):
    test_fp = None

    @classmethod
    def setUpClass(cls):
        BaseTest.test_fp = context.get_test_abs_filepath("base_system_file.test")

    @classmethod
    def tearDownClass(cls):
        BaseTest.test_fp = None

    def setUp(self):
        self.base_system_file = BaseSystemFile(BaseTest.test_fp)

    def tearDown(self):
        self.base_system_file = None

    @staticmethod
    def cp_example_file(origin_fp, target_fp):
        shutil.copyfile(origin_fp, target_fp)


if __name__ == '__main__':
    unittest.main()
