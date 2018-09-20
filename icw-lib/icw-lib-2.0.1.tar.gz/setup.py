import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="icw-lib",
    version="2.0.1",
    author="Alberto Ocaranza",
    author_email="haneawa.contact@gmail.com",
    description="Instagram data crawler.",
    url="https://github.com/Haneawa/icw-lib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)