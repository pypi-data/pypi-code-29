from setuptools import setup


setup(
    name="browser-cat",
    version="0.1.1",
    scripts=['bcat'],

    # metadata to display on PyPI
    author="Dhananjay Balan",
    author_email="mail@dbalan.in",
    description="Cat to browser",
    license="BSD",
    keywords="text mua mutt browser cat",
    url="http://github.com/dbalan/browser-cat",
    project_urls={
        "Bug Tracker": "http://github.com/dbalan/browser-cat/issues",
        "Documentation": "http://github.com/dbalan/browser-cat",
        "Source Code": "http://github.com/dbalan/browser-cat",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    long_description="Send stdin to browser, useful when you are on a terminal, and want to render"
    "html. This was written originally to pipe html email from text MUAs like"
    "neomutt",
)
