# -*- coding: utf-8 -*- vim: et ts=8 sw=4 sts=4 si tw=79 cc=+8
"""Installer for the visaplan.plone.transform package."""

from setuptools import find_packages
from setuptools import setup

package_name = 'visaplan.plone.transform'
VERSION = (open('VERSION').read().strip()
           # + '.dev1'  # in branches only
           )


# ------------------------------------------- [ for setup_kwargs ... [
long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
])

# see as well --> src/visaplan/plone/transform/configure.zcml,
# MANIFEST.in:
exclude_subpackages = (
        # nun in --> visaplan.kitchen:
        'forks',
        )
exclude_packages = []
for subp in exclude_subpackages:
    exclude_packages.extend([package_name + '.' + subp,
                             package_name + '.' + subp + '.*',
                             ])
packages = find_packages(
            'src',
            exclude=exclude_packages)
# ------------------------------------------- ] ... for setup_kwargs ]

setup_kwargs = dict(
    name=package_name,
    version=VERSION,
    description="HTML transformations for Plone sites",
    long_description=long_description,
    # Get more from https://pypi.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Intended Audience :: Developers",
        "Natural Language :: German",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    # keywords='Python Plone',
    author='Tobias Herp',
    author_email='tobias.herp@visaplan.com',
    url='https://pypi.org/project/visaplan.plone.transform',
    license='GPL version 2',
    packages=packages,
    namespace_packages=[
        'visaplan',
        'visaplan.plone',
        ],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
        'visaplan.kitchen',
        'visaplan.tools',
        'visaplan.plone.infohubs',
        'visaplan.plone.tools',
        'visaplan.plone.pdfexport',
        'visaplan.plone.base',
        # ... further requirements removed
    ],
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
setup(**setup_kwargs)
