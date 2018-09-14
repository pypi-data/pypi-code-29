import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="webyPy",
    version="0.0.2",
    author="Takshan Gowda",
    author_email="takshan.gowdii@gmail.com",
    description="A light-weight web-design package for Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TakshanGowda/webEpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)