"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""
from setuptools import setup, find_packages

setup(
    name='py-config-parser',
    version='2.0',
    description='Simple python json configuration file parser',
    url='https://github.com/damirazo/py-config-parser',
    author='damirazo',
    author_email='me@damirazo.ru',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Code Generators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='config parser json',
    packages=find_packages(),
)
