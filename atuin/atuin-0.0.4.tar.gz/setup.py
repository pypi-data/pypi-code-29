from setuptools import setup, find_packages
import atuin

setup(
    name='atuin',
    version=atuin.__version__,
    description='''A tool for challenge creation and management
                    for CSTEM/Roboplay Competition''',
    author='Steven Herman',
    author_email='stejher@gmail.com',
    license='GPL3',
    packages=find_packages(),
    install_requires=[
        'colorama',
        'mistletoe',
        'pdfkit'
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'atuin = atuin.__main__:main'
        ]
    })
