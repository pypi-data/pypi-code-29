from setuptools import setup, find_packages


def long_description():
    with open("README.md", "r") as readme:
        long_description = readme.read()
    return long_description


setup(
    name="simple_query",
    version="0.0.2",
    author="Matan Noam Shavit",
    description="Query pattern of containers of objects",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/matannoam/SimpleQuery",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
