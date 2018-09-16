from setuptools import setup

setup(
    name='GraphWFC',
    version='0.9.0',
	author="lamelizard",
    author_email="florian.drux@rwth-aachen.de",
    description='Colors a networkx (Di)Graph based on patterns extracted from an colored example (Di)Graph',
    packages=['graphwfc',],
    install_requires=[
          'networkx',
      ],
    python_requires=">=3.0",
    url='https://github.com/lamelizard/GraphWaveFunctionCollapse',
    license='MIT',
    long_description=open('README.md').read(),
)