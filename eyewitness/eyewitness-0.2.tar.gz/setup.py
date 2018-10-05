from setuptools import setup, find_packages


description = """\
A light weight framework for Object Detection."""

setup(
    name = 'eyewitness',
    version = '0.2' ,
    description = description,
    author = 'Ching-Hua Yang',
    url = 'https://gitlab.com/penolove15/witness',
    classifiers = [
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages()
)
