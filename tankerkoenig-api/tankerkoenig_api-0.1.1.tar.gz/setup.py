from __future__ import print_function
from setuptools import setup
from setuptools.command.test import test as TestCommand
import io
import os
import sys
import datetime

import tankerkoenig_api

here = os.path.abspath(os.path.dirname(__file__))
__version = datetime.datetime.now().strftime("%Y.%m.%d.%H%M%S")
if "CI_COMMIT_TAG" in os.environ:
    __version = os.environ["CI_COMMIT_TAG"]


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


long_description = read('README.md')


class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        errcode = tox.cmdline(self.test_args)
        sys.exit(errcode)

setup(
    name='tankerkoenig_api',
    version=__version,
    url='https://gitlab.com/smartesthome.blog/libraries/python/tankerkoenig_api',
    license='Apache Software License',
    author='Iulius Gutberlet',
    tests_require=['tox==3.3.0', 'flake8==3.5.0', 'flake8_docstrings==1.3.0'],
    install_requires=['requests==2.19.1'],
    cmdclass={'test': Tox},
    author_email='iulius@sniggle.me',
    description='tankerkoenig API',
    long_description=long_description,
    packages=['tankerkoenig_api'],
    include_package_data=True,
    platforms='any',
    test_suite='tankerkoenig_api.test.test_tankerkoenig',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries'
        ],
    extras_require={
        'testing': ['pytest'],
    }
)
