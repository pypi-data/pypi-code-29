# /usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='pylinux2',
    version='0.10',
    description="a python library which helps to access linux resources",
    keywords='python linux resource',
    author='ruiruige',
    author_email='whx20202@gmail.com',  # 作者邮箱
    url='https://github.com/ruiruige',  # 作者链接
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[  # 需求的第三方模块
        'enum',
    ],
    entry_points={},
)
