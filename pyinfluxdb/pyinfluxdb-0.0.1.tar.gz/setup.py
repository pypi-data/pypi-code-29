from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="pyinfluxdb",
    version="0.0.1",
    description="A electronic fence package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/muumlover/elecfence",
    author="MUUMLOVER",
    author_email="muumlover@foxmail.com",
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Build Tools',
    ],
    keywords='elecfence geojson map gps',
    packages=find_packages(),
    install_requires=['influxdb'],
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/muumlover/elecfence/issues',
        'Funding': 'https://donate.pypi.org',
        'Say Thanks!': 'http://saythanks.io/to/example',
        'Source': 'https://github.com/muumlover/elecfence/',
    },
)
