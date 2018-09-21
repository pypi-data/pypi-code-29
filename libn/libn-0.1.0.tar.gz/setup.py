from setuptools import setup, Extension
import sys

eca = []
ela = []
libs = []
macros = []

if '--enable-gpu' in sys.argv:
    sys.argv.remove('--enable-gpu')
    libs = ['OpenCL']
    macros = [('HAVE_CL_CL_H', '1')]
    if sys.platform == 'darwin':
        macros = [('HAVE_OPENCL_OPENCL_H', '1')]
        ela = ['-framework', 'OpenCL']
else:
    libs = ['b2']
    eca = ['-fopenmp']

setup(
    name="libn",
    version='0.1.0',
    packages=['libn'],
    description='Python implementation of NANO-related functions.',
    url='https://github.com/rbw/libn',
    author='rbw',
    author_email='rbw@vault13.org',
    license='MIT',
    python_requires='>=3.5',
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
