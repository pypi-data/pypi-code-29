import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simplega",
    version="1.0.0",
    author="Alysson A Costa",
    author_email="alysson.avila.costa@gmail.com",
    description="A simple implementation of Genetic Algorithm",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nu12/simplega",
    packages=['simplega'],
    package_dir={'simplega':
                 'simplega'},
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)