import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lycee",
    version="2.6.0",
    author="Vincent MAILLE",
    author_email="vincent.maille@ac-amiens.fr",
    description="Un ensemble de fonctions pour utiliser facilement Python au lycée.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://edupython.tuxfamily.org/",
    packages=setuptools.find_packages(),
	install_requires = ['numpy', 'scipy', 'matplotlib'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: CeCILL-B Free Software License Agreement (CECILL-B)",
        "Operating System :: OS Independent",
    ),
)