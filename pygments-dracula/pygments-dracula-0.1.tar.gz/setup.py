#!/usr/bin/python

from setuptools import setup, find_packages

setup(
    name='pygments-dracula',
    version='0.1',
    description='Pygments plugin version of the dracula theme to use with pygmentize.',
    keywords='pygments style dracula',
    license='BSD',
    author='Joseph DelCioppio',
    author_email='joseph.delcioppio@gmail.com',

    url='https://github.com/thedelchop/pygments-dracula-plugin',

    packages = find_packages(),
    install_requires=['pygments >= 1.4'],

    entry_points='''
    [pygments.styles]
    dracula=pygments_dracula:DraculaStyle
    ''',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
