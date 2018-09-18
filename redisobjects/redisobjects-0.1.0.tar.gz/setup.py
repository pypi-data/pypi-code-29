from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

install_requires = ['aioredis']
classifiers = [
    'Topic :: Database',
    'Topic :: Database :: Database Engines/Servers',
    'License :: OSI Approved :: MIT License',
]

setup(
    name='redisobjects',
    version='0.1.0',
    description='Object-oriented wrapper for aioredis.',
    long_description=long_description,
    author='Jochem Barelds',
    author_email='barelds.jochem@gmail.com',
    url='https://gitlab.com/jchmb/redisobjects',
    packages=find_packages(exclude=['tests', 'examples']),
    install_requires=install_requires,
    include_package_data=True,
    classifiers=classifiers,
)
