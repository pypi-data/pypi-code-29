from setuptools import setup, find_packages

import si
version = si.__version__

setup(
    name='si-api-python-client',
    description='Simple Intelligence python api client',
    long_description='Simple Intelligence python api client',
    # long_description=open('README.md').read(),
    version=version,
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests", "examples"]),
    url='https://bitbucket.com/simpleintelligence/si-api-python-client',
    license='MIT',
    author='Simple Intelligence Inc.',
    author_email='dev@simpleintelligence.com',
    install_requires=[
        'requests==2.19.1',
        'requests-toolbelt==0.8.0'
    ]
)