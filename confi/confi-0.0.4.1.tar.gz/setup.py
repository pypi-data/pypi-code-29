from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='confi',
    version='0.0.4.1',
    extras_require={
        'test': [
            'pytest',
        ]
    },
    packages=find_packages(),
    long_description=long_description,
    include_package_data=True,
    description='Comfortable python app configuration',
    author='Boris Tseitlin',
    author_email='btseytlin@start.film',
    keywords=['configuration', 'env', 'docker']
)
