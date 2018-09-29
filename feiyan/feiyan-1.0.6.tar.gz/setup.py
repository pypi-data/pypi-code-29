#!/usr/bin/env python
# coding:utf-8


from setuptools import setup, find_packages

with open("feiyan/README.md", "r") as f:
    long_description = f.read()

setup(
    name="feiyan",
    version="1.0.6",
    author="jerrygaoyang",
    author_email="917616767@qq.com",
    description="iot feiyan package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jerrygaoyang/feiyan",
    packages=find_packages(),
    install_requires=["requests"]
)
