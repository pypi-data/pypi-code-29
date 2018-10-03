import os

from setuptools import setup, find_packages

NAME = 'wagtail_podcast'
DESCRIPTION = 'A simple podcast app built for Wagtail CMS and Django'
URL = 'https://gitlab.com/dfmeyer/wagtail_podcast'
EMAIL = 'me3064@gmail.com'
AUTHOR = 'Daniel F. Meyer'
REQUIRES_PYTHON = '>=3.5'
VERSION = '0.1'
LICENSE = 'MIT'
KEYWORDS = ['Django', 'Wagtail', 'podcast']
PROJECT_URLS = {
    "Bug Tracker": "https://gitlab.com/dfmeyer/wagtail_podcast/issues",
    "Documentation": "https://wagtail-podcast.readthedocs.io/en/latest/",
    "Source Code": "https://gitlab.com/dfmeyer/wagtail_podcast",
}

REQUIRED = ['wagtail', 'django-social-share', 'mutagen']

PACKAGES = ['wagtail_podcast', 'wagtail_podcast.migrations']

here = os.path.abspath(os.path.dirname(__file__))

try:
    with open('README.rst') as f:
        LONG_DESCRIPTION = f.read()
except FileNotFoundError:
    LONG_DESCRIPTION = DESCRIPTION

setup(
    name=NAME,
    version=VERSION,
    packages=find_packages(),
    include_package_data=True,
    url=URL,
    license=LICENSE,
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    long_description_content_type='text/x-rst',
    python_requires=REQUIRES_PYTHON,
    install_requires=REQUIRED,
    keywords=KEYWORDS,
    project_urls=PROJECT_URLS,
)
