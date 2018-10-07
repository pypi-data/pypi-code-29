from setuptools import setup, find_packages

NAME = "httplaceholder"
VERSION = "0.5.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["msrest>=0.2.0"]

setup(
    name=NAME,
    version=VERSION,
    description="httplaceholder",
    author="Duco",
    author_email="mail@ducode.org",
    url="https://github.com/dukeofharen/httplaceholder_python",
    keywords=["Swagger", "httplaceholder"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="A Python library used for communicating with the HttPlaceholder REST API."
)
