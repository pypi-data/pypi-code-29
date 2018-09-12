# Copyright (c) v87.us Development Team.

import os
import sys
from distutils.core import setup
from setuptools import find_packages

if sys.version_info < (3, 6):
    sys.exit("Sorry, Python < 3.6 is not supported")

os.chdir(os.path.dirname(sys.argv[0]) or ".")
here = os.path.abspath(os.path.dirname(__file__))

ns = {}
with open(os.path.join(here, "refunc/version.txt")) as f:
    exec(f.read(), {}, ns)

setup_args = dict(
    name="refunc",
    version=ns["__version__"],
    description="Python client for refunc",
    author="binzhao",
    license="Apache License Version 2.0",
    url="https://github.com/refunc/py-refunc",
    author_email="wo@zhaob.in",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "refunc = refunc.entry:run_from_file",
            "refunc-dev = refunc.entry:run_from_file_dev",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
    ],
    package_data={"": ["*.*"]},
    include_package_data=True,
    long_description="""\
    Python client for refunc http://refunc.io/
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
