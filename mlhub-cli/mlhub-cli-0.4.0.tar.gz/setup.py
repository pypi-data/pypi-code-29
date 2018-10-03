from setuptools import setup, find_packages

setup(
    name='mlhub-cli',
    version='0.4.0',
    description='Mlhub CLI',
    url='https://github.com/tsuberim/mlhub',
    author='Matan Tsuberi',
    author_email='tsuberim@gmail.com',
    license='GPL-3.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'PyInquirer==1.0.2',
        'halo==0.0.17',
        'google-cloud-storage==1.12.0'
    ],
    entry_points = {
        'console_scripts': ['mlhub=mlhub:main'],
    },
    zip_safe=False
)
