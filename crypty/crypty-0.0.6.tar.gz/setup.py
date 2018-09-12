import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="crypty",
    version="0.0.6",
    author="Yi Sheng Siow",
    author_email="siowyisheng@gmail.com",
    description="Encrypt and decrypt text easily",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/foreverfighter/crypty",
    packages=setuptools.find_packages(),
    install_requires=[
        'cryptography',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
