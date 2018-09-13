"""
Setup for Docs Configuration
"""
from setuptools import setup, find_packages

from docs_conf import __author__
from docs_conf import __version__


with open('requirements.txt') as f:
    install_reqs = f.read().splitlines()


setup(
    setup_requires=['pbr'],
    pbr=True,
    install_requires=install_reqs
)
