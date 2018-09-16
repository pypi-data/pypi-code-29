import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lasagna",
    version="0.0.1",
    author="Neverik",
    author_email="adminr@neverik.com",
    description="A Python web framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/lasagna",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
