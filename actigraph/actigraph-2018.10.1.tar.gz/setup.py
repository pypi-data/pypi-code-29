from setuptools import setup

setup(
    name='actigraph',
    version='2018.10.01',
    description='A library to convert raw accelerometer data to ActiGraph-like "counts".',
    url='https://bitbucket.org/atpage/actigraph',
    author='Alex Page',
    author_email='alex.page@rochester.edu',
    license='MIT',
    packages=['actigraph'],
    install_requires=['numpy','scipy>=1.0.0'],
    keywords='ActiGraph accelerometer count',
    zip_safe=False
)
