# -*- coding: utf-8 -*-
# @Time    : 18-9-28 下午1:16
# @Author  : duyongan
# @FileName: setup.py
# @Software: PyCharm

from setuptools import setup, find_packages
import sys

from distutils.core import setup

setup(
    name='simple_pickle',
    version='1.0.0',
    packages=['simple_pickle'],
    author='Haydon',
    author_email='13261051171@163.com',
    description='easy utils for pickle load/dump and write/read file'
)