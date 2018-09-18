# encoding: utf-8

import os
import io
import sys
from setuptools import setup, find_packages, Command
from shutil import rmtree

NAME = 'reelog'
DESCRIPTION = 'python log best practice.'
URL = ''
EMAIL = 'samrui0129@gmail.com'
AUTHOR = 'Sam Rui'
REQUIRES_PYTHON = '>=2.7.0'
VERSION = '1.7'

REQUIRED = [
]

EXTRAS = {
}

here = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION


class UploadCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            print('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        print('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        print('Uploading the package to PyPI via Twine…')
        os.system('twine upload dist/*')

        # print('Pushing git tags…')
        # os.system('git tag v{0}'.format(VERSION))
        # os.system('git push --tags')

        sys.exit()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/x-rst',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    zip_safe=False,
    license='Apache License',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    cmdclass={
        'upload': UploadCommand,
    }
)
