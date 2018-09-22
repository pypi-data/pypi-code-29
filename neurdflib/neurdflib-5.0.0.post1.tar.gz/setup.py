#!/usr/bin/env python

import os
import re
from setuptools import setup, find_packages

kwargs = {}
kwargs['install_requires'] = [ 'six', 'isodate', 'pyparsing']
kwargs['tests_require'] = ['html5lib', 'networkx', 'SPARQLWrapper']
kwargs['test_suite'] = "nose.collector"
kwargs['extras_require'] = {'sparql': ['SPARQLWrapper'], 'html': ['html5lib']}

def find_version(filename):
    _version_re = re.compile(r'__version__ = "(.*)"')
    for line in open(filename):
        version_match = _version_re.match(line)
        if version_match:
            return version_match.group(1)

version = find_version('rdflib/__init__.py') + '-1'

packages = find_packages(exclude=('examples*', 'test*'))

if os.environ.get('READTHEDOCS', None):
    # if building docs for RTD
    # install examples, to get docstrings
    packages.append("examples")

setup(
    name='neurdflib',
    version=version,
    description="TEMP RELEASE of new features for RDFLib",
    maintainer_email="tgbugs@gmail.com",
    url="https://github.com/tgbugs/rdflib",
    license="BSD-3-Clause",
    platforms=["any"],
    classifiers=[
            "Programming Language :: Python",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "License :: OSI Approved :: BSD License",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Operating System :: OS Independent",
            "Natural Language :: English",
                 ],
    long_description="""\
This is a temporary convenience package for changes waiting to be
merged into the primary rdflib repo.
https://github.com/RDFLib/rdflib/pull/649

Unless you have a specific use case for these changes you should
install upstream rdflib.  https://pypi.org/project/rdflib/
""",
    packages = packages,
    entry_points = {
        'console_scripts': [
            'rdfpipe = rdflib.tools.rdfpipe:main',
            'csv2rdf = rdflib.tools.csv2rdf:main',
            'rdf2dot = rdflib.tools.rdf2dot:main',
            'rdfs2dot = rdflib.tools.rdfs2dot:main',
            'rdfgraphisomorphism = rdflib.tools.graphisomorphism:main',
            ],
        },

    **kwargs
    )
