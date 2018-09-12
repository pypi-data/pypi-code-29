from setuptools import setup, find_packages
setup(
    name="LibTextClassification",
    version="1.1",
    packages=find_packages(),
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
        # And include any *.msg files found in the 'hello' package, too:
    },

    # metadata for upload to PyPI
    author="Chong Wang",
    author_email="1147833662@qq.com",
    description="Text Classification",
    license="PSF",
    keywords="Text Classification",
    url="http://example.com/HelloWorld/",
    install_requires=[
        'bs4',
        'gensim',
        'nltk',
        'numpy',
        'tensorflow',
        'tflearn',
    ],
)