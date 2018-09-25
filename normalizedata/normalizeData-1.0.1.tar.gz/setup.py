from setuptools import setup
def readme():
    with open('README.txt') as f:
        return f.read()
setup(
    name='normalizeData',
    version='1.0.1',
    author='hebbalkarsudhir',
    author_email='hebbalkarsudhir@gmail.com',
    license='AGPL 3.0',
    long_description=readme(),
    include_package_data=True,
    packages=["normalizeData"],
    scripts=["normalizeData/normalizeData.py"],
    keywords=["normalization", "data", "data cleaning", "data normalization"],
    url='https://github.com/sudhir8184/normalizeData',
    zip_safe=False,
    test_suite='nose.collector',
    tests_require=['nose'],
)
