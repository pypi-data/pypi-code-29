import setuptools as tools
# IMPORTANT: Do NOT use any packages execpt setuptools, even built-in -> read using open()

tools.setup(
    name='greg_scraper',
    version='1.0.1',
    author='Greg Pevnev',
    url='https://github.com/GregoryPevnev/python-package',
    description='Web Scraper',

    # Packages(Folders) depoyed into Package(accessible by user) -> Use __init__.py
    packages=['src'],

    # Dependencies(Read from requirements)
    install_requires=[
        'beautifulsoup4==4.6.3',
        'bs4==0.0.1',
        'certifi==2018.8.24',
        'chardet==3.0.4',
        'idna==2.7',
        'requests==2.19.1',
        'urllib3==1.23'
    ]
)
