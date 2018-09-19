from setuptools import setup

setup(
    name="featuren",
    description="A simple application for managing your features in production.",
    long_description=open('README.md').read(),
    version="0.1",
    url="https://github.com/jairojair/featuren",
    license="MIT",
    author="Jairo Jair",
    author_email="jairojair@gmail.com",
    entry_points={"console_scripts": ["featuren=featuren.cli:cli"]},
    install_requires=[open('requirements.txt').read()],
)
