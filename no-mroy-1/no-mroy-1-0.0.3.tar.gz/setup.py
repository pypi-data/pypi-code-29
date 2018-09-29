from setuptools import setup, find_packages
from setuptools.command.install import install
import os, sys
import time

setup(name='no-mroy-1',
    version='0.0.3',
    description='a msg plugins',
    url='https://github.com/Qingluan/no-mroy-1.git',
    author='Qing luan',
    license='MIT',
    include_package_data=True,
    zip_safe=False,
    packages=find_packages(),
    install_requires=[ 'mroylib-min','tornado', 'qtornado','qqbot'],
    entry_points={
        'console_scripts': [
            'Qserver=Reserver.main:main',
            'Qwechat=msgplugins.wechat:StartWeRobot'
        ]
    },

)
