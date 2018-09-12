'''
Settings made by django_secrecy app.
https://github.com/Cyxapic/django-secrecy
'''

from .base import *
from .production import *
try:
    from .development import *
except ImportError:
    pass
