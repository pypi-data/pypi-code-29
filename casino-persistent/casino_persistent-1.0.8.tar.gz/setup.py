import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="casino_persistent",
    version="1.0.8",
    author="Nam Hoang",
    author_email="namhoang@vncdevs.io",
    description="Casino Persistent",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/htrongnam/casino_persistent",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['SQLAlchemy', 'SQLAlchemy-Utils', 'Flask-SQLAlchemy'],
)
