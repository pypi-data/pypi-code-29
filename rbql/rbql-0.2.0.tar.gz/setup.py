"""setup.py: setuptools control."""
 
import re
from setuptools import setup
 
 
version = re.search( "^__version__\s*=\s*'(.*)'", open('rbql/rbql.py').read(), re.M).group(1)
 
 
with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")
 
 
setup(
    name = "rbql",
    packages = ["rbql"],
    entry_points = {
        "console_scripts": ['rbql-py = rbql.rbql_main:main']
        },
    version = version,
    description = "Rainbow Query Language",
    long_description = long_descr,
    long_description_content_type = 'text/markdown',
    author = "Dmitry Ignatovich",
    author_email = "mechatroner@yandex.ru",
    url = "https://rbql.org",
    include_package_data = True
    )
