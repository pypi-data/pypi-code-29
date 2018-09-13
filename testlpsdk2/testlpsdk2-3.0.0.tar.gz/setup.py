import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    from distutils.command.build_py import build_py

install_requires = ['playsound']
if sys.version_info < (2, 6):
    install_requires.append('requests >= 0.8.8, < 0.10.1')
    install_requires.append('ssl')
else:
    install_requires.append('requests >= 0.8.8')

if sys.version_info < (3, 0):
    try:
        from util import json
    except ImportError:
        install_requires.append('simplejson')

setup(
    name='testlpsdk2',
    packages=['testlpsdk2'],
    version='3.0.0',
    description='Lyrebird Vocal Avatar SDK for Python',
    author='The Lyrebird Team',
    author_email='support@lyrebird.ai',
    cmdclass={'build_py': build_py},
    install_requires=install_requires,
    url='https://github.com/Momoumar/testlpsdk',
    keywords=['LYREBIRD-AI', 'TTS', 'AI', 'VOCAL AVATAR', 'VOICE'],
)
