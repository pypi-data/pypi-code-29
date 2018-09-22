import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="xipctl",
    scripts=["xipctl"],
    version="0.1.1",
    author="Rodolfo Castillo Mateluna",
    author_email="rodolfocastillomateluna@gmail.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    install_requires=['sndr'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
