from setuptools import setup, find_packages
setup(
    name='dxl-core',
    version='0.1.6',
    description='Core utility library.',
    url='https://github.com/tech-pi/dxcore',
    author='Hong Xiang',
    author_email='hx.hongxiang@gmail.com',
    license='MIT',
    namespace_packages=['dxl'],
    packages=find_packages('src/python'),
    package_dir={'': 'src/python'},
    install_requires=["pyyaml"],
    zip_safe=False)
