#!/usr/bin/python
"""Factorial project"""
from setuptools import find_packages, setup

setup(name = 'gif2txt_gif',
    version = '1.0',
    description = "把GIF图片字符gif图片",
    long_description = "通过输入gif文件路径等信息,把gif图片转成字符图片png然后在合并成字符gif",
    platforms = ["Linux"],
    author="leon.hu",
    author_email="sdcxhuoxiaoqi@126.com",
    url="",
    license = "MIT",
    packages=find_packages()
    )
