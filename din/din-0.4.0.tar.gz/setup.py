"""Setup script for din."""


# [ Imports:Python ]
import pathlib

# [ Imports:Third Party ]
import setuptools


# [ Version ]
def _get_version():
    version_path = pathlib.Path(__file__).parent / 'version.py'
    version_code = version_path.read_text()
    version_state = {}
    # we own this code - executing it is fine
    # pylint: disable=exec-used
    exec(version_code, version_state)  # nosec
    # pylint: enable=exec-used
    return version_state['VERSION']


VERSION = _get_version()


# [ Setup ]
setuptools.setup(
    # package name
    name='din',
    # package version
    version=VERSION,
    # short description
    description='Dunder Mixins',
    # the documentation displayed on pypi
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    # not strictly necessary, but it's a good practice to provide a url if you have one (and you should)
    url='https://gitlab.com/toejough/din',
    # you.  you want attribution, don't you?
    author='toejough',
    # your email.  Or, *an* email.  If you supply an 'author', pypi requires you supply an email.
    author_email='toejough@gmail.com',
    # a license
    license='MIT',
    # "classifiers", for reasons.  Below is adapted from the official docs at https://packaging.python.org/en/latest/distributing.html#classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        # Pick your license as you wish (should match "license" above)
            'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    # keywords.  because classifiers are for serious metadata only?
    keywords="dunder mixin equal equality repr str",
    # what packages are included.
    packages=setuptools.find_packages(),
    # minimum requirements for installation (third-party packages your package uses)
    install_requires=[
        'mypy_extensions',
    ],
    # dependency links besides the package index
    dependency_links=[],
    # extras
    extras_require={
        'test': [
            'bandit==1.4.0',
            'flake8==3.5.0',
            'flake8-aaa==0.3.0',
            'flake8-assertive==1.0.1',
            'flake8-author==1.1.4',
            'flake8-blind-except==0.1.1',
            'flake8-bugbear==18.2.0',
            'flake8-builtins-unleashed==1.3.1',
            'flake8-commas==2.0.0',
            'flake8-comprehensions==1.4.1',
            'flake8-copyright==0.2.0',
            'flake8-debugger==3.1.0',
            'flake8-docstrings==1.3.0',
            'flake8-double-quotes==0.0.1',
            'flake8-expandtab==0.3',
            'flake8-imports==0.1.1',
            'flake8-logging-format==0.4.0',
            'flake8-mutable==1.2.0',
            'flake8-pep257==1.0.5',
            'flake8-pytest==1.3',
            'flake8-self==0.2.2',
            'flake8-single-quotes==0.1.0',
            'flake8-super-call==1.0.0',
            'flake8-tidy-imports==1.1.0',
            'flake8-todo==0.7',
            'mypy==0.610',
            'pylint==2.0.0.dev2',
            'pytest==3.6.3',
            'pytest-cov==2.5.1',
            'vulture==0.28',
        ],
        'dev': [
            'bpython==0.17.1',
        ],
        'dist': [
            'setuptools',
            'wheel',
            'twine',
        ],
    },
    # give your package an executable.
    entry_points={
        # console_script format:
        #   <name>=<package>:<function>
        #   when the user calls 'hello_world' on the cli, 'hello_world/__init__.py::_cli()" will be called.
        'console_scripts': [],
    },
    # if desired, include single files at the top level as packages via `py_modules=[<modules>]`
    py_modules=['din'],
)
