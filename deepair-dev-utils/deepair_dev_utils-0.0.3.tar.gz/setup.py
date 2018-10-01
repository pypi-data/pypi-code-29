import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="deepair_dev_utils",
    version="0.0.3",
    author="DeepAir Dev",
    author_email="naman@deepair.io",
    description="This is a sub modular package for developer utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/deepair/",
    packages=setuptools.find_packages(),
    classifiers=(
        'Intended Audience :: Developers',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
