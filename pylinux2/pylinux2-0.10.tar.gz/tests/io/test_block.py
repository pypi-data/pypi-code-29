# /usr/bin/env python
# coding=utf-8
import unittest

# noinspection PyUnresolvedReferences
from .. import context
from pylinux.io.block import parse_lsblk_output


class TestBlock(unittest.TestCase):

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

    def test_block(self):
        text = """
NAME  FSTYPE   SIZE TYPE MOUNTPOINT
xvda           250G disk
xvda1 ext4     250G part /
xvdb  ext4    1000G disk /home/admin/name/123
xvdc  ext4    1000G disk /home/admin/name/123/xxx
"""
        block_list = parse_lsblk_output(text)
        for block in block_list:
            print block

        print block_list[0].partitions
        self.assertEqual(len(block_list[0].partitions), 1)


if __name__ == '__main__':
    unittest.main()
