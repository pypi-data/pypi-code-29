import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='taskwarrior-jrnl-hook',
    version='0.1.0',
    url='https://github.com/Hatoris/taskwarrior-jrnl-hook',
    description=(
        'A hook to add started task in taskwarrior to jrnl'
    ),
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    author='Florian Bernard',
    author_email='florianxbernard@gmail.com',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        "Programming Language :: Python :: 3",
    ],
    install_requires=[
        "taskw",
        "babel"
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'taskwarrior_jrnl_hook= taskwarrior_jrnl_hook:cmdline'
        ],
    },
)