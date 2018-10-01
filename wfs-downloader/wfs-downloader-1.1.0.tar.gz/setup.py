import re

from setuptools import setup, find_packages

# get metadata from module using a regexp
with open('wfs_downloader/__init__.py') as f:
    metadata = dict(re.findall(r'__(.*)__ = [\']([^\']*)[\']', f.read()))

setup(
    name=metadata['title'],
    version=metadata['version'],
    author=metadata['author'],
    author_email=metadata['email'],
    maintainer=metadata['author'],
    maintainer_email=metadata['email'],
    license=metadata['license'],
    description=u'Downloads GML files from a WFS service in a pseudo-paginated way using bounding boxes and combine them again to one file.',
    url='https://github.com/codeforberlin/wfs-downloader',
    packages=find_packages(),
    install_requires=[
        'lxml==3.7.3',
        'PyYAML'
    ],
    classifiers=[],
    entry_points={
        'console_scripts': [
            'wfs-downloader=wfs_downloader.download:main'
        ]
    }
)
