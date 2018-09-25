from setuptools import setup
from friendsep import __version__

long_description=""
with open("README.md","r") as fh:
    long_description=fh.read()

setup(
        name="friendsep",
        description='A simple command line tool to watch a random episode of F.R.I.E.N.D.S',
        version=__version__,
        author='VinitraMk',
        author_email='vinitramk@gmail.com',
        long_description=long_description,
        long_description_content="text/markdown",
        url='https://github.com/VinitraMk/friendsep',
        packages=[
            'friendsep'
            ],
        entry_points={
            'console_scripts':[
                'friendsep=friendsep.friendsep:main'
                ]
            },
        classifiers=[
                'Development Status :: 4 - Beta',
                'Intended Audience :: Developers',
                'Operating System :: POSIX',
                'Programming Language :: Python :: 3',
                "License :: OSI Approved :: MIT License",
            ],
        )
