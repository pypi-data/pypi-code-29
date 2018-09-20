from setuptools import setup, find_packages


setup(name='x-mroy-1047',
    version='0.2.0',
    description='a anayzer package',
    url='https://github.com/Qingluan/.git',
    author='Qing luan',
    license='MIT',
    include_package_data=True,
    zip_safe=False,
    packages=find_packages(),
    install_requires=[ 'mroylib-min>=1.5.1', 'geoip2','fabric3', 'qrcode', 'pillow','image', 'xlwt','xlrd', 'x-mroy-1050', 'x-mroy-1045'],
    entry_points={
        'console_scripts': ['x-web=web.main:main', 'x-web-cmd=web.vultr:main']
    },

)
