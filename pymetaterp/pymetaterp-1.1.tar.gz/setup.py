from setuptools import setup, find_packages
setup(name='pymetaterp',
      version='1.01',
      description='A python parser that builds python ASTs in 502 lines of python without using modules',
      long_description=open("readme.md").read(),
      long_description_content_type="text/markdown",
      url='https://github.com/asrp/pymetaterp',
      author='asrp',
      author_email='asrp@email.com',
      packages=find_packages(), #['pymetaterp'],
      keywords='parser peg python minimal')
