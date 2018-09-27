from setuptools import setup, Distribution


class BinaryDistribution(Distribution):
    def has_ext_modules(foo):
        return True


setup(
    name='hyperdual',
    version='0.8.1',
    description='HyperDual Number Library',
    packages=['hyperdual'],
    package_data={
        'hyperdual': ['hyperdual.so'],
    },
    install_requires=[
          'boost',
    ],
    distclass=BinaryDistribution
)
