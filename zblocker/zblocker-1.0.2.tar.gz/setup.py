#!/usr/bin/env python
# coding=utf-8

from setuptools import setup,find_packages
setup(
    name = 'zblocker',           #上传到网站后将显示在网页上的模块名字
    version = '1.0.2',
    py_modules = ['zblocker'],
    author='zlyuan',
    author_email='1277260932@qq.com',
    packages = find_packages(),
    description = '阻塞器, 单人阻塞器和多人阻塞器',
    long_description=open('description.txt','r',encoding='utf8').read(),     #项目介绍
    url='https://pypi.org/',
    license='GNU GENERAL PUBLIC LICENSE',
    platforms=['all'],
    scripts = [],              #额外的文件
    install_requires=[],                        #依赖库
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
