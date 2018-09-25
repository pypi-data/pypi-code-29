#!/usr/bin/env python
# coding:utf-8


from setuptools import setup, find_packages

setup(
    name="feiyan",
    version="1.0.0",
    keywords=("pip", "feiyan", "jerrygaoyang"),
    description="An feature extraction algorithm",
    license="MIT Licence",
    url="",
    author="jerrygaoyang",
    author_email="917616767@qq.com",
    packages=find_packages(),
    include_package_data=True,
    platforms="aliyun",
    install_requires=["requests"]
)
