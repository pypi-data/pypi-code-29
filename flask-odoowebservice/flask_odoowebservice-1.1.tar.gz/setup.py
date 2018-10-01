from setuptools import setup,find_packages

setup(
    name='flask_odoowebservice',
    version='1.01',
    url='https://github.com/FranciscoCarbonell/flask-odoowebservice',
    license='MIT',
    author='Francisco Carbonell',
    author_email='francabezo@gmail.com',
    description='odoo web service extension from flask',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=['Flask','pymongo','mongokat','flask-mongokat']
)