from setuptools import setup

setup(
    name='gabmap',
    version=__import__('gabmap').__version__,
    url='https://www.gabmap.nl/',
    author='Martijn Wieling, Herbert Kruitbosch, Research and Innovation Support',
    author_email='H.T.Kruitbosch@rug.nl',
    description='Python module with tools to prepare gabmap data. (Currently) Only supports conversion from geojson to gabmap-supported kml. Tested on Python3.6, probably also works in 2.7 and 3.x',
    license='BSD',
    packages=[
        'gabmap',
    ],
    include_package_data=True,
    install_requires=[
        'fastkml>=0.11,<2',
        'shapely>=1.5.17,<2'
    ],
    extras_require={},
    zip_safe=True,
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
