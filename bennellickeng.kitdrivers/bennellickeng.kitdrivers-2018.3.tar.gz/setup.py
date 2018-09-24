from setuptools import setup, find_packages
from os import path

def readme():
    with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
        return f.read()

setup(
    namespace_packages=['bennellickeng'],
    name='bennellickeng.kitdrivers',
    version='2018.3',
    description='Bennellick Engineering Kit Drivers',
    long_description=readme(),
    long_description_content_type="text/markdown",
    url='https://bitbucket.org/bennellickeng/kit-drivers/',
    author='Bennellick Engineering Limited',
    author_email='info@bennellick.com',
    license='BSD 3-clause',
    packages=find_packages(),
    entry_points = {
        'console_scripts': [
            'bel-scopegrab=bennellickeng.kitdrivers.usbtmc.scope:grab_CLI',
            'bel-vnagrab=bennellickeng.kitdrivers.prologix.vna:grab_CLI',
            'bel-randsvnagrab=bennellickeng.kitdrivers.rands.vna:grab_CLI',
        ]
    },
    install_requires=[
        'boltons>=17.0.0',
        'numpy',
        'scikit-rf>=0.14.0',
        'matplotlib',
        'pyudev',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
    ],
    zip_safe=False
)
