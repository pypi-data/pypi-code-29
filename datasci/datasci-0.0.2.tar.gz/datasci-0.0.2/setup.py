from setuptools import setup

setup(
    name='datasci',
    version='0.0.2',
    author='Christopher Brown',
    author_email='io@henrian.com',
    url='https://github.com/chbrown/datasci-python',
    description='Data science utilities',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    packages=['datasci'],
    python_requires='>=3.6',
    install_requires=open('requirements.txt').readlines(),
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
        'pytest-cov',
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
        'Topic :: Sociology',
        'Topic :: Text Processing',
    ],
)
