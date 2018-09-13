from setuptools import setup, find_packages
from ghostbot import GhostbotProfile

ghostbot_long_description = """
=================================
Ghostbot the UI Testing Framework
=================================

-----------
Information
-----------

- Current Version: {version}
- Latest Release: {release_datetime}
- Official Web Site: [http://metaworks.io/ghostbot/]

------------
Dependencies
------------

""".format(version=GhostbotProfile.version(), release_datetime=GhostbotProfile.release_datetime())

ghostbot_classifiers = [
    "Development Status :: 1 - Planning",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: BSD License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3 :: Only"
]

setup(
    name="ghostbot",
    version=GhostbotProfile.version(),
    description="UI Testing Framework",
    long_desciption=ghostbot_long_description,
    keywords="ui test testing framework automation crawler scraper",
    url="http://metaworks.io/ghostbot/",
    author="ORITA Takemi",
    author_email="orita@metaworks.io",
    license="BSD",
    packages=find_packages(exclude=["bin", "build", "dist", "docs", "ghostbot.egg-info", "tests"]),
    install_requires=["selenium", "bs4", "requests", 'flask', 'docopt', 'pymongo', 'html2text'],
    classifiers=ghostbot_classifiers
)
