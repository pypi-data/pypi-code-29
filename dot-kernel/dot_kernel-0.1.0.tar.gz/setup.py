# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="dot_kernel",
    version="0.1.0",
    url="https://github.com/laixintao/jupyter-dot-kernel",
    author="laixintao",
    author_email="laixintao1995@163.com",
    description="Writing dot language and render in jupyter.",
    packages=["dot_kernel"],
    install_requires=["graphviz", "jupyter"],
)
