#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

from setuptools import setup, dist
dist.Distribution(dict(setup_requires = ['bob.extension']))

# load the requirements.txt for additional requirements
from bob.extension.utils import load_requirements, find_packages
install_requires = load_requirements()

setup(

    name = 'bob.hobpad2.chapter19',
    version = open("version.txt").read().rstrip(),
    description = 'Software package to reproduce Evaluation Methodologies for Biometric Presentation Attack Detection chapter of Handbook of Biometric Anti-Spoofing: Presentation Attack Detection 2nd Edition',

    url = 'https://gitlab.idiap.ch/bob/bob.hobpad2.chapter19',
    license = 'GPLv3',
    author = 'Pavel Korshunov',
    author_email = 'pavel.korshunov@idiap.ch',
    keywords = 'bob',

    long_description = open('README.rst').read(),

    packages = find_packages('bob'),
    include_package_data = True,

    install_requires = install_requires,

    entry_points = {
      'console_scripts': [
        'plot_far_frr_pad.py = bob.hobpad2.chapter19.plot_far_frr_pad:main',
        'plot_pad_results.py = bob.hobpad2.chapter19.plot_pad_results:main',
        ],
    },
    classifiers = [
      'Framework :: Bob',
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
      'Natural Language :: English',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
      'Topic :: Scientific/Engineering :: Artificial Intelligence',
      'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
