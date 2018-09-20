# -*- coding: utf-8 -*-
# ===============================================================
#  @author: huangchi@zhiyitech.cn
#  @date: 2018/9/17 上午11:49
#  @brief: 
# ===============================================================

import setuptools

with open("spider_task_monitor/README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="spider_task_monitor",
    version="0.0.5",
    author="IceFruit",
    author_email="huangchi@zhiyitech.cn",
    description="对于爬虫任务调度的监控",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/IceFruit0777/py_package/tree/master/spider_task_monitor",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
