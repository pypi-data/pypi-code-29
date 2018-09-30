from distutils.core import setup
from setuptools import find_packages

packages=find_packages()
print('found packages:',packages)
setup(
    name='brainnetworks',
    version='0.1',
    packages=packages,
    license='MIT License',
    long_description=open('README.md').read(),
)
