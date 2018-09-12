import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sureal",
    version="0.1.0",
    author="Zhi Li",
    author_email="zli@netflix.com",
    description="Subjective quality scores recovery from noisy measurements.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Netflix/sureal",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS",
    ),
)
