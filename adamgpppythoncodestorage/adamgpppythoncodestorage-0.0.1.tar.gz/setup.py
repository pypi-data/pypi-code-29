import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='adamgpppythoncodestorage',
    version="0.0.1",
    author="Adam Guła",
    author_email="nacoipoco@gmail.com",
    description="Private Python Code Storage",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adamgpp/python_storage",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
