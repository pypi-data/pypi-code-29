# Copyright (c) v87.us Development Team.

import os
import sys
from distutils.core import setup
from setuptools import find_packages

os.chdir(os.path.dirname(sys.argv[0]) or ".")
here = os.path.abspath(os.path.dirname(__file__))

ns = {}
with open(os.path.join(here, "rfctl/version.txt")) as f:
    exec(f.read(), {}, ns)

setup_args = dict(
    name="rfctl",
    version=ns["__version__"],
    description="Refunc cli client",
    author="binzhao",
    license="Apache License Version 2.0",
    url="https://github.com/refunc/py-refunc",
    author_email="wo@zhaob.in",
    packages=find_packages(),
    entry_points={"console_scripts": ["rfctl = rfctl.rfctl:cli"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
    ],
    include_package_data=True,
    long_description="""\
    Python cli for refunc http://refunc.io/
    """,
)

if "setuptools" in sys.modules:
    setup_args["zip_safe"] = False
    setup_args["install_requires"] = install_requires = []

    with open("requirements.txt") as f:
        for line in f.readlines():
            req = line.strip()
            if not req or req.startswith("#") or "://" in req:
                continue
            install_requires.append(req)


def main():
    setup(**setup_args)


if __name__ == "__main__":
    main()
