import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CuraPackageDeployer",
    version="1.0.0",
    author="Chris ter Beke",
    author_email="c.terbeke@ultimaker.com",
    description="Automatically build, deploy and distribute Ultimaker Cura Toolbox packages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ChrisTerBeke/CuraPackageDeployer",
    packages=setuptools.find_packages(),
    install_requires=[
        "requests",
        "bravado"
    ],
    license="AGPL-3.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)
