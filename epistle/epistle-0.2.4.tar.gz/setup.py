from setuptools import setup, find_packages
import epistle

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='epistle',
    version=epistle.__version__,
    license=epistle.__license__,
    author=epistle.__author__,
    description="Note taking with version control",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/msharp/epistle',
    author_email='maxsharples@gmail.com',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'epistle = epistle.cli:epistle',
        ],
    },
    install_requires='click>=6.7',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Topic :: Terminals',
        'Topic :: Text Processing',
        'Topic :: Utilities'
    ],
)
