import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dci_utils",
    version="0.0.22",
    author="Andrew Johnson",
    author_email="andrejohnson@expedia.com",
    description="A set of utilities for DCI jobs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://ewegithub.sb.karmalab.net/EWE/dci-data-dci-utils",
    packages=setuptools.find_packages(),
    install_requires=[
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
