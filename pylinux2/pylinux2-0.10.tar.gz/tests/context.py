# /usr/bin/env python
# coding=utf-8

import os
import sys

self_folder_path = os.path.dirname(__file__)
sys.path.insert(0, os.path.abspath(os.path.join(self_folder_path, '..')))

# noinspection PyUnresolvedReferences
import pylinux


def get_test_abs_filepath(filename):
    """
    获取测试所用文件的绝对路径
    :param filename:
    """
    return os.path.abspath(os.path.join(self_folder_path, "files", filename))
