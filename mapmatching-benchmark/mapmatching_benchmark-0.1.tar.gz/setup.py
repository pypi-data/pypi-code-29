import setuptools
from setuptools import setup

setup(
	name='mapmatching_benchmark',
	version='0.1',
	description='Map Matching Benchmark',
	author='F.I.D.O.',
	author_email='david.fido.fiedler@gmail.com',
	license='MIT',
	packages=setuptools.find_packages(),
	install_requires=['roadmaptools'],
	package_data={'mapmatching_benchmark.resources': ['*.cfg']}
)
