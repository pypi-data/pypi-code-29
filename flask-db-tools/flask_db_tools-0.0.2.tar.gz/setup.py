import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='flask_db_tools',
    version='0.0.2',
    packages=find_packages(),
    install_requires=[
        'sqlalchemy-migrate',
    ],
    include_package_data=True,
    license='BSD License',
    description='Flask databases tools',
    long_description=README,
    author='Boris M',
    author_email='bb@bb.com',
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7'
    ],
)