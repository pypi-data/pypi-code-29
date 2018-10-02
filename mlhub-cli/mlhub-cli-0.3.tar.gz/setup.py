from setuptools import setup, find_packages

setup(
    name='mlhub-cli',
    version='0.3',
    description='Mlhub CLI',
    url='https://github.com/tsuberim/mlhub',
    author='Matan Tsuberi',
    author_email='tsuberim@gmail.com',
    license='GPL-3.0',
    packages=find_packages(),
    entry_points = {
        'console_scripts': ['mlhub=mlhub:main'],
    },
    zip_safe=False
)
