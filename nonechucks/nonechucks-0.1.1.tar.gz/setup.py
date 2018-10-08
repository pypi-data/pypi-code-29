from setuptools import setup, find_packages


setup(name='nonechucks',
      version='0.1.1',
      url='https://github.com/msamogh/nonechucks',
      license='MIT',
      author='Amogh Mannekote',
      author_email='msamogh@gmail.com',
      description="""NoneChucks is a library for PyTorch that allows you to drop samples from your data and ensures that your Datasets and Transforms do not fail because of a few samples that are not parseable.""",
      packages=find_packages(),
      long_description=open('README.md').read(),
      zip_safe=False)
