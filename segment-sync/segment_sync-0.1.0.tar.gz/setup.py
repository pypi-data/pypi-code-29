from setuptools import setup, find_packages

setup(
    name='segment_sync',
    description='Simple GUI tool for sync project segments',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'gui_scripts': [
            'segmentsync = segment_sync.main:main',
        ],
    },
    install_requires=[
        'PyQt5',
    ],
    author='Valery',
    author_email='v.agishev@2gis.ru',
    license='Apache2',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: X11 Applications :: Qt',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Utilities'
    ]
)
