#!/usr/bin/python3

from setuptools import setup, find_packages

with open('README.rst') as f:
    long_description = f.read()

setup(
    name="wlint",
    version="0.1.0a",
    package_dir={
        "": "lib"
    },
    packages=find_packages("lib"),

    entry_points={
        "console_scripts": [
            "wlint = wlint.driver:main"
        ],

        "wlint.drivers": [
            "count-words = wlint.count_words:_COUNT_WORDS_COMMAND",
            "punctuation-style = wlint.punctuation_style:_PUNCTUATION_STYLE_COMMAND",
            "list-filter = wlint.list_filter:_LIST_FILTER_COMMAND",
        ],

        "wlint.puririfiers": [
            "text = wlint.purify:_TEXT_PURIFIER",
            "tex = wlint.purify:_TEX_PURIFIER"
        ],

        "wlint.punctuation_rules": [
            "colon = wlint.punctuation.colon:_COLON_RULES",
            "dash = wlint.punctuation.dash:_DASH_RULES",
            "quote = wlint.punctuation.quote:_QUOTE_RULES",
            "range = wlint.punctuation.range:_RANGE_RULES",
            "time = wlint.punctuation.time:_TIME_RULES"
        ]
    },

    package_data={
        "wlint": [
            "share/filter-lists/filter-words.txt",
            "share/filter-lists/thought-words.txt",
            "share/filter-lists/weasel-words.txt"
        ]
    },

    author="Stephen Newell",
    description="Linter tools for writing",
    long_description=long_description,
    long_description_content_type='text/x-rst',
    license="BSD-2",
    url="https://github.com/snewell/wlint",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: BSD License",
        "Topic :: Utilities"
    ]
)
