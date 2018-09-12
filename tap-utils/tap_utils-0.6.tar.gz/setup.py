from setuptools import setup

setup(name='tap_utils',
      version='0.6',
      description='TAP utils',
      url='',
      author='TAP',
      author_email='tap8888@gmail.com',
      license='MIT',
      packages=['tap_utils'],
      zip_safe=False,
      install_requires=[
          'pycrypto==2.6.1',
          'boto3==1.7.70',
          'psycopg2'
      ],
    )
