"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as readme_file:
    readme = readme_file.read()

with open(path.join(here, 'CHANGELOG.md')) as changelog_file:
    changelog = changelog_file.read()

long_description = readme + '\n\n' + changelog

with open(path.join(here, 'convert_and_download', '_version.py')) as version_file:
    exec(version_file.read())

setup(
    name='convert_and_download',
    version=__version__,
    description='Convert and Download Jupyter Notebooks',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/bryanwweber/convert_and_download',
    author='Bryan W. Weber',
    author_email='bryan.w.weber@gmail.com',
    license='BSD-3-Clause',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='jupyter notebook javascript pdf',
    packages=find_packages(),
    install_requires=[
        'thermohw>=0.4,<1.0',
        'notebook>=5.5.0,<6.0',
        'ipython_genutils>=0.2.0,<1.0',
        'pdfrw>=0.4.0,<0.5.0',
    ],
    include_package_data=True,
    data_files=[
        # like `jupyter nbextension install --sys-prefix`
        ("share/jupyter/nbextensions/convert_and_download", [
            "convert_and_download/static/main.js",
        ]),
        # like `jupyter nbextension enable --sys-prefix`
        ("etc/jupyter/nbconfig/tree.d", [
            "jupyter-config/nbconfig/tree.d/convert_and_download.json"
        ]),
        # like `jupyter serverextension enable --sys-prefix`
        ("etc/jupyter/jupyter_notebook_config.d", [
            "jupyter-config/jupyter_notebook_config.d/convert_and_download.json"
        ])
    ],
    python_requires='~=3.6',
    zip_safe=False,
    project_urls={
        'Bug Reports': 'https://github.com/bryanwweber/convert_and_download/issues',
        'Source': 'https://github.com/bryanwweber/convert_and_download/',
    },
)
