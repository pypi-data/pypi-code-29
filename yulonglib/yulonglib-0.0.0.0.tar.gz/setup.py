# coding:utf-8

from setuptools import setup

setup(
    name='yulonglib',     # 包名字
    version='0.0.0.0',   # 包版本
    description='start',   # 简单描述
    author='pydison',  # 作者
    author_email='pydison@gmail.com',  # 作者邮箱
    url='http://pydison.github.io',      # 包的主页
    packages=['yulonglib',],                 # 包
    install_requires=['requests>=1.0',],
)
