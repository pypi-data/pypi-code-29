import os

from setuptools import find_packages, setup

NAME = 'wagtail_gallery'
DESCRIPTION = 'A simple gallery app built for Wagtail CMS and Django'
URL = 'https://gitlab.com/dfmeyer/wagtail_gallery'
EMAIL = 'me3064@gmail.com'
AUTHOR = 'Daniel F. Meyer'
REQUIRES_PYTHON = '>=3.5'
VERSION = '0.1'
LICENSE = 'MIT'
KEYWORDS = ['Django', 'Wagtail', 'gallery']
PROJECT_URLS = {
    "Bug Tracker": "https://gitlab.com/dfmeyer/wagtail_gallery/issues",
    "Documentation": "https://wagtail-gallery.readthedocs.io/en/latest/",
    "Source Code": "https://gitlab.com/dfmeyer/wagtail_gallery",
}

REQUIRED = ['wagtail', 'django-social-share', ]

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
