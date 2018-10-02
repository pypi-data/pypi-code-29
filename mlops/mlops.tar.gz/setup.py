
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
  name         = 'mlops',
  version      = '0.1.1',
  author       = 'Arata Furukawa',
  author_email = 'info@ornew.net',
  license      = '',
  url          = 'https://github.com/ornew/mlops',
  description  = '',
  classifiers  = [],
  keywords     = '',
  long_description = long_description,
  long_description_content_type = long_description_content_type,
  install_requires = ["protobuf", "ruamel.yaml"],
  packages = ["mlops", "mlops.core"],
  package_dir = {"mlops": ""},
  include_package_data = True,
  scripts = ["tools/mlops"],
)

