import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dirbpy",
    version="1.1.5",
    author="Marc-Olivier Bouchard",
    author_email="mo.bouchard1997@gmail.com",
    description="This is the new version of dirb in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/marcolivierbouch/dirbpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ],
)
