import ast
import io
import re

from setuptools import setup

with io.open('README.md', 'rt', encoding="utf8") as f:
    readme = f.read()

_description_re = re.compile(r'description\s+=\s+(?P<description>.*)')

with open('lektor_asciidoctor.py', 'rb') as f:
    description = str(ast.literal_eval(_description_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    author=u'Andres Perez C.',
    author_email='andresperezcera@gmail.com',
    description=description,
    keywords='Lektor plugin static-site blog asciidoc, using Asciidoctor Ruby Gem',
    license='MIT',
    long_description=readme,
    long_description_content_type='text/markdown',
    name='lektor-asciidoctor',
    py_modules=['lektor_asciidoctor'],
    tests_require=['pytest'],
    version='0.1',
    url='https://github.com/andresperezcera/lektor-asciidoctor.git',
    classifiers=[
        'Environment :: Plugins',
        'Environment :: Web Environment',
        'Framework :: Lektor',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'lektor.plugins': [
            'asciidoctor = lektor_asciidoctor:AsciiDoctorPlugin',
        ]
    }
)
