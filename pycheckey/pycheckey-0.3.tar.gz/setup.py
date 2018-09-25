import setuptools

import pycheckey


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=pycheckey.__name__,
    version=pycheckey.__version__,
    author=pycheckey.__author__,
    author_email=pycheckey.__email__,
    description=pycheckey.__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=pycheckey.__repository__,
    packages=setuptools.find_packages(exclude=("tests",)),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>3.5.2',
)