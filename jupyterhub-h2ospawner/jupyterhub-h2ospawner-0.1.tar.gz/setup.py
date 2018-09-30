from setuptools import setup

setup(
    name='jupyterhub-h2ospawner',
    version='0.1',
    description='JupyterHub Spawner using H2O based on systemdspawner',
    long_description='See https://github.com/ycysuk/h2ospawner for more info',
    url='https://github.com/ycysuk/h2ospawner',
    author='Chengyi Yang',
    author_email='ycysuk@gmail.com',
    license='3 Clause BSD',
    packages=['h2ospawner'],
    install_requires=[
        'jupyterhub>=0.9',
        'jupyterhub-systemdspawner>=0.11'
    ],
)
