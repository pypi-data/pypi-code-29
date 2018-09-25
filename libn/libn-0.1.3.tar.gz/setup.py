import sys
import os
from setuptools import setup, Extension


eca = []
ela = []
libs = []
macros = []


GCC_MIN_MAX = (5, 9)


def find_executable(name):
    path = os.getenv('PATH')
    for p in path.split(os.path.pathsep):
        full_path = os.path.join(p, name)
        if os.path.exists(full_path) and os.access(full_path, os.X_OK):
            return full_path

    return None


def gcc_get_latest():
    # generate list of gcc versions to look for, starting with the most recent
    gcc_versions = ['gcc-{version}'.format(version=i) for i in range(*GCC_MIN_MAX).__reversed__()]

    for gv in gcc_versions:
        gcc_executable = find_executable(gv)
        if gcc_executable:
            return gcc_executable

    return None


os.environ['CC'] = gcc_get_latest() or 'gcc'

if '--enable-gpu' in sys.argv:
    sys.argv.remove('--enable-gpu')
    if sys.platform == 'darwin':
        macros = [('HAVE_OPENCL_OPENCL_H', '1')]
        ela = ['-framework', 'OpenCL']
    else:
        macros = [('HAVE_CL_CL_H', '1')]
        libs = ['OpenCL']
else:
    libs = ['b2', 'omp']
    eca = ['-fopenmp']

setup(
    name="libn",
    version='0.1.3',
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
            extra_compile_args=eca,
            extra_link_args=ela,
            libraries=libs,
            define_macros=macros)
    ])
