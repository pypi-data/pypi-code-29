import setuptools
import package_updater

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="package_updater",
    version=package_updater.__version__,
    author="Laurent Riviere",
    author_email="superlevure.dev@gmail.com",
    description="Update a package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/superlevure/package_updater",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["tqdm", "requests"],
)
