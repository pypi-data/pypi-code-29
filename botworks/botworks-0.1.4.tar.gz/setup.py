import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("version.txt", "r") as vf:
    version = vf.readline()

setuptools.setup(
    name="botworks",
    version=version,
    author="William Hanson",
    author_email="42045551+doubleyuhtee@users.noreply.github.com",
    description="Slack bot framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/doubleyuhtee/botworks",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta"
    ),
)