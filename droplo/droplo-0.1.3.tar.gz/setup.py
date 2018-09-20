import setuptools
import sys
import os
import re
from setuptools import setup
from setuptools.command.install import install

package = 'droplo'

with open('README.md') as f:
    long_description = f.read()


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("^__version__ = ['\"]([^'\"]+)['\"]",
                     init_py, re.MULTILINE).group(1)


# python setup.py tag
if sys.argv[-1] == 'tag':
    print("Pushing tags to GitHub:")
    os.system("git tag -a {0} -m 'version {0}'".format(get_version(package)))
    os.system("git push --tags")
    os.system("git push")
    sys.exit()


class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our version"""
    description = 'verify that the git tag matches our version'

    def run(self):
        version = get_version(package)
        tag = os.getenv('CIRCLE_TAG')

        if tag != version:
            info = "Git tag: {0} does not match the version of this app: {1}".format(
                tag, version
            )
            sys.exit(info)


setup(
    name="droplo",
    version=get_version(package),
    url="https://github.com/droploio/droplo.py",

    author="Droplo Inc",
    author_email="contact@droplo.io",

    description="Official Python SDK for the Droplo content API",
    long_description=long_description,
    long_description_content_type='text/markdown',

    packages=setuptools.find_packages(),

    install_requires=['requests>=2.14.0'],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    test_suite='tests',
    tests_require=[],
    cmdclass={
        'verify': VerifyVersionCommand,
    }
)
