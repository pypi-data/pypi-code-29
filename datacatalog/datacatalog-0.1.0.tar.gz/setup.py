import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="datacatalog",
    version="0.1.0",
    author="Matthew Vaughn",
    author_email="opensource@sd2e.org",
    description="Python package implementing essential logic for SD2 Data Catalog",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SD2E/python-datacatalog",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
