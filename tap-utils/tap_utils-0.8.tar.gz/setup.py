from setuptools import setup

setup(name='tap_utils',
      version='0.8',
      description='TAP utils',
      url='',
      author='TAP',
      author_email='tap8888@gmail.com',
      license='MIT',
      packages=['tap_utils'],
      zip_safe=False,
      install_requires=[
          'boto3',
          'psycopg2',
          'vaderSentiment==3.2.1'
      ],
    )
