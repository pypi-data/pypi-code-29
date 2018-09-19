import setuptools
import sys
import os
import re

package = 'droplo'


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("^__version__ = ['\"]([^'\"]+)['\"]",
                     init_py, re.MULTILINE).group(1)


# python setup.py publish
if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist upload")
    args = {'version': get_version(package)}
    print("Pushing tags to GitHub:")
    os.system("git tag -a %(version)s -m 'version %(version)s'" % args)
    os.system("git push --tags")
    os.system("git push")
    sys.exit()


setuptools.setup(
    name="droplo",
    version=get_version(package),
    url="https://github.com/droploio/droplo.py",

    author="Droplo Inc",
    author_email="contact@droplo.io",

    description="Official Python SDK for the Droplo content API",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',

    packages=setuptools.find_packages(),

    install_requires=[],

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
    tests_require=[]
)
