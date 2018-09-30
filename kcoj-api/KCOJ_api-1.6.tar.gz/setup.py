from setuptools import setup, find_packages
from os import path

# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='KCOJ_api',
    version='1.6',
    description='A Python Module for get data from real KCOJ.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='pinlin',
    author_email='moneycat711@gmail.com',
    license='MIT License',
    packages=find_packages(),
    install_requires=['requests', 'bs4'],
    platforms=["all"],
    url='https://github.com/kcoj/KCOJ_api',)