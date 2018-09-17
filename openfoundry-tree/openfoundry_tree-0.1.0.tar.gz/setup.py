import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="openfoundry_tree",
    version="0.1.0",
    author="Keoni Gandall",
    author_email="koeng101@gmail.com",
    description="OpenFoundry's Tree object code.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/koeng/openfoundry-tree",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

