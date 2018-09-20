import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gitswitch",
    version="0.0.1",
    author="Steven Sierra",
    author_email="bizoru@gmail.com",
    description="A small utility to switch different ssh folders",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bizoru/git-switch",
    scripts=['bin/git-switch'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
