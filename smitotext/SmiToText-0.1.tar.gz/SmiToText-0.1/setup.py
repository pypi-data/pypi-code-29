import io
import os

from setuptools import setup, find_packages

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))



install_requires = [
    "numpy",
    "mecab-python3",
    "jpype1",
    "nltk",
    "spacy",
    "langdetect",
    "soyspacing",
    "scipy",
    "scikit-learn",
    "python-crfsuite",
    "tensorflow",
    "caret",

]
setup(
    name='SmiToText',
    version='0.001',
    py_modules = ['SmiToText'],
    packages=find_packages(exclude=['tests']),
    install_requires=install_requires,
    include_package_data=True,
    url='https://github.com/jjeaby/SmiToText',
    license='Apache 2.0',
    author='Lee Yong Jin',
    author_email='jjeaby@gmail.com',
    long_description=open('README.md').read(),
    zip_safe=False,
    classifiers      = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)
