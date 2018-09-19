import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='EasyFlow',
    version='0.1dev2',
    author='Rohit Jain',
    author_email='rohit06nitbpl@gmail.com',
    description='Modular Distributed TensorFlow Framework',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://pypi.python.org/pypi/EasyFlow/',
    packages=setuptools.find_packages(),

    scripts=['bin/test.py'],
    license='LICENSE.txt',
    
    
)
