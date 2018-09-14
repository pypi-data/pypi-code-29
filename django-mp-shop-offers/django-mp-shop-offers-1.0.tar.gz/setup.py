
from setuptools import setup, find_packages

version = '1.0'
url = 'https://github.com/pmaigutyak/mp-shop-offers'


setup(
    name='django-mp-shop-offers',
    version=version,
    description='Django shop offers app',
    long_description=open('README.md').read(),
    author='Paul Maigutyak',
    author_email='pmaigutyak@gmail.com',
    url=url,
    download_url='{}/archive/{}.tar.gz'.format(url, version),
    packages=find_packages(),
    include_package_data=True,
    license='MIT'
)
