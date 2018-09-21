from setuptools import setup


setup(name='harder',
      version='0.0.6',
      description='Reinforcement Learning Utils',
      url='https://github.com/jknthn/harder',
      author='Jeremi Kaczmarczyk',
      author_email='jeremi.kaczmarczyk@gmail.com',
      license='MIT',
      packages=['harder'],
      install_requires=[
          'gym', 'numpy', 'scipy'
      ],
zip_safe=False)