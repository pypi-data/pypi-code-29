from setuptools import setup, find_packages

setup(
    name='sveetoy-cli',
    version=__import__('sveetoy_cli').__version__,
    description=__import__('sveetoy_cli').__doc__,
    long_description=open('README.rst').read(),
    author='David Thenon',
    author_email='sveetch@gmail.com',
    url='https://github.com/sveetch/sveetoy-cli',
    license='MIT',
    packages=find_packages(exclude=['tests*']),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        'six',
        'click>=5.1,<6.0',
        'colorama',
        'colorlog',
        'colour',
    ],
    entry_points={
        'console_scripts': [
            'sveetoy = sveetoy_cli.cli.console_script:cli_frontend',
        ]
    },
    include_package_data=True,
    zip_safe=False
)