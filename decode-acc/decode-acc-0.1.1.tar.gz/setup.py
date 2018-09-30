import setuptools


with open('README.md') as fh:
    long_description = fh.read()


setuptools.setup(
    name='decode-acc',
    version='0.1.1',
    packages=('decode_acc',),
    install_requires=['six'],

    author='Peter Pentchev',
    author_email='roam@ringlet.net',
    description='Incrementally decode bytes into strings and lines',
    long_description=long_description,
    license='BSD-2',
    url='https://gitlab.com/ppentchev/decode-acc/',

    zip_safe=True,
)
