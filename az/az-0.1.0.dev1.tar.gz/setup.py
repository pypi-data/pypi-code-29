from setuptools import setup, find_packages

from az import __version__

long_description = open('README.md').read()

setup(
    name='az',
    version=__version__,
    description='AZ - simple command line tools',
    author='Yehuda Deutsch',
    author_email='yeh@uda.co.il',

    license='MIT',
    url='https://gitlab.com/uda/az/',
    project_urls={
        'Source': 'https://gitlab.com/uda/az/',
    },
    keywords='cli console',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
    ],
)
