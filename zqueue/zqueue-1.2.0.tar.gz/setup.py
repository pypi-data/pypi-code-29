#!/usr/bin/env python
# coding=utf-8

from setuptools import setup,find_packages
setup(
    name = 'zqueue',           #上传到网站后将显示在网页上的模块名字
    version = '1.2.0',
    py_modules = ['zqueue'],
    author='zlyuan',
    author_email='1277260932@qq.com',
    packages = find_packages(),
    description = '本地队列模块\n相对别的队列模块提高了执行速度并且减少了资源开销',
    long_description=open('description.txt','r',encoding='utf8').read(),     #项目介绍
    url='https://pypi.org/',
    license='GNU GENERAL PUBLIC LICENSE',
    platforms=['all'],
    scripts = [],              #额外的文件
    install_requires=['zblocker'],                        #依赖库
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
