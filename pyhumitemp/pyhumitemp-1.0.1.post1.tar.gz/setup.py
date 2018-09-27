import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyhumitemp",
    version="1.0.1.post1",
    author="Viharm",
    author_email="viharm@malviya.net",
    description="Script to capture numeric humidity and temperature output from DHT22",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/viharm/pyHumiTemp",
    packages=setuptools.find_packages(),
    keywords='python humidity temperature iot terminal dht22',
    project_urls={
      'Bug Reports': 'https://github.com/viharm/pyHumiTemp/issues',
      'Source': 'https://github.com/viharm/pyHumiTemp',
    },
    classifiers=[
        "Programming Language :: Python",
        "License :: Other/Proprietary License",
        "Operating System :: POSIX",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Natural Language :: English",
        "Topic :: System :: Hardware",
        "Topic :: System :: Monitoring",
        "Topic :: Terminals",
        "Topic :: Utilities",
    ],
)