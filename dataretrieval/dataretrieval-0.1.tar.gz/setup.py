import setuptools

with open("README.md","r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='dataretrieval',
    version='0.1',
    description='Tools for downloading hydrologic and climate data.',
    url='https://github.com/USGS-python/dataretrieval',
    author='Timothy Hodson',
    author_email='thodson@usgs.gov',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=setuptools.find_packages(),
    zip_safe=False
)
