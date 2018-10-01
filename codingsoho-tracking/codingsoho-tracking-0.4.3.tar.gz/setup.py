import os
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

from tracking import __version__

setup(
    name='codingsoho-tracking',
    version=__version__,
    packages=find_packages(exclude=['example']),
    include_package_data=True,
    license='MIT License',
    description="Basic visitor tracking and blacklisting for Django",
    long_description=README,
    keywords='django, tracking, visitors',
    url='http://github.com/hordechief/codingsoho-tracking/',
    author='Horce Chief, Josh VanderLinden',
    author_email='hordechief@qq.com',
    maintainer='Horde Chief',
    maintainer_email='hordechief@qq.com',
    install_requires=[
        'django>=1.9,<=1.11',
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: Log Analysis",
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Page Counters",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware",
        "Topic :: Security",
        "Topic :: System :: Monitoring",
        "Topic :: Utilities",
    ]
)
