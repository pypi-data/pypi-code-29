import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jira-client-py",
    version="0.0.1",
    author="H20Dragon",
    author_email="h20dragon@outlook.com",
    description="Atlassian JIRA client written in Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/jira-client-py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
