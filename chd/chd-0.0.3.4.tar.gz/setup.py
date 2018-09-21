import codecs

from setuptools import setup, find_packages

import chd


install_requires = [
    'cryptography>=2.3.1',
    'scrapy>=1.5.1'
]


def long_description():
    with codecs.open('README.rst', encoding='utf8') as f:
        return f.read()


setup(
    name='chd',
    version=chd.__version__,
    description=chd.__doc__.strip(),
    long_description=long_description(),
    download_url='https://github.com/mikhailsidorov/chd',
    author=chd.__author__,
    author_email='mikhail.a.sidorov@yandex.com',
    license=chd.__license__,
    url='https://github.com/mikhailsidorov/chd',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'chd = chd.__main__:main',
        ],
    },
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Environment :: Console',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Topic :: Education',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Terminals',
        'Topic :: Utilities'
    ],
)
