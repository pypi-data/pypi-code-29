from setuptools import find_packages, setup


setup(
    name="sherlockbikepy",
    version="0.1.3",
    license="GPL3",
    description="Python library to interact with the sherlock.bike API",
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    author="Philipp Schmitt",
    author_email="philipp@schmitt.co",
    url="https://github.com/pschmitt/sherlockbikepy",
    packages=find_packages(),
    install_requires=[
        "requests"
    ]
)
