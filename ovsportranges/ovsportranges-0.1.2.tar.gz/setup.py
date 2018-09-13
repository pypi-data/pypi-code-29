from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ovsportranges',
    version='0.1.2',
    license='MIT',
    py_modules=['ovsportranges'],
    description='OVS bitwise port/mask ranges',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='James Anderson',
    author_email='janderson@braintrace.com',
    url='https://github.com/Braintrace/ovsportranges',
    keywords='openflow port ranges ovs ofctl',
    python_requires=">2.7",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: OpenStack',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Intended Audience :: Information Technology',
        'Topic :: System :: Networking',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ]
)
