from setuptools import setup, find_packages
from os.path import join, dirname
from distutils.core import setup

setup(
    name = 'aws_checker_basic',
    packages = find_packages(),
    version = '0.1',
    description = 'List AWS resources',
    author = 'diboan',
    author_email = 'diboan@yandex.ru',
    include_package_data=True,
    url = 'https://github.com/diboanches/aws_checker',
    download_url = 'https://github.com/diboanches/aws_checker',
)
