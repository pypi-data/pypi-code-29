import os
from setuptools import setup


def read_readme():
    with open("README.md", "r") as f:
        long_description = f.read()

    return long_description


setup(
    name='simplesqlitewrap',
    version='0.1.15',
    description='Simple util from which I inherit my sqlite classes',
    long_description=read_readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/zeroone2numeral2/simplesqlitewrap',
    author='zeroone2numeral2',
    license='MIT',
    packages=['simplesqlitewrap'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Database",
    ),
    zip_safe=False
)