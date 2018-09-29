from setuptools import setup, Distribution


class BinaryDistribution(Distribution):
    def has_ext_modules(foo):
        return True


setup(
    name='dualdiff',
    version='0.1.1',
    description='Dual and Hyperdual Number Library',
    packages=['dualdiff'],
    package_data={
        'dualdiff': ['libdual.so', 'libboost_python-py27.so', 'libboost_python-py27.so.1.65.1'],
    },
    distclass=BinaryDistribution
)
