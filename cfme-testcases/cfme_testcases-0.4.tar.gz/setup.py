# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

with open("README.rst", "rb") as fp:
    LONG_DESCRIPTION = fp.read().decode("utf-8").strip()


setup(
    name="cfme_testcases",
    version="0.4",
    url="https://github.com/mkoura/cfme-testcases",
    description="Create new testrun and upload missing testcases using Polarion Importers",
    long_description=LONG_DESCRIPTION,
    author="Martin Kourim",
    author_email="mkourim@redhat.com",
    license="GPL",
    packages=find_packages(exclude=("tests",)),
    scripts=["cfme_testcases_upload.py"],
    install_requires=["pytest", "dump2polarion>=0.25", "six"],
    keywords=["polarion", "testing"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Testing",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Intended Audience :: Developers",
    ],
    include_package_data=True,
)
