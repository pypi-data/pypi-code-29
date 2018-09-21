from setuptools import setup

setup(
    name='smart_rename',
    version='1.1',
    packages=['smart_rename'],
    entry_points={
        'console_scripts': [
            'smart-rename=smart_rename.smart_rename:main',
        ]
    },
    install_requires=['prename']
)
