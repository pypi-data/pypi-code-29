from setuptools import setup


def long_description():
    with open('./README.md') as file:
        return file.read()


setup(
    name='phraseextractor',
    version='0.5',
    packages=['extractor'],
    url='https://github.com/ppengkkang/phrase-extractor',
    license='MIT',
    author='Peng Yong',
    author_email='ppengkkang16@gmail.com',
    description='A shallow phrase extractor',
    long_description=long_description(),
    long_description_content_type="text/markdown",
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)
