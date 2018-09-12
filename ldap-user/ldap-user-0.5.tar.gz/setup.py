#! /usr/bin/env python
# coding: utf-8

#  __author__ = 'meisanggou'

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import sys

if sys.version_info <= (2, 7):
    sys.stderr.write("ERROR: ldap-user requires Python Version 2.7 or above.\n")
    sys.stderr.write("Your Python Version is %s.%s.%s.\n" % sys.version_info[:3])
    sys.exit(1)

name = "ldap-user"
version = "0.5"
url = "https://github.com/meisanggou/ldapuser"
license = "MIT"
author = "meisanggou"
short_description = "use ldap verify user"
long_description = """use ldap verify user"""
keywords = "ldap-user"
install_requires = ["python-ldap", "six"]
entry_points = {'console_scripts': [
    'jy-ldap-config=ldap_user.cli:create_config'
]}

setup(name=name,
      version=version,
      author=author,
      author_email="zhouheng@gene.ac",
      url=url,
      packages=["ldap_user", "ldap_user/util"],
      license=license,
      description=short_description,
      long_description=long_description,
      keywords=keywords,
      install_requires=install_requires,
      entry_points=entry_points
      )
