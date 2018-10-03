from setuptools import setup

def readme_file():
    with open("README.rst", encoding="utf-8") as rf:
        return rf.read()

setup(name="prtestlib", version="1.0.1", description="This is a excellent lib", packages=["sztestlib"], py_modules=["Tool"], author="Sz", author_email="caiseyingzi@gmail.com", long_description=readme_file(), url="https://caiseyingzi.com", license="MIT")

