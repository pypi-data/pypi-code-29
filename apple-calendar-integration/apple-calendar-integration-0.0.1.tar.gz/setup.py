import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="apple-calendar-integration",
    version="0.0.1",
    author="SoulSoft Inc",
    author_email="admin@soulsoftinc.com",
    description="The ICloud API for events management",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SoulSoft/apple-calendar-integration",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)