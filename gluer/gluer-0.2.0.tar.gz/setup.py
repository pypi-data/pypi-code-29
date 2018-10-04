import os
from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
        name = "gluer",
        version = "0.2.0",
        author = "Kamil Maciejko",
        author_email = "maciejkokamil@gmail.com",
        description = "Dependency injection for python",
        packages = ['gluer'],
        long_description = long_description,
        long_description_content_type="text/markdown",
        python_requires=">=3.6.0",
        setup_requires=["pytest-runner"],
        tests_require=["pytest"],
)
