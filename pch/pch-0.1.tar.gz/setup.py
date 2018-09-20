from setuptools import find_packages
from setuptools import setup


setup(
    name='pch',
    description='Extra hooks for pre-commit.',
    url='https://github.com/saxix/pre-commit-hooks',
    version='0.1',
    author='Stefano Apostolico',
    author_email='s.apostolico@gmail.com',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    packages=find_packages(exclude=('tests*', 'testing*')),
    install_requires=['cfgv', 'pre-commit'],
    entry_points={
        'console_scripts': [
            'check-missed-migrations = pch.check_missed_migrations:main',
            'check-untracked = pch.check_untracked:main',
            'check-env-template = pch.check_env_template:main',
        ],
    },
)
