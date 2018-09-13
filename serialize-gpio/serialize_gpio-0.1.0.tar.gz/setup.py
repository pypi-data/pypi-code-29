import setuptools

with open("Readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="serialize_gpio",
    version="0.1.0",
    author="Pablo Paglilla",
    author_email="pablopaglilla16@gmail.com",
    description="Python library for controlling Raspberry Pi® GPIO Pins through a serializable message protocol.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PabloPaglilla/serialize_gpio",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
    ],
)
