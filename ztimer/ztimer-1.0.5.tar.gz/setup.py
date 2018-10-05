#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='ztimer',
    version='1.0.5',
    py_modules=['ztimer'],
    author='zlyuan',
    author_email='1277260932@qq.com',
    packages=find_packages(),
    description='计时器池管理器, 将多个计时器挂在到计时器管理器中, 用一个线程来统一管理, 减少资源消耗',
    long_description=open('description.txt', 'r', encoding='utf8').read(),  # 项目介绍
    url='https://pypi.org/',
    license='GNU GENERAL PUBLIC LICENSE',
    platforms=['all'],
    scripts=[],  # 额外的文件
    install_requires=['zsingleton', 'zblocker>=1.0.2'],  # 依赖库
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ]
)
