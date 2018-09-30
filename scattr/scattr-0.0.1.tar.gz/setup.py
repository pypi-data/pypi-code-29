import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="scattr",
    version="0.0.1",
    author="Martin Skarzynski",
    author_email="marskar@gmail.com",
    description="Add user-defined methods to Python classes.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/marskar/scattr",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
