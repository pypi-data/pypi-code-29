# Always prefer setuptools over distutils
from setuptools import setup


def readme():
    with open("README.rst") as f:
        return f.read()


setup(
    name="getignore",
    version="2.0.0",
    description="Command line utility to download common .gitignore files",
    long_description=readme(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="github gitignore download",
    url="https://github.com/Jackevansevo/getignore",
    author="Jack Evans",
    author_email="jack@evans.gb.net",
    license="MIT",
    entry_points={"console_scripts": ["getignore=getignore:main"]},
    py_modules=["anyprint"],
)
