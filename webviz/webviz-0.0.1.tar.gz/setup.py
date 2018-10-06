import setuptools

with open('./README.md') as f:
    long_description = f.read()


setuptools.setup(
    name="webviz",
    version="0.0.1",
    author="Equinor ASA",
    author_email="fg_gpl@equinor.com",
    description="Webviz is a static site generator that facilitates automatic reporting and visualization.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Statoil/webviz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: OS Independent",
    ],
    project_urls={
        'Bug Reports': 'https://github.com/Statoil/webviz/issues',
        'Documentation': 'https://webviz.readthedocs.io',
},
)
