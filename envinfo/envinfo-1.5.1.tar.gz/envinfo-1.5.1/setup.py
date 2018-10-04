import os
from setuptools import setup


setup(
    name='envinfo',
    version='1.5.1',
    install_requires=[
        'synfo'
    ],
    url='https://github.com/mrstephenneal/synfo',
    license='GPL-3.0',
    author='Stephen Neal',
    author_email='stephen@stephenneal.net',
    description='Legacy wrapper module for synfo.'
)

os.system('pip uninstall envinfo')
