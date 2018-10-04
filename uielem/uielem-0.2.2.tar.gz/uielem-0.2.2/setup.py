from setuptools import setup, find_packages

setup(name='uielem',
      version='0.2.2',
      description='Wrapper over Tkinter for more Pythonic UI building',
      long_description=open("README.md").read(),
      long_description_content_type="text/markdown",
      url='https://github.com/asrp/uielem',
      author='asrp',
      author_email='asrp@email.com',
      py_modules=find_packages(),
      install_requires=['undoable'],
      keywords='wrapper tkinter pythonic')
