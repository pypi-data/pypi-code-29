#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='zmsgcentre',
    version='1.0.3',
    py_modules=['zmsgcentre'],
    author='zlyuan',
    author_email='1277260932@qq.com',
    packages=find_packages(),
    description='消息中心, 避免代码的强耦合性',
    long_description=open('description.txt', 'r', encoding='utf8').read(),  # 项目介绍
    url='https://pypi.org/',
    license='GNU GENERAL PUBLIC LICENSE',
    platforms=['all'],
    scripts=[],  # 额外的文件
    install_requires=[],  # 依赖库
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
