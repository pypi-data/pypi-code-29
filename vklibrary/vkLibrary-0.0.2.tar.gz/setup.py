import setuptools

#with open("README.md", "r") as fh:
   # long_description = fh.read()

setuptools.setup(
    name="vkLibrary",
    version="0.0.2",
    author="Dmitry Petukhov",
    author_email="petumit@yandex.ru",
    description="vk library package",
    #long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/petukhovlive/vkLibrary",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
