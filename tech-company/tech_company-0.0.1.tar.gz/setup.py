import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tech_company",
    version="0.0.1",
    author="T Smith",
    author_email="dev@null.org",
    description="A Tech Company",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://example.org",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)