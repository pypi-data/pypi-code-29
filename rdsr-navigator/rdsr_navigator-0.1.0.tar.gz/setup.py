import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rdsr_navigator",
    version="0.1.0",
    author="Robert Vorbau",
    author_email="robert.vorbau@sll.se",
    description="Package for extracting data from DICOM RDSR files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    install_requires=['pydicom', 'pandas'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
