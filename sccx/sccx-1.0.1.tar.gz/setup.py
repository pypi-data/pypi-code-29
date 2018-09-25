import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sccx",
    version="1.0.1",
    author="Ziyadsk",
    author_email="Ziyadkader@outlook.com",
    description="A Great cheat cheet and a quick reference command line tool",
    url="https://github.com/ziyadsk/scc",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)