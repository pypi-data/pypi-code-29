import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements/prod.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="blinkistconfig",
    version="0.0.3",
    author="Peter Shoukry",
    author_email="peter@blinkist.com",
    description="Adapter based configuration handler (supports ENV and AWS SSM).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/blinkist/blinkist-config-python",
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    install_requires=requirements,
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
