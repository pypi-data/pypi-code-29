from setuptools import setup, find_packages


setup(
    name='mongoodm',
    version='0.0.1a20',
    url='https://gitlab.com/opentrustee/mongoodm.git',
    author='Daniel Holmes',
    author_email='dan@centricwebestate.com',
    license='Commercial',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='object document mapper mongodb mongo',
    install_requires=['pymongo'],
    tests_require=[
        'mongomock',
        'simplejson'
    ],
    extras_require={
        'dev': [],
        'test': ['mongomock', 'simplejson'],
        'flaskapp': ['Flask'],

    }
)
