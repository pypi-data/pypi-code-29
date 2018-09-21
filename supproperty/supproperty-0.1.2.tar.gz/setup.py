from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='supproperty',

    version='0.1.2',

    description='Supremum property',

    long_description=long_description,

    long_description_content_type='text/markdown',

    url='http://ccs.chem.ucl.ac.uk',

    author='Kristof Farkas-Pall',

    requires=['numpy'],

    packages=find_packages(),

    include_package_data=True,

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

