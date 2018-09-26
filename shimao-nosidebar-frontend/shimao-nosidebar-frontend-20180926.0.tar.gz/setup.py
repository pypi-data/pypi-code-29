from setuptools import setup, find_packages

setup(name='shimao-nosidebar-frontend',
      version='20180926.0',
      description='Shimao smart',
      url='https://github.com/home-assistant/home-assistant-polymer',
      author='shi mao fengsh',
      author_email='fengsh998@163.com',
      license='Apache License 2.0',
      packages=find_packages(include=[
          'hass_frontend',
          'hass_frontend_es5',
          'hass_frontend.*',
          'hass_frontend_es5.*'
      ]),
      install_requires=[
          'user-agents==1.1.0',
      ],
      include_package_data=True,
      zip_safe=False)
