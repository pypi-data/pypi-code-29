from distutils.core import setup
setup(
  name = 'impl',
  packages = ['impl'],
  version = '0.1',
  description = 'LIME-based library for interpretation of local models',
  author = 'Vinicius Araujo',
  author_email = 'vinicius.brandao.araujo@ccc.ufcg.edu.br',
  license='BSD',
  url = 'https://github.com/viniaraujoo/IPML',
  install_requires=[
          'numpy',
          'scipy',
          'scikit-learn>=0.18',
          'scikit-image>=0.12',
          'tensorflow==1.4.0',
          'keras',
          'os',
          'sklearn',
          'lime'
      ],
  keywords = ['interpretable', 'model', 'lime']
)