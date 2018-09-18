import setuptools

with open('README.rst', 'r') as f:
    readme = f.read()

with open('version', 'r') as f:
    version = f.read()

if __name__ == '__main__':

    setuptools.setup(
        name='ohmlr',
        version=version,
        description='One-hot multinomial logisitc regression',
        long_description=readme,
        author='Joseph P. McKenna',
        author_email='joepatmckenna@gmail.com',
        url='http://joepatmckenna.github.io/ohmlr',
        download_url='https://pypi.org/project/ohmlr',
        packages=['ohmlr'],
        license='MIT',
        keywords=['inference', 'statistics', 'machine learning'])
