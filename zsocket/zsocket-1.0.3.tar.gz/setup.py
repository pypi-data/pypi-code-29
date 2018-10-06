#!/usr/bin/env python
# coding=utf-8

from setuptools import setup,find_packages
setup(
    name = 'zsocket',           #上传到网站后将显示在网页上的模块名字
    version = '1.0.3',
    py_modules = [],
    author='zlyuan',
    author_email='1277260932@qq.com',
    packages = find_packages(),
    description = '网络连接socket封装, 支持心跳包, 支持长连接, 断线检测, 不粘包',
    long_description=open('description.txt','r',encoding='utf8').read(),     #项目介绍
    url='https://pypi.org/',
    license='GNU GENERAL PUBLIC LICENSE',
    platforms=['all'],
    scripts = ['description.txt'],              #额外的文件
    install_requires=['ztimer>=1.0.5'],                        #依赖库
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
