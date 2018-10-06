from setuptools import setup

setup(name='pygeek-stellar',
      version='0.1',
      description='A Python CLI to interact with the Stellar network',
      url='https://github.com/XavierAraujo/pygeek-stellar',
      author='XavierAraujo',
      author_email='xavier.araujo92@gmail.com',
      license='MIT',
      packages=['pygeek_stellar'],
      install_requires=[
          'stellar-base',
      ],
	  scripts=['bin/pygeek-stellar'],
      python_requires='>=3.7',
      zip_safe=False)
