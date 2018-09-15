from setuptools import setup
import io

with io.open('README.md', encoding='utf_8') as fp:
    readme = fp.read()

setup(name='mastermind',
      version='0.1',
      long_description=readme,
      long_description_content_type='text/markdown; charset=UTF-8',
      classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
      ],
      description='Play mastermind with python !',
      keywords='mastermind notebook ipywidgets game',
      url='https://github.com/NicolasHoulier/mastermind.git',
      author='Nicolas Houlier',
      author_email='nicolas.houlier@imt-atlantique.net',
      license='MIT',
      install_requires=['ipywidgets>=7.4', 'notebook_toggle_code'],
      packages=['mastermind'],
      package_data={'img': ['*.png'], 'notebooks': ['*.ipynb']},
      include_package_data=True,
      zip_safe=False)
