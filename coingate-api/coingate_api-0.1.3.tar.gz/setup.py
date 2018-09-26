import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()


setuptools.setup(
    name='coingate_api',
    version='0.1.3',
    packages=['coingate_api',],
    install_requires=['requests>=2.10',],
    license='Apache License version 2',
    description='SDK of CoinGate API for Python 3+',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='coingate coingate-api payment merchant',
    author='Alex Shinkevich aka alexshin',
    author_email='alex.shinkevich@gmail.com',
    url='https://github.com/Sociumnet/coingate-api-python',
    download_url='https://github.com/Sociumnet/coingate-api-python/archive/v0.1.3.tar.gz',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Operating System :: OS Independent',
    ]
)
