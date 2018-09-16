# /usr/bin/env python
# coding=utf-8
import unittest

# noinspection PyUnresolvedReferences
import context
from context import get_test_abs_filepath
from pylinux.system_file.rc_local import RcLocal


class TestRcLocal(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        必须使用@classmethod 装饰器,所有test运行前运行一次
        :return:
        """
        print('setUpClass')

    def setUp(self):
        """
        每个测试用例执行之前做操作
        :return:
        """
        print('setUp')

    def tearDown(self):
        """
        每个测试用例执行之后做操作
        :return:
        """
        self.config_file = None
        print('tearDown')

    def test_get_single_line_setting(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
