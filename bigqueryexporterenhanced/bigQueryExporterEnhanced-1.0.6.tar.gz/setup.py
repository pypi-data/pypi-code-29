import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='bigQueryExporterEnhanced',
    version='1.0.6',
    description='Package codes to execute queries on BQ and save to local machine, to BQ table or to GCS.',
    author='Icarus So (enhanced by Jason Tsang)',
    author_email='tsangkinhoi@gmail.com',
    url='https://github.com/tsangkinhoi/bigQueryExporter-enhanced',  # use the URL to the github repo
    keywords=['bigquery', 'local', 'export'],  # arbitrary keywords
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'google-cloud-bigquery==1.*',
        'google-cloud-storage==1.*',
        'pandas',
    ],
)
