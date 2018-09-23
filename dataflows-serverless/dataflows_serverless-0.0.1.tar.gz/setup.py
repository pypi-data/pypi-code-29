from setuptools import setup, find_packages
from os import path
from time import time

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

if path.exists("VERSION.txt"):
    # this file can be written by CI tools (e.g. Travis)
    with open("VERSION.txt") as version_file:
        version = version_file.read().strip().strip("v")
else:
    version = str(time())

setup(
    name='dataflows_serverless',
    version=version,
    description='''Use the DataFlows library using serverless concepts.''',
    long_description=long_description,
    url='https://github.com/OriHoch/dataflows-serverless',
    author='''Ori Hoch''',
    author_email='''ori@uumpa.com''',
    license='MIT',
    packages=find_packages(exclude=['examples', 'tests', '.tox']),
    install_requires=['dataflows', 'requests', 'kubernetes', 'jinja2', 'shortuuid'],
    package_data={'dataflows_serverless': ['manifests/*.yaml', 'bin/*.sh']},
    entry_points={
      'console_scripts': [
        'dataflows_serverless_bin = dataflows_serverless.cli:bin',
        'dataflows_serverless_image = dataflows_serverless.cli:image',
      ]
    },
)
