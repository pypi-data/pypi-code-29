# -*- coding: utf-8 -*-

import sys
import os
from setuptools import setup, Extension

ext_args = {
    'extra_compile_args': [],
    'extra_link_args': [],
    'libraries': [],
    'define_macros': []
}

GCC_MIN_MAX = (5, 9)  # Look for gcc versions between 5 and 9
POW_GPU = os.environ.pop('USE_GPU', False)  # Enable GPU work generation using OpenCL
LINK_OMP = os.environ.pop('LINK_OMP', False)  # Link with the OMP library (OSX)


def get_gcc():
    """
    Looks in OS PATH env for gcc-{GCC_MIN_MAX}, starting with MAX.

    If no gcc-{VERSION} is found, `None` is returned
    unless...
    os.environ['CC'] is set, then that value is returned.
    """

    path = os.getenv('PATH').split(os.path.pathsep)

    for version in range(*GCC_MIN_MAX).__reversed__():
        f_name = 'gcc-{0}'.format(version)

        for _dir in path:
            full_path = os.path.join(_dir, f_name)
            if os.path.exists(full_path) and os.access(full_path, os.X_OK):
                return f_name

    return None


if sys.platform == 'darwin':
    if POW_GPU:
        ext_args['define_macros'] = [('HAVE_OPENCL_OPENCL_H', '1')]
        ext_args['extra_link_args'] = ['-framework', 'OpenCL']
    else:
        ext_args['libraries'] = ['b2', 'omp'] if LINK_OMP else ['b2']
        ext_args['extra_compile_args'] = ['-fopenmp']
elif sys.platform == 'linux':
    if POW_GPU:
        ext_args['define_macros'] = [('HAVE_CL_CL_H', '1')]
        ext_args['libraries'] = ['OpenCL']
    else:
        ext_args['extra_compile_args'] = ['-fopenmp']
        ext_args['libraries'] = ['b2']
else:
    raise OSError('Unsupported OS platform')

# Use the most recent version of gcc
os.environ['CC'] = os.environ.get('CC', get_gcc())

setup(
    name="libn",
    version='0.1.6',
    packages=['libn'],
    description='Python implementation of NANO-related functions.',
    url='https://github.com/rbw/libn',
    author='rbw',
    author_email='rbw@vault13.org',
    license='MIT',
    python_requires='>=3.6',
    install_requires=['requests'],
    ext_modules=[
        Extension(
            'libn.work',
            sources=['libn/work.c'],
            **ext_args

        )
    ]
)
