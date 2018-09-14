from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="DarkMute",
    version="0.1.8",
    author="Jessica Ward",
    description="Mute snapcast client playing on raspi3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://git.xhost.io/jess/Dark-Mute",
    packages=find_packages(),
    entry_points={
        'console_scripts': ['darkmute = darkmute:dark_mute'],
    },
    install_requires=[
        "RPi.GPIO==0.6.3",
        "snapcast==2.0.8",
        "zeroconf==0.20.0"
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Topic :: System :: Hardware"
    ]
)
