from os import path

from setuptools import setup

readme_file_path = path.join(path.abspath(path.dirname(__file__)), 'README.md')
with open(readme_file_path, encoding='utf-8') as readme_file:
    long_description = readme_file.read()

setup(
    name='botox-di',
    version='1.4.3',
    url='https://gitlab.com/lebedev.games/botox-di',
    project_urls={
        'Code': 'https://gitlab.com/lebedev.games/botox-di',
        'Issue tracker': 'https://gitlab.com/lebedev.games/botox-di/issues'
    },
    description='The Botox is a lightweight dependency injection pattern implementation for Python.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Ilya Lebedev',
    author_email='lebedev.games.mail@gmail.com',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    packages=['botox'],
    platforms='any',
    python_requires='>=3.6'
)
