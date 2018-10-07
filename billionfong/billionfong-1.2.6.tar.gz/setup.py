import setuptools

with open("README.rst", "r") as readMe:
    long_description = readMe.read()

setuptools.setup(
    name="billionfong",
    version="1.2.6",
    author="Billy Fong",
    author_email="billionfong@billionfong.com",
    description="Welcome to billionfong's playground",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://www.billionfong.com/",
    download_url="https://github.com/billionfong/Python_Package",
    packages=setuptools.find_packages(),
)
