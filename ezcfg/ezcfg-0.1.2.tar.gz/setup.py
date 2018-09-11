from setuptools import setup, find_packages

setup(
    name='ezcfg',
    version='0.1.2',
    description="Simple python configuration tool",
    long_description=open('README.md').read(),
    author="Yuval Shalev",
    author_email='shalev67@gmail.com',
    url='https://github.com/shalev67/EZconfig',
    packages=find_packages(include=['ezcfg']),
    include_package_data=True,
    license="MIT license",
    keywords='ezcfg',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ]
)
