import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ordinalizer",
    version="1.0.0",
    author="Sandor DARGO",
    author_email="sandor.dargo@gmail.com",
    description="A package helping to get numbers as ordinals",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sandordargo/ordinalizer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    test_suite='ordinalizer.tests',
)
