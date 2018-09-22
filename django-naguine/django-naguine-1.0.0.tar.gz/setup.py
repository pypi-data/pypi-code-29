"""PyPI Package Configuration."""

from setuptools import find_packages, setup

import naguine


def read(filename):
    """Returns contents of `filename`."""

    with open(filename) as file:
        return file.read()


setup(
    name='django-naguine',
    version=naguine.__version__,
    packages=find_packages(exclude=['tests']),
    python_requires=">=3.6",
    install_requires=['Django>=2.0'],
    author='Cole Carter',
    author_email='coleccarter@gmail.com',
    license='BSD',
    description=naguine.__doc__,
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/colexyz/django-naguine',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ],
)
