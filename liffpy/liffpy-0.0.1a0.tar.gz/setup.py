# -*- coding:utf-8 -*-
import re
import setuptools

__version__ = ''
with open('liffpy/__about__.py', 'r') as fd:
    reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
    for line in fd:
        m = reg.match(line)
        if m:
            __version__ = m.group(1)
            break


def _requirements():
    with open('requirements.txt', 'r') as fd:
        return [name.strip() for name in fd.readlines()]


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="liffpy",
    version=__version__,
    author="FumiyaOgawa",
    author_email="engineer.fumi@gmail.com",
    description="It is a package that allows you to manipulate LIFF(Line Frontend Framework) by Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='Apache License 2.0',
    url="https://github.com/fantm21/liffpy",
    packages=[
        "liffpy",
    ],
    install_requires=_requirements(),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development",
    ],
)
