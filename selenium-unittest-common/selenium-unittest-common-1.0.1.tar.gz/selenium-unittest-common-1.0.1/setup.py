import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='selenium-unittest-common',
    version='1.0.1',
    author='Yukitaka Maeda',
    author_email='yumaeda@gmail.com',
    description='Python modules for selenium unit test',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/yumaeda/selenium-unittest',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
