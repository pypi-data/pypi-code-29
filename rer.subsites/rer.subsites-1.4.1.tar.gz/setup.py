# -*- coding: utf-8 -*-
"""
This module contains the tool of rer.subsites
"""
import os
from setuptools import setup, find_packages

version = '1.4.1'

setup(name='rer.subsites',
      version=version,
      description="Subsites for ER portals",
      long_description=open("README.rst").read() + "\n" +
      open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          'Framework :: Plone',
          'Framework :: Plone :: 5.0',
          'Framework :: Plone :: 5.1',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License (GPL)',
      ],
      keywords='',
      author='RedTurtle Technology',
      author_email='sviluppoplone@redturtle.it',
      url='https://rersvn.ente.regione.emr.it/svn/plone/prodotti/rer.subsites/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['rer', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'plone.directives.form',
                        'plone.api',
                        ],
      extras_require={
          'test': [
              'plone.app.testing',
              'plone.testing',
              'plone.app.contenttypes',
              'plone.app.robotframework[debug]',
              'unittest2',
          ]
      },
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
