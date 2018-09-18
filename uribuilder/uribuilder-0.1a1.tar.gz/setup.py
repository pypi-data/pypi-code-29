from setuptools import setup
from setuptools import find_packages
import uribuilder

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='uribuilder',
    version=uribuilder.__version__,
    author="Fabrizio Destro",
    author_email="destro.fabrizio@gmail.com",
    description="Build URI.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3"
    ],
    url="https://github.com/dexpota/uribuilder",
    packages=find_packages(),
)
