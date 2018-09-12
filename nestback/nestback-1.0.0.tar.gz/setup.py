import setuptools


'''from distutils.core import setup'''
with open("README.md","r") as fh:
    long_description=fh.read()

setuptools.setup(
    name              ='nestback',
    version           ='1.0.0',
    py_modules        =['nestback'],
    description       ='A simple printer of nested lists',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
     )
