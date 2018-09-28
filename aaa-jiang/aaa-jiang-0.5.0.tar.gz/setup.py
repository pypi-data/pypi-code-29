from setuptools import setup, find_packages
setup(name='aaa-jiang',
      version='0.5.0',
      description='Scalable Reconstruction Framework.',
      url='https://github.com/threebegetsallthings/aaa.git',
      author='hongjiang',
      author_email='hushangjituan@outlook.com',
      license='Apache',
      packages=find_packages('aa'),
      package_dir={'': 'aa'},
      install_requires=['dxl-learn>0.0.13',
                        'dxl-core',
                        'tensorflow',
                        'doufo'],
      entry_points="""
            [console_scripts]
            srf=srf.api.cli.main:srf
      """,
      zip_safe=False)
