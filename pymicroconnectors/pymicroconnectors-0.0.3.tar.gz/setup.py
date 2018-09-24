from distutils.core import setup
from pipenv.project import Project
from pipenv.utils import convert_deps_to_pip
import setuptools

pfile = Project(chdir=False).parsed_pipfile
requirements = convert_deps_to_pip(pfile['packages'], r=False)

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pymicroconnectors',
    version='0.0.3',
    author='Danilo Delizia',
    author_email='ddelizia@gmail.com',
    description="Make connection easier for your microservices",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ddelizia/pymicroconnectors",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,
)