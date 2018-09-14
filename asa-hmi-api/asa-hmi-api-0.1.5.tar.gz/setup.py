from setuptools import setup, find_packages

REQUIREMENTS = [
    'setuptools',
    'pyserial',
    'numpy',
]

setup(
    name='asa-hmi-api',
    version='0.1.5',
    description = '',
    long_description='',
    author = 'mickey9910326',
    author_email = 'mickey9910326@gmail.com',
    url='https://gitlab.com/mickey9910326/hmi-api-py',
    license = 'MIT',
    packages=find_packages(),
    zip_safe=False,
    entry_points = {},
    install_requires=REQUIREMENTS
)
