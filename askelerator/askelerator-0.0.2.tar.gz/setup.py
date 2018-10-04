import setuptools

with open('README.md', 'r') as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name='askelerator',
    version='0.0.2',
    author='lfx',
    author_email='fx@zrkf.pw',
    description='A code skeleton generator for accelerated coding.',
    long_description=LONG_DESCRIPTION,
    long_descriptionformat='text/markdown',
    url='https://askelerator.pw',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        "Operating System :: OS Independent",
    ],
    )
