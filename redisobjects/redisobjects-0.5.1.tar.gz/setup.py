from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

install_requires = ['aioredis', 'shortuuid']
classifiers = [
    'Topic :: Database',
    'Topic :: Database :: Database Engines/Servers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Intended Audience :: Developers',
    'Development Status :: 3 - Alpha',
]

setup(
    name='redisobjects',
    version='0.5.1',
    description='Object-oriented wrapper for aioredis.',
    long_description=long_description,
    author='Jochem Barelds',
    author_email='barelds.jochem@gmail.com',
    license='MIT',
    url='https://gitlab.com/jchmb/redisobjects',
    packages=find_packages(exclude=['tests', 'examples']),
    python_requires='>=3.6',
    install_requires=install_requires,
    include_package_data=True,
    classifiers=classifiers,
)
