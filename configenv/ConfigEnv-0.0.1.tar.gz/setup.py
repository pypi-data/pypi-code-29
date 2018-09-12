import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='ConfigEnv',
    version='0.0.1',
    author="Théo \"Nydareld\" Guerin",
    author_email="theo.guerin.pro@gmail.com",
    description="Gestionnaire de configuration en json, ini avec overide possible en variable d’environnement",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Nydareld/ConfigEnv",
    packages=setuptools.find_packages(exclude=["tests"]),
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

)
