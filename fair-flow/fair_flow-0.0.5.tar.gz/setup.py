import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fair_flow",
    version="0.0.5",
    author="Joe Fair",
    author_email="joe@fairanswers.com",
    description="Simple Workflow Library",
    url="https://fairanswers.com",
    dependency_links=['git+https://github.com/timtadh/dot_tools@master#egg=dot_tools-0.1'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
