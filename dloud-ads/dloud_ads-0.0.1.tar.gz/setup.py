import setuptools

setuptools.setup(
    name="dloud_ads",
    version="0.0.1",
    url="https://github.com/dataloudlabs/dloud-ads",

    author="Pedro Sousa",
    author_email="pjgs.sousa@gmail.com",

    description="Abstract Data Structures commonly used in CS scenarios. Implemented by Data Loud Labs!",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
