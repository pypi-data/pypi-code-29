import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mentorship",
    version="0.0.1",
    author="Acamica",
    author_email="mentorship@acamica.com",
    description="Never stop teaching",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/acamica/python-mentorship",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

