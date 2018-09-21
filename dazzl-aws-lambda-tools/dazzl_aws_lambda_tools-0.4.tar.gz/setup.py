import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='dazzl_aws_lambda_tools',
    version='0.4',
    author='VAILLANT Jeremy',
    author_email='jeremy@dazzl.tv',
    description='Library python for simplify to create lambda function (AWS lambda) and Dazzl API service.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/dazzl-tv/dazzl-aws-lambda-tools.git',
    packages=setuptools.find_packages(),
    install_requires=[
        'requests'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent"
    ]
)
