from setuptools import setup, find_packages

print(find_packages())

setup(
    name='mlhub-cli',
    version='0.3.4',
    description='Mlhub CLI',
    url='https://github.com/tsuberim/mlhub',
    author='Matan Tsuberi',
    author_email='tsuberim@gmail.com',
    license='GPL-3.0',
    packages=find_packages(),
    install_requires=[
        'PyInquirer',
        'halo',
        'google-cloud-storage',
    ],
    entry_points = {
        'console_scripts': ['mlhub=mlhub:main'],
    },
    zip_safe=False
)
