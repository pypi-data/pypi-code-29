import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='vpxhw_ml',
    version='0.2',
    author='Ray Xu',
    author_email='rxuniverse@google.com',
    description="package for machine learning in vpxhw",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[
      'vpxhw_db_job_locator', 
      'vpxhw_db_data_uploader',
      ],
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)