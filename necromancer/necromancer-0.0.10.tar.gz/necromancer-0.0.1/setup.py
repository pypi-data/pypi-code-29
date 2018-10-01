import setuptools
from necromancer.version import Version


setuptools.setup(
    name='necromancer',
    version=Version('0.0.1').number,
    description='Python Package Boilerplate',
    long_description=open('README.md').read().strip(),
    author='Chris Hayden and Zack Kollar',
    author_email='me@seedyrom.io',
    url='http://github.com/SeedyROM/necromancer',
    py_modules=['necromancer'],
    entry_points={
        'console_scripts': [
            'necro=necromancer.cli.__main__'
        ],
    },
    install_requires=[
        'docopt',
        'toml',
        'jinja2'
    ],
    license='MIT License',
    zip_safe=False,
    keywords='boilerplate generator',
)
