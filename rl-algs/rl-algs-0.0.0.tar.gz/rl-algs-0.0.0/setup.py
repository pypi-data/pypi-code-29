from setuptools import setup, find_packages

setup(name='rl-algs',
      py_modules=['rl_algs'],
      install_requires=[
          'scipy',
          'tqdm',
          'joblib',
      ]
)
