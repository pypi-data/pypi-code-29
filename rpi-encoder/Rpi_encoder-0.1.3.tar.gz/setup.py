from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Rpi_encoder',
    version='0.1.3',
    description='High-level interface for the KY040 rotary encoder and switch.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Akex2/Rpi_Encoder',
    author='Alex',
    author_email='schoints@gmail.com',
    keywords='keyes rotary encoder switch A B',
    #py_modules=["pyky040"],
    packages=find_packages(),
    install_requires=['RPi.GPIO'],
    project_urls={
        'Bug Reports': 'https://github.com/Akex2/Rpi_Encoder/issues',
        'Source': 'https://github.com/Akex2/Rpi_Encoder',
    },
)
