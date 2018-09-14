import setuptools

with open("README.md", "r") as file_handle:
    long_description = file_handle.read()

setuptools.setup(
    name="insomnia",
    version="0.0.0",
    author="Ahura Jami",
    description="To be updated",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)