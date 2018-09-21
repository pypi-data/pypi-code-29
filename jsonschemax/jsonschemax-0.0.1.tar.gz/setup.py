import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jsonschemax",
    version="0.0.1",
    author="ocavue",
    author_email="ocavue@gmail.com",
    description="An implementation of JSON Schema for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ocavue/jsonschemax",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
