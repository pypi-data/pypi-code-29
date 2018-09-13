
from setuptools import setup,find_packages
import sys

setup(
    name="technologycycle",
    version="1.0.2",
    description="a tool for patent trend analysis",
    long_description="i am a little teapot",
    author="qqqq",
    author_email="1412187956@qq.com",
    license="MIT",
    url="https://pypi.org/manage/projects/",
    packages=['technologycycle'],
    install_requires=[
        "numpy",
        "scipy",
        "matplotlib",
        "xlrd",
        ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
)
