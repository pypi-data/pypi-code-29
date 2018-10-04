import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
        name="world_serpent",
        version="0.0.1",
        author="John Martinez",
        author_name="johndavidmartinez1@gmail.com",
        description="Abstractions to assist the construction of Mongo Aggregations.",
        long_description_content_type="text/markdown",
        url="https://github.com/johndavidmartinez/world-serpent",
        packages=setuptools.find_packages()
)
