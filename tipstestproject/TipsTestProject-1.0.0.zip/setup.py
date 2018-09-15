# from distutils.core import setup
from setuptools import setup

def readme_file():
    with open("README.rst", encoding="utf-8") as rf:
        return rf.read()

setup(name="TipsTestProject",version="1.0.0",description="this is a niubi lib",packages=["Tipstestlib"], py_modules=["tools"], author="Tips Lee",author_email="tips@qq.com",long_description=readme_file(),url="http://github.com/",licence="MIT")
