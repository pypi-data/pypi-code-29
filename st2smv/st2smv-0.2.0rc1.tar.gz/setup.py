## Copyright (c) 2016-2018, Blake C. Rawlings.

import glob
import os
import setuptools


def find_package_data(package, glob_pattern):
    globbed = glob.glob(os.sep.join((package, glob_pattern)))
    print(globbed)
    relative = [
        os.sep.join(x.split(os.sep)[1:]) # strip the leading directory
        for x in globbed
    ]
    print(relative)
    return relative


with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
    readme_text = f.read()

setuptools.setup(
    name='st2smv',
    version='0.2.0-rc.1',
    author='Blake C. Rawlings',
    author_email='blakecraw@gmail.com',
    description=(
        'A tool to convert Structured Text PLC code to an SMV model.'
    ),
    license='GPLv3+',
    url='https://pypi.python.org/pypi/st2smv',
    packages=[
        'st2smv',
        'st2smv.plugins',
        'st2smv.plugins.connectivity',
        'st2smv.plugins.irrelevant_logic',
        'st2smv.plugins.predicates',
        'st2smv.plugins.stdlib',
        'st2smv.plugins.varlock',
    ],
    entry_points={
        'console_scripts': ['st2smv=st2smv.__main__:main']
    },
    long_description=readme_text,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Scientific/Engineering',
    ],
    install_requires=['networkx<2.0', 'pyparsing', 'six', 'lark-parser'],
    extras_require={
        'predicates': ['PySMT', 'networkx'],
    },
    package_data={
        'st2smv': [
            'Makefile.run',
            '*.smv',
            '*.lark',
        ] + [
            x for x in find_package_data('st2smv', 'examples/scheduling/*')
            if not x.endswith('~')
        ],
    },
)
