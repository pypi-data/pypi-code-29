from setuptools import find_packages, setup
from innate.__version__ import __version__

setup(
    name="innate",
    version=__version__,
    packages=find_packages(),
    license="MIT License",
    author="Jordan Eremieff",
    author_email="jordan@eremieff.com",
    url="https://github.com/erm/innate/",
    description="Small library for implementing command-line interfaces in Python 3.6+",
)
