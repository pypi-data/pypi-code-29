import sys
import codecs
from setuptools import setup, find_packages
import csgrid2unstr


version = csgrid2unstr.__version__
classifiers = [
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Topic :: Scientific/Engineering',
    'Topic :: Software Development',
    'Operating System :: OS Independent',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
]
install_requires = [
    'numpy',
    'setuptools',
    'meshio>=2.1.0'
]


setup(
    name='csgrid2unstr',
    version=version,
    author='Qiao Chen',
    description='Creating and converting cubed-sphere grids to unstructured meshes',
    author_email='benechiao@gmail.com',
    keywords='Math',
    long_description=codecs.open('README.rst', encoding='utf-8').read(),
    url='https://github.com/chiao45/csgrid2unstr',
    packages=find_packages(),
    license='MIT',
    classifiers=classifiers,
    install_requires=install_requires,
    entry_points={'console_scripts': [
        'csgrid2unstr = csgrid2unstr.main:main']},
)
