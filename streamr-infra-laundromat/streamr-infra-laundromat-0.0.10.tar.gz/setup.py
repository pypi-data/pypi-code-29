import setuptools
import os
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="streamr-infra-laundromat",
    version=os.getenv("RELEASE_VERSION", None),
    author="Streamr",
    author_email="contact@streamr.com",
    description="Library to clean PR infra",
    long_description="",
    url="https://github.com/streamr-dev/streamr-infra-laundromat",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["boto3", "docopt", "docker"],
    entry_points={
        'console_scripts': [
            'laundromat=laundromat.cli:main',
        ],
    }
)
