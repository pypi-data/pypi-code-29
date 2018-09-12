from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='j2s3-cli',
    version='1.1.1',
    url='https://github.com/jackmahoney/j2s3-cli',
    license='Apache 2.0',
    install_requires=[
        'j2s3==1.0.2',
        'click==6.7'
    ],
    py_modules=['src'],
    entry_points='''
      [console_scripts]
      j2s3=src:cli
    ''',
    description='A cli for publishing Java maven projects to an S3 maven repository',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='jackmahoney',
    author_email='jackmahoney212@gmail.com',
)

