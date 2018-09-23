import codecs
import os

from setuptools import setup, find_packages


__version__ = os.getenv('TAG', '0.1a1')


URL = 'https://bitbucket.org/kiotsystem/remote-sensors-api'


def open_local(paths, mode='r', encoding='utf8'):
    path = os.path.join(
        os.path.join(
            os.path.abspath(os.path.dirname(__file__)),
            *paths
        )
    )

    return codecs.open(path, mode, encoding)


with open_local(['README.md']) as readme:
    long_description = readme.read()


with open_local(['requirements.txt']) as req:
    install_requires = req.read().split("\n")


keywords = ['iot', 'embedded', 'remote_sensors', 'arduino', 'sensors', 'xbee']


setup(
    name='remote_sensors',
    packages=find_packages(exclude=['*.tests', 'tests']),
    version=__version__,
    description='Remote Sensors API framework',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Arnulfo Solis',
    author_email='arnulfojr94@gmail.com',
    url=URL,
    download_url=f'{URL}/get/{__version__}.tar.gz',
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=install_requires,
    keywords=keywords,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
