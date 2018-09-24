import setuptools

setuptools.setup(
    name='release_name_generator',
    version='0.0.1',
    author='Pavel Kolodkin',
    author_email='pavel@kolodkin.com',
    description='To generate milestone name',
    url='https://github.com/smbdsbrain/markov-experiments',
    license='MIT License',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': ['release_name_generator = release_name_generator.main:program.run']
    },
    install_requires=[
        'pyyaml',
        'invoke'
    ]
)
