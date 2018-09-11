from .enviaremail import EnviarEmail
from .spark import Spark
from .funcoes import Funcoes

import sys


latest_version = '0.0.55'

if 'stdclasses' in sys.modules:
  print "esta"
  import pkg_resources
  v = pkg_resources.get_distribution("stdclasses").version
  while not v == latest_version:
    
    del sys.modules["stdclasses"]
    !pip install --upgrade --no-cache-dir stdclasses
    !pip install --upgrade --no-cache-dir stdclasses
    import stdclasses
    v = pkg_resources.get_distribution("stdclasses").version
    