import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="imd_handler",
    version="0.0.420",
    author="G to_tha K to tha W",
    author_email="gewatson@digitalglobe.com",
    description="Set of stuff for ingesting, discovery, editing and storing DG IMD files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DigitalGlobe/IMDiddler",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)