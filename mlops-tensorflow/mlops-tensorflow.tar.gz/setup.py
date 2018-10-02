
import io
from setuptools import setup, find_packages

readme_file = ''
if readme_file != '':
  with io.open(readme_file, encoding='utf-8') as f:
    long_description = f.read()
    long_description_content_type = 'text/markdown'
else:
  long_description = ''
  long_description_content_type = None

setup(
  name         = 'mlops-tensorflow',
  version      = '0.1.0',
  author       = 'Arata Furukawa',
  author_email = 'info@ornew.net',
  license      = '',
  url          = 'https://github.com/ornew/mlops/driver/tensorflow',
  description  = '',
  classifiers  = [],
  keywords     = '',
  long_description = long_description,
  long_description_content_type = long_description_content_type,
  install_requires = ["tensorflow-hub", "ruamel.yaml"],
  packages = ["mlops.driver.tensorflow", "mlops.driver.tensorflow.v1"],
  package_dir = {"mlops.driver.tensorflow": ""},
  include_package_data = True,
  scripts = [],
)

