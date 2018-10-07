import os
import re
import setuptools


module_path = os.path.join(os.path.dirname(__file__), 'findwatt/__init__.py')
version_line = [line for line in open(module_path)
                if line.startswith('__version__')][0]
__version__ = re.findall("\d+\.\d+\.\d+", version_line)[0]


setuptools.setup(
    name="findwatt",
    version=__version__,
    url="https://bitbucket.org/FwPyClassification/findwatt-python",
    author="FindWAtt",
    author_email="luis@findwatt.com",
    description="Python client for FindWAtt's API",
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    py_modules=['findwatt'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        "requests>=2.18.4,<3.0.0",
        "marshmallow>=2.15.2,<3.0.0"
    ],
    classifiers=(
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
