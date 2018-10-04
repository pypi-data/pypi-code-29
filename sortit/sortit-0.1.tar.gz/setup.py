from setuptools import setup
def readme():
    with open('README.md') as f:
        return f.read()

setup(name='sortit',
      version='0.1',
      description='some sorting functions',
      url='http://github.com/storborg/funniest',
      author='Sortmaster X',
      author_email='sortmasterx@sortit.com',
      license='MIT',
      packages=['sorting_nz_style'],
      zip_safe=False)