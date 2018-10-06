from setuptools import setup, find_packages

setup(name='nnst',

      version='0.0.0.4',

      download_url='https://github.com/jason9693/NNST-Naver-News-for-Standard-and-Technology-Database/archive/0.0.1.tar.gz',

      url='https://github.com/jason9693/NNST-Naver-News-for-Standard-and-Technology-Database',

      license='MIT',

      author='Yang Kichang',

      author_email='ykcha9@gmail.com',

      python_requires = '>=3',

      classifiers=[

          'Development Status :: 4 - Beta',

          'Intended Audience :: Developers',

          'License :: OSI Approved :: MIT License',

          'Programming Language :: Python :: 3.6',

          'Programming Language :: Python :: 3.5',

          'Programming Language :: Python :: 3.4',

      ],

      install_requires=[
        'bs4>=0.0.1',
        'nose>=1.3.7',
        'numpy>=1.15.0',
        'pandas>=0.23.4',
        'requests>=2.19.1',
        'urllib3>=1.23'
      ],

      packages=find_packages(exclude=['csv','example']),

      description = 'Korean News Dataset For ML',

      zip_safe=False,

      )