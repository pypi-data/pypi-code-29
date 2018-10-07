# encoding: utf8
from distutils.core import setup
from setuptools import find_packages

setup(
    name='japanize-matplotlib',
    version='1.0.0',
    description='matplotlibのフォント設定を自動で日本語化する',
    author='uehara1414',
    author_email='akiya.noface@gmail.com',
    url='https://github.com/uehara1414/japanize-matplotlib',
    packages=find_packages(),
    package_data={
        'fonts': ['fonts'],
    },
)
