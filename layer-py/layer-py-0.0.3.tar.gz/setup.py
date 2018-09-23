from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='layer-py',
      version='0.0.3',
      description='Layer sdk for LRX',
      long_description=readme(),
      long_description_content_type='text/markdown',
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ],
      keywords='layer node protocol cryptography provider identity',
      url='https://github.com/LayerProtocol/layer-py',
      author='NoRestLabs',
      author_email='galen@norestlabs.com',
      license='MIT',
      packages=['layer'],
      install_requires=[
          'markdown',
          'eth-abi == 1.1.1',
          'eth-account == 0.2.3',
          'eth-hash == 0.1.4',
          'eth-keyfile == 0.5.1',
          'eth-keys == 0.2.0b3',
          'eth-rlp == 0.1.2',
          'eth-utils == 1.0.3',
          'web3 == 4.4.1',
          'requests == 2.19.1',
          'cryptography == 2.3.1'
      ],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      entry_points={
          'console_scripts': ['layer-command=layer.command_line:main'],
      },
      include_package_data=True,
      zip_safe=False)
