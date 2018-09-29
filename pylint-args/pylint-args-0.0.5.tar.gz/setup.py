#!/usr/bin/env python3
import setuptools
import subprocess
import sys

from setuptools.command.test import test as TestCommand


__version__ = '0.0.5'


class TestAndLintCommand(TestCommand):
    description = 'run linters, tests and create a coverage report'
    user_options = []

    def run_tests(self):
        self._run(['scripts/lint.sh'])
        self._run(['py.test', '--cov=pylint_args'])

    def _run(self, command):
        try:
            subprocess.check_call(command)
        except subprocess.CalledProcessError as error:
            print(f'Command "{" ".join(command)}" failed with exit code {error.returncode}')
            sys.exit(error.returncode)


with open('README.md', 'r') as fh:
    long_description = fh.read()


with open('requirements_dev.txt', 'r') as fh:
    test_requirements = [l.strip() for l in fh.readlines() if l.strip() and not l.startswith('#')]


with open('requirements.txt', 'r') as fh:
    requirements = [l.strip() for l in fh.readlines() if l.strip() and not l.startswith('#')]


setuptools.setup(
    name='pylint-args',
    version=__version__,
    author='Nikita Boyarskikh',
    author_email='n02@ya.ru',
    description='Pylint plugin checking order of the passing keyword arguments to the function',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Nikita-Boyarskikh/pylint-args',
    install_requires=requirements,
    tests_require=requirements + test_requirements[1:],
    include_package_data=True,
    cmdclass={'test': TestAndLintCommand},
    license='MIT',
    data_files=[
        ('.', ['requirements.txt', 'requirements_dev.txt']),
    ],
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Natural Language :: Russian',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='pylint plugin keyword order',
)
