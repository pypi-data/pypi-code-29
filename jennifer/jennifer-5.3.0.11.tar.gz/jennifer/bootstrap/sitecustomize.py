import sys
import os
from os import path


try:
    jennifer = __import__('jennifer')
except ImportError:
    jennifer_path = path.abspath(path.join(path.dirname(__file__), '..', '..'))
    sys.path.append(jennifer_path)
    jennifer = __import__('jennifer')

if os.environ.get('JENNIFER_MASTER_ADDRESS') is not None:
    config = {
        'address': os.environ['JENNIFER_MASTER_ADDRESS'],
        'log_path': os.environ['JENNIFER_LOG_PATH'],
    }
    jennifer.config.init(config)
