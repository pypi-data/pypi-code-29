#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='zthreadpool',
    version='1.0.1',
    py_modules=['zthreadpool'],
    author='zlyuan',
    author_email='1277260932@qq.com',
    packages=find_packages(),
    description='线程池, 固定指定数量的线程来执行任务, 避免重复创建和销毁线程时的资源消耗',
    long_description=open('description.txt', 'r', encoding='utf8').read(),  # 项目介绍
    url='https://pypi.org/',
    license='GNU GENERAL PUBLIC LICENSE',
    platforms=['all'],
    scripts=[],  # 额外的文件
    install_requires=['zqueue>=1.2.0', 'zblocker'],  # 依赖库
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
