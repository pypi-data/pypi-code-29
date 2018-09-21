import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='vpxhw_db_data_uploader',
    version='0.9',
    author='Ray Xu',
    author_email='rxuniverse@google.com',
    description="package for uploading data to vpxhw database",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[
"google-cloud-bigquery==0.24.0",
"google-cloud-storage==1.1.1",
"pandas>=0.20.1",
"mock",
"pytest",
"httplib2==0.10.3",
"matplotlib",
"mysqlclient",
    ],
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)