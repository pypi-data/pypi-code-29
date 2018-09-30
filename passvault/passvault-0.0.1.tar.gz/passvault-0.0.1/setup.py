import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='passvault',
    version='0.0.1',
    description='Password storing manager',
    long_description=README,
    url='https://github.com/ikrugloff/passvault',
    license='GNU General Public License v3.0',
    keywords=['python', 'vault', 'password'],
    author=['Ilia Kruglov',
            'Rail Zakirov',
            'Leonid Mikhailov',
            'Veronika Korepanova',
            'Daniyar Kaliyev',
            'Nikolai Kotov'],
    include_package_data=True,
    python_requires='>=3.6.5',
    install_requires=[
        'PyQt5==5.11.2',
        'SQLAlchemy==1.2.12',
        'cryptography==2.3.1'
    ],
    entry_points={
        'console_scripts': [
            'passvault = start_script.main:main'
        ]
    },
)
