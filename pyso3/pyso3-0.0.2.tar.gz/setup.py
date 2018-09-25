import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyso3",
    version="0.0.2",
    author="Henry Jacobs",
    author_email="hoj201@gmail.com",
    description="A minimal package for dealing with rotation matrices",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hoj201/pyso3",
    download_url="https://github.com/hoj201/pyso3/archive/v0.0.1.tar.gz",
    packages=setuptools.find_packages(exclude=['test*']),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=["numpy>=1.14"],
    python_requires='>=2.7, <4',
)
