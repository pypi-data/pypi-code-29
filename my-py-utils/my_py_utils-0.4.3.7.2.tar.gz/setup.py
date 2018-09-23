import setuptools
import my_py_utils

with open("README.md", "r") as fh:
    long_description = fh.read()

pkg_version = my_py_utils.__version__
setuptools.setup(
    name="my_py_utils",
    version=pkg_version,
    author="Mohammed Shameer",
    author_email="reachme@shameer.de",
    description="Package containig my essential definitions",
    url="https://github.com/amdshameer/my_py_utils",
    download_url = 'https://github.com/amdshameer/my_py_utils/archive/'+pkg_version+'.tar.gz',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
)