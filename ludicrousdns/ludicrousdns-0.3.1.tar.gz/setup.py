import setuptools


with open('README.md') as f:
    readme = f.read()

setuptools.setup(
    name='ludicrousdns',
    version='0.3.1',
    description='A ludicrously speedy DNS resolver',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://gitlab.com/sheddow/ludicrousdns',
    author='Sigurd Kolltveit',
    author_email='sigurd.kolltveit@gmx.com',
    license='MIT',
    packages=['ludicrousdns'],
    package_data={'ludicrousdns': ['data/*.txt']},
    install_requires=[
        'aiodns>=1.1.1',
    ],
    python_requires='>=3.5',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'ludicrousdns = ludicrousdns.cli:main',
        ],
    },
    zip_safe=False)
