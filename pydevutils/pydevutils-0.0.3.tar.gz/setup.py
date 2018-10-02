import os

from setuptools import setup

PACKAGE = os.path.basename(os.path.dirname(os.path.abspath(__file__))).replace('-', '_')
VERSION="0.0.3"

def get_requirements():
    reqs = []
    try:
        f = file("requirements.txt", "r")
        l = f.readlines()
        for e in l:
            reqs.append(e.strip("\n"))
    except Exception:
        print("Failed to install requirements") 

    return reqs


def get_long_description():
    
    with open("README.md") as f:
        long_description = f.read()
        
    return long_description

setup(
    name=PACKAGE,
    packages=[PACKAGE],
    version=VERSION,
    description='A collection of commands and functions used for building modules and developing python code.',
    long_description=get_long_description(),     
    test_suite='tests',
    install_requires=get_requirements(), 
    include_package_data=True, # include package data under svn source control
    keywords = [],
    ## Sample entry point
    entry_points = {
        'console_scripts': ['bump_package_patch_version = pydevutils.commands:bump_package_patch_version']
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ],
)
