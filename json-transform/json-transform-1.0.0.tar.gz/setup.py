import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

with open("requirements.txt", "r") as f:
    install_requirements = [line.strip().replace("\n", "") for line in f.readlines()]


setuptools.setup(
    name="json-transform",
    version="1.0.0",
    author="Peter Morawski",
    author_email="contact@peter-morawski.de",
    keywords="convert python object json",
    description="Convert python objects to JSON documents and vice versa.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/Peter-Morawski/json-transform",
    install_requires=install_requirements,
    test_suite="test_suite",
    py_modules=["jsontransform"],
    license="MIT License",
    classifiers=(
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
        "Topic :: Communications",
        "Topic :: Software Development",
        "Topic :: Utilities",
    ),
)
