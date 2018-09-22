from setuptools import setup
import os

version = "0.9.0"

def write_version():
    with open(os.path.join("cachelite", "version.py"), 'w') as fp:
        fp.write("version='{VERSION}'".format(VERSION=version))

write_version()
readme = open('README.rst').read()

setup(
    name="cachelite",
    version=version,
    author="yokoshin",
    author_email=os.environ.get('PYPI_EMAIL'),
    url='https://bitbucket.org/yokoshin/cachelite',
    description='a simple multi-process scalable cache implementation',
    long_description=readme,
    packages=['cachelite', ],
    scripts=['scripts/cachelite_ctl.py'],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
