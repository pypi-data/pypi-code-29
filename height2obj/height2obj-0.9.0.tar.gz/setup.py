# -*- coding: utf-8 -*-
#
# This file is based on the setup.py example.
# All changes are (c) 2018 Sebastian Georg


from setuptools import setup



with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='height2obj',
    version='0.9.0',
    description='Converts heightmap to 3d mesh.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://bitbucket.org/sgeorg_htw/height2obj',
    author='Sebastian Georg',
    author_email='sebastian.georg@htwsaar.de',
    license='Apache License 2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Multimedia :: Graphics :: 3D Modeling'
    ],
    py_modules=['height2obj'],
    install_requires=['pillow'],
    python_requires='>=3',
    entry_points={
        'console_scripts': ['height2obj=height2obj:main']
    },
    
)