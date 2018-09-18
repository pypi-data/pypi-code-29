from setuptools import setup ,find_packages

with open("README.rst", "r") as fh:
    long_description = fh.read()
    
setup(
    name='icdar_tools',
    version='0.0.3',
    description='a pip install icdar_tools',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=['icdar_tools'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    author='mlib_4_you',
    author_email='none.none@gmail.com',
    install_requires = [
        'shapely',
    ],
    keywords=['icdar data tools' ,'East tools']
)
