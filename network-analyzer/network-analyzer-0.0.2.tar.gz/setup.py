from setuptools import setup
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='network-analyzer',
    version="0.0.2",
    author="Ashutosh Mishra",
    author_email="ashutoshdtu@gmail.com",
    maintainer="Saurabh Shandilya",
    maintainer_email="saurabhshandilya.1991@gmail.com",
    description="Analyze your network traffic",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ashutoshdtu/network-analyzer",
    packages=['network_analyzer', 'rpc_apiserver', 'socketio_server'],
    include_package_data=True,
    install_requires=required,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Framework :: Flask",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Programming Language :: Python :: 2.7",
        "Operating System :: POSIX",
        "Topic :: System :: Monitoring",
        "Topic :: System :: Networking"
    ]
)