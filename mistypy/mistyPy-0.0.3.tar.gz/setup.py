import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mistyPy",
    version="0.0.3",
    author="CP Sridhar",
    author_email="sridhar@mistyrobotics.com",
    description="Python library for Misty. BETA V 0.0.3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MistyCommunity/mistyPy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)