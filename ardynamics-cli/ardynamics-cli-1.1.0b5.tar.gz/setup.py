"""Packaging settings."""


from codecs import open
from os.path import abspath, dirname, join
from subprocess import call

from setuptools import Command, find_packages, setup

from cli import __version__


this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()


class RunTests(Command):
    """Run all tests."""
    description = 'run tests'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Run all tests!"""
        errno = call(['py.test', '--cov=ardynamics-cli', '--cov-report=term-missing'])
        raise SystemExit(errno)


setup(
    name = 'ardynamics-cli',
    version = __version__,
    description = 'AR Dynamics CLI',
    long_description = long_description,
    url = 'https://ardynamics.eu',
    author = 'Alwin Roosen',
    author_email = 'info@alwinroosen.tech',
    license = 'UNLICENSE',
    classifiers = [
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: Public Domain',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    keywords = 'ardynamics-cli',
    packages = find_packages(exclude=['docs', 'tests*']),
    install_requires = ['docopt', 'boto3', 'mysql-connector-python'],
    extras_require = {
        'test': ['coverage', 'pytest', 'pytest-cov'],
    },
    entry_points = {
        'console_scripts': [
            'ardynamics-cli=cli.cli:main',
            'cli=cli.cli:main',
        ],
    },
    cmdclass = {'test': RunTests},
)