import setuptools

with open("README.txt", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django_croppic_py3",
    version="0.0.2",
    author="Alex Davies",
    author_email="alex@mooloomedia.com",
    description="A version of the django-croppic module updated to work with django 2+ and Python 3+.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://mooloomedia.com",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)