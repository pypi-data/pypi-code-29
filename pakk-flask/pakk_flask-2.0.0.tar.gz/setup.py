"""
Utilities for working with pakk files in a flask web application.
"""
from setuptools import setup, find_packages

with open("readme.md", "r") as readme:
    LONG_DESC = readme.read()

setup(
    name="pakk_flask",
    version="2.0.0",
    author="Tristen Horton",
    author_email="tristen@tristenhorton.com",
    description="Utilities for working with pakk files in a flask web application.",
    long_description=LONG_DESC,
    long_description_content_type="text/markdown",
    url="https://github.com/pakk/pakk-flask",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent"
    ]
)
