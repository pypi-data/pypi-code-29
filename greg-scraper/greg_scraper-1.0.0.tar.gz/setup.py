import setuptools as tools
# IMPORTANT: Do NOT use any packages execpt setuptools, even built-in -> read using open()

lines = []

with open('./requirements.txt', 'r') as reader:
    lines = reader.readlines()

tools.setup(
    name='greg_scraper',
    version='1.0.0',
    author='Greg Pevnev',
    url='https://github.com/GregoryPevnev/python-package',
    description='Web Scraper',

    # Packages(Folders) depoyed into Package(accessible by user) -> Use __init__.py
    packages=['src'],

    # Dependencies(Read from requirements)
    install_requires=lines
)
