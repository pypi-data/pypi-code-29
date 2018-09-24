import os
import re
from setuptools import setup

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('optimalprobes/optimalprobes.py').read(),
    re.M
    ).group(1)

with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")

with open("LICENSE", "rb") as f:
    license_file = f.read().decode("utf-8")

setup(
    name = "cmdline-op-jul14-01", # change this to optimalprobes, PyPI only allows a projectname once
#    download_url = ,
    packages = ["optimalprobes"],
    entry_points = {
        "console_scripts": ['optimalprobes = optimalprobes.optimalprobes:main']
        },
    version = version,
    description = "Python command line application for Optimal Probes.",
    long_description = long_descr,
    author = "Shriyaa Mittal",
    author_email = "mittalshriyaa@gmail.com",
#    maintainer= "",
#   maintainer_email = "",
    url = "http://www.shuklagroup.org/",
    license = license_file,
    )
