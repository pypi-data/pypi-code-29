# /usr/bin/env python
# coding=utf-8

import unittest

import context

from pylinux.common.util import file_util
from pylinux.system_file.base_system_file import BaseSystemFile

from tests.common.base_test import BaseTest


class TestBaseSystemFile(BaseTest):
    test_fp = None

    @classmethod
    def setUpClass(cls):
        TestBaseSystemFile.test_fp = context.get_test_abs_filepath("base_system_file.test")

    @classmethod
    def tearDownClass(cls):
        TestBaseSystemFile.test_fp = None

    def setUp(self):
        self.base_system_file = BaseSystemFile(TestBaseSystemFile.test_fp)

    def tearDown(self):
        self.base_system_file = None

    def test_no_comment(self):
        """
        验证一个配置项在没有注释情况下是否能成功
        :return:
        """
        name = "test_no_comment"
        expected = name + "_value"
        value = self.base_system_file.get_setting(name)
        self.assertEqual(value, expected)

    def test_error_comment(self):
        """
        验证一个配置项在错误注释情况下是否能成功
        应该是能成功的，注释被忽略
        :return:
        """
        name = "test_error_comment"
        expected = name + "_value"
        value = self.base_system_file.get_setting(name)
        self.assertEqual(value, expected)

    def test_correct_name(self):
        """
        验证happy path
        :return:
        """
        name = "test_correct_name"
        expected = name + "_value"
        value = self.base_system_file.get_setting(name)
        self.assertEqual(value, expected)

    def test_left_space_name(self):
        """
        验证一个配置项在 左侧有空白的情况下是否能成功
        :return:
        """
        name = "test_left_space_name"
        expected = name + "_value"
        value = self.base_system_file.get_setting(name)
        self.assertEqual(value, expected)

    def test_right_space_name(self):
        """
        验证一个配置项在 右侧有空白的情况下是否能成功
        :return:
        """
        name = "test_right_space_name"
        expected = name + "_value"
        value = self.base_system_file.get_setting(name)
        self.assertEqual(value, expected)

    def test_both_space_name(self):
        """
        验证一个配置项在 双侧有空白的情况下是否能成功
        :return:
        """
        name = "test_both_space_name"
        expected = name + "_value"
        value = self.base_system_file.get_setting(name)
        self.assertEqual(value, expected)

    def test_connector_space_name(self):
        """
        验证一个配置项在 连接符附近有空白的情况下是否能成功
        :return:
        """
        name = "test_connector_space_name"
        expected = name + "_value"
        value = self.base_system_file.get_setting(name)
        self.assertEqual(value, expected)

    def test_add_setting(self):
        """
        验证增加一个配置项
        :return:
        """
        random_fp = file_util.generate_tmp_fp()
        self.cp_example_file(self.test_fp, random_fp)
        tmp_file = BaseSystemFile(random_fp)
        tmp_file.set_setting("liu", "rui")

        now_file = BaseSystemFile(random_fp)
        self.assertEqual("rui", now_file.get_setting("liu"))

    def test_update_setting(self):
        """
        test update a setting
        :return:
        """
        random_fp = file_util.generate_tmp_fp()
        self.cp_example_file(self.test_fp, random_fp)
        tmp_file = BaseSystemFile(random_fp)
        tmp_file.set_setting("test_update_setting", "after_value")

        now_file = BaseSystemFile(random_fp)
        self.assertEqual("after_value", now_file.get_setting("test_update_setting"))


if __name__ == '__main__':
    unittest.main()
