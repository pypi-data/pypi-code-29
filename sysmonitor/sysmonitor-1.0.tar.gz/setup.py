#pylint: disable=all
import os
from setuptools import setup, find_packages

# Load release variables
release_file = os.path.join(os.path.dirname(__file__),
                            "sysmonitor", "release.py")
exec(open(release_file, "rb").read())

def requires():
    with open("requirements.txt", "r") as rfile:
        lines = rfile.read().splitlines()
    return lines

setup (
        name="sysmonitor",
        version=version,
        description=description,
        long_description=long_desc,
        url=url,
        packages=find_packages(),
        license=license,
        author=author,
        author_email=author_email,
        classifiers=[c for c in classifiers.split("\n") if c],
        install_requires=requires(),
        python_requires=">=3.5",
        )
