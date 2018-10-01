try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='eth_rpc_api',
    version='0.3.10',
    description='Ethereum JSON-RPC client',
    long_description=open('README.rst').read(),
    author='Dead Possum Labs (forked fromn Consensus)',
    author_email='info@consensys.net, d.soldatenko@dplabs.irish ',
    url='https://github.com/sl4mmer/eth_rpc_api',
    packages=['eth_rpc_api'],
    license='MIT',
    install_requires=[
        'ethereum==2.*',
        'requests==2.*',
    ],
)
