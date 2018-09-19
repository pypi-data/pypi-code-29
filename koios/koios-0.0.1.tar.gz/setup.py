import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='koios',
    version='0.0.1',
    description='Machine learning in Python!',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/somapaul/koios',
    author='Paul A. Soma, Jr.',
    author_email='somapaul@msu.edu',
    license='MIT',
    packages=setuptools.find_packages(),
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
