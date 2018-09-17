from setuptools import setup
setup(name = 'edbot',
    version = '4.1.979',
    description = 'The Edbot Python API',
    url = 'http://support.ed.bot',
    author = 'Robots in Schools Ltd',
    author_email = 'support@ed.bot',
    packages = [ 'edbot' ],
    install_requires = [ 'ws4py' ],
    zip_safe = False
)