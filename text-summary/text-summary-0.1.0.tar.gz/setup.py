"""wheel setup for Prosper common utilities"""
from codecs import open
import importlib
from os import path, listdir

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

HERE = path.abspath(path.dirname(__file__))

__package_name__ = 'text-summary'
__library_name__ = 'summary'

def get_version(package_name):
    """find __version__ for making package

    Args:
        package_name (str): path to _version.py folder (abspath > relpath)

    Returns:
        str: __version__ value

    """
    module = package_name + '._version'
    package = importlib.import_module(module)

    version = package.__version__

    return version

class PyTest(TestCommand):
    """PyTest cmdclass hook for test-at-buildtime functionality

    http://doc.pytest.org/en/latest/goodpractices.html#manual-integration

    """
    user_options = [
        ('pytest-args=', 'a', 'Arguments to pass to pytest'),
    ]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = [
            'tests',
            '-rx',
            f'--cov={__library_name__}',
            '--cov-report=term-missing',
            '--cov-config=.coveragerc',
        ]

    def run_tests(self):
        import shlex
        import pytest
        pytest_commands = []
        try:
            pytest_commands = shlex.split(self.pytest_args)
        except AttributeError:
            pytest_commands = self.pytest_args
        errno = pytest.main(pytest_commands)
        exit(errno)


setup(
    name=__package_name__,
    author='John Purcell',
    author_email='jpurcell.ee@gmail.com',
    url=f'https://github.com/lockefox/{__package_name__}',
    download_url=f'https://github.com/lockefox/{__package_name__}/tarball/v{get_version(__library_name__)}',
    version=get_version(__library_name__),
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3.6'
    ],
    keywords='nltk summary text article',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['LICENSE', 'README.rst'],
        __library_name__: ['version.txt', 'app.cfg']
    },
    entry_points={
        'console_scripts': [
            f'summarize={__library_name__}.summarize:run_main',
        ]
    },
    python_requires='>=3.6',
    install_requires=[
        'ProsperCommon',
        'plumbum',
        'nltk',
        'newspaper3k',
    ],
    tests_require=[
        'pytest',
        'pytest_cov',
    ],
    extras_require={
        'dev':[
            'sphinx',
            'sphinxcontrib-napoleon',
            'semantic-version',
        ]
    },
    cmdclass={
        'test':PyTest,
    }
)
