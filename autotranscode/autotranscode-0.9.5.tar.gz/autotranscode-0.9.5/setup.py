from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name="autotranscode",
    author = "Thane",
    author_email = "thane@gitlab.litbird.de",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3.5",
        "Topic :: Multimedia :: Sound/Audio :: Conversion",
    ],
    description = "A simple, fast and reliable music library transcoder",
    install_requires = [
        "tqdm"
    ],
    license = "GNU GPL v3",
    long_description = readme(),
    long_description_content_type='text/markdown',
    packages = [
        "autotranscode"
    ],
    scripts = [
        "bin/autotranscode"
    ],
    url = "http://gitlab.litbird.de/Thane_DE/AutoTranscode",
    version = "0.9.5",
)

