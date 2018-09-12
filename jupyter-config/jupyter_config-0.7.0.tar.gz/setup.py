from setuptools import setup
import os

here = os.path.abspath(os.path.dirname(__file__))
name = 'jupyter_config'

version_ns = {}
with open(os.path.join(here, name, '_version.py')) as f:
    exec(f.read(), {}, version_ns)

extras_require = {
    'test': ['pytest']
}
extras_require['dev'] = ['check_manifest'] + extras_require['test']

setup(
    name='jupyter_config',
    packages=['jupyter_config'],
    version=version_ns['__version__'],
    author='M Pacer',
    author_email='mpacer@berkeley.edu',
    url='https://github.com/mpacer/jupyter_config',
    install_requires=[
        "jupyter_core",
        "notebook>=5.3"
        ],
    entry_points={
        'console_scripts':[
            'jupyter-config = jupyter_config.configapp:main'
        ]},
    extras_require=extras_require,
)
