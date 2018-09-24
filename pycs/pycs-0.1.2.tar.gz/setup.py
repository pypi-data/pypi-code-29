from setuptools import setup

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name="pycs",
    version="0.1.2",
    description="Basic data structures and algorithms",
    long_description=long_description,
    url="http://github.com/DanielLenz/pycs",
    author="Daniel Lenz",
    author_email="mail@daniellenz.org",
    license="MIT",
    packages=["pycs", "pycs.datastructures", "pycs.algorithms"],
    zip_safe=False,
)
