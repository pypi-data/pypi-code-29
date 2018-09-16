
# from distutils.core import setup
from setuptools import setup

def readme_file():
    with open("README.rst", encoding="utf-8") as rf:
        return rf.read()

setup(name="viytestlib", version="1.0.1", description="this is a lib2",packages=["viytestlib"],
      py_modules=["Tool"], author="Viy", author_email="feng743588510@163.com",
      long_description=readme_file(),
      url="https://github.com/Viy/Python_code", license="MIT")
