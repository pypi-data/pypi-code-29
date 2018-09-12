#!/usr/bin/env python3
from setuptools import setup
from subprocess import Popen, PIPE

git_describe = ["git", "describe", "--abbrev=0", "--tags"]
version = Popen(git_describe, stdout=PIPE).communicate()[0].decode('utf-8')
setup(
    name='function-shield',
    version=version,
    author='PureSec',
    author_email='support@puresec.io',
    packages=['function_shield'],
    include_package_data=True
)
