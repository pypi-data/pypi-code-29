#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Note: To use the 'upload' functionality of this file, you must:
#   $ pip install twine

import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command

# Package meta-data.
NAMESPACE = 'sine'
MODULE_NAME = 'alarmclock'
NAME = NAMESPACE + '.' + MODULE_NAME
DESCRIPTION = 'Windows command line alarm clock (python2)'
URL = 'https://github.com/SineObama/AlarmClock'
EMAIL = '714186139@qq.com'
AUTHOR = 'Xian Zheng'
REQUIRES_PYTHON = '>=2.7.0'
VERSION = None

# What packages are required for this module to be executed?
REQUIRED = [
    'plone.synchronize',
    'sine.threads>=0.1.5',
    'sine.path',
    'sine.properties',
]

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier for that!

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    with open(os.path.join(here, NAMESPACE, MODULE_NAME, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION

class MyCommand(Command):
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('>>>>{0}'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

class UploadCommand(MyCommand):
    """Support setup.py upload."""

    description = 'Build and publish the package.'

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPi via Twine…')
        os.system('twine upload dist/*')

        self.status('Pushing git tags…')
        os.system('git tag v{0}'.format(about['__version__']))
        os.system('git push --tags')
        
        sys.exit()

class ReinstallCommand(MyCommand):
    """repack the package and reinstall locally."""
    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uninstalling the package locally')
        os.system('pip uninstall ' + NAME)

        self.status('Installing the package locally')
        for name in os.listdir('dist'):
            if name.endswith('.whl'):
                break
        else:
            self.status('internal error: can not find .whl file in dist/')
            sys.exit()
        os.system('pip install dist/' + name)
        
        sys.exit()

class UninstallCommand(MyCommand):
    def run(self):
        self.status('Uninstalling the package locally')
        os.system('pip uninstall ' + NAME)
        
        sys.exit()

# Where the magic happens:
setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],

    # entry_points={
    #     'console_scripts': ['mycli=mymodule:cli'],
    # },
    namespace_packages=[NAMESPACE],
    install_requires=REQUIRED,
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: Microsoft :: Windows'
    ],
    # $ setup.py publish support.
    cmdclass={
        'upload': UploadCommand,
        'rei': ReinstallCommand,
        'uni': UninstallCommand,
    },
)
