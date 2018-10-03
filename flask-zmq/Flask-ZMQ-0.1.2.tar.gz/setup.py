"""
Flask-ZMQ
----------

Adds ZMQ support to your Flask application.
"""
import setuptools
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='Flask-ZMQ',
    version='0.1.2',
    url='https://github.com/rebill/flask-zmq',
    license='BSD',
    author='Rebill',
    author_email='rebill@qq.com',
    description='Flask extension for ZMQ',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    platforms='any',
    install_requires=[
        'Flask',
        'pyzmq',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
