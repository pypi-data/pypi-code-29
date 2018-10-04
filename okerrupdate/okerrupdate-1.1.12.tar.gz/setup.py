from setuptools import setup
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='okerrupdate',
    version='1.1.12',
    description='micro client for okerr cloud monitoring system',
    url='http://okerr.com/',
    author='Yaroslav Polyakov',
    author_email='xenon@sysattack.com',
    license='MIT',
    packages=['okerrupdate'],
    scripts=['scripts/okerrupdate'],

    long_description = read('README.md'),
    long_description_content_type='text/markdown',

    install_requires=['requests','future'],
    zip_safe=False
)    

