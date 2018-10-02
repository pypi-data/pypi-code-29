#!/usr/bin/env python

# ------------------------------------------------------------------------
#
#  This file is part of the Chirp Connect Python SDK.
#  For full information on usage and licensing, see http://chirp.io/
#
#  Copyright (c) 2011-2018, Asio Ltd.
#  All rights reserved.
#
# ------------------------------------------------------------------------

import os
import re
import platform
from setuptools import setup, Extension

vstr = open('chirpsdk/__init__.py', 'r').read()
regex = r"^__version__ = ['\"]([^'\"]*)['\"]"
version = re.search(regex, vstr, re.M)

if platform.system() == 'Darwin':
    arch = 'darwin'
elif platform.system() == 'Linux':
    arch = 'rpi' if os.uname()[4].startswith('arm') else 'linux'
else:
    raise RuntimeError('The Chirp Python SDK is not configured for %s platforms. ' \
                       'Please contact contact@chirp.io for custom builds' % platform)

connect = Extension('_connect',
                    sources=['chirpsdk/_connect.c'],
                    include_dirs=['./chirpsdk', './chirpsdk/include'],
                    library_dirs=['./chirpsdk/libraries/' + arch],
                    runtime_library_dirs=['$ORIGIN/chirpsdk/libraries/' + arch],
                    libraries=['chirp-connect-shared'])

setup(
    name='chirpsdk',
    version=version.group(1),
    description='Chirp Connect Python SDK',
    long_description='The Chirp Connect Python SDK enables the user to send '
                     'and receive data using the device\'s microphone and speaker.',
    license='License :: Other/Proprietary License',
    author='Asio Ltd.',
    author_email='developers@chirp.io',
    url='https://developers.chirp.io',
    packages=['chirpsdk', 'tests', 'bin'],
    ext_modules=[connect],
    install_requires=[
        'sounddevice>=0.3.10', 'pysoundfile>=0.9.0',
        'requests>=2.18.1', 'requests-futures==0.9.7',
        'configparser==3.5.0'
    ],
    include_package_data=True,
    tests_require=['mock==2.0.0'],
    keywords=['sound', 'networking', 'chirp'],
    scripts=[
        'bin/chirp-audio-read', 'bin/chirp-audio-write',
        'bin/chirp-receive', 'bin/chirp-send'
    ],
    test_suite='tests',
    classifiers=[
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Communications',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers'
    ]
)
