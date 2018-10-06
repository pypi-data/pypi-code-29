import setuptools

__author__ = None
__version__ = None

# Reading long description from README.md
with open("README.md", "r") as fh:
    long_description = fh.read()

# Reading __version__ and __author__ from __version__.py
with open("rs3clans/__version__.py") as f:
    exec(f.read())

REQUIRED_INSTALL = []
with open('requirements.txt') as f:
    REQUIRED_INSTALL = f.read().splitlines()

REQUIRED_DEV = []
with open('requirements-dev.txt') as f:
    REQUIRED_DEV = f.read().splitlines()

AUTHOR = __author__
VERSION = __version__
NAME = 'rs3clans'
EMAIL = 'johnvictorfs@gmail.com'
DESCRIPTION = 'A Python 3 module wrapper for RuneScape 3 Clan\'s API'
URL = 'https://github.com/johnvictorfs/rs3clans.py'
REQUIRES_PYTHON = '>=3.6.0'
LICENSE = 'MIT'

setuptools.setup(
    name=NAME,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=REQUIRED_INSTALL,
    setup_requires=REQUIRED_DEV,
    python_requires=REQUIRES_PYTHON,
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    license=LICENSE,
    packages=setuptools.find_packages(exclude=('tests',)),
    url=URL,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7"
    ]
)
