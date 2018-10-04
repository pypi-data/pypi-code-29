from setuptools import setup

# read the contents of your README file
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

requires = [
    "pyhcl>=0.3.00",
    "PyYAML>=3.00"
]

setup(
    name='tf_cop',
    version='0.2.1',
    description='auto terraform review',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ys-tydy/tf_cop',
    author='ys-tydy',
    author_email='',
    license='ys-tydy',
    keywords='terraform hcl review',
    packages=[
        "tf_cop",
    ],
    entry_points={
        "console_scripts": [
            "tfcop=tf_cop.cli:cli"
        ]
    },
    package_data={'tf_cop': ['_default_review_book/*/*.yaml']},
    install_requires=requires,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.6',
    ],
)

# python setup.py sdist
# twine check dist/*
# twine upload dist/*
# pip install -Iv ./dist/tf_cop-0.0.9.tar.gz
