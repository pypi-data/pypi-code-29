import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="strainpycon",
    version="1.0",
    author="Ymir Vigfusson, Lars Ruthotto, Rebecca M. Mitchell, Lauri Mustonen, Xiangxi Gao",
    author_email="ymir.vigfusson@emory.edu",
    description="Strain disambiguation methods for mixed DNA samples",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.ymsir.com/strainpycon/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
