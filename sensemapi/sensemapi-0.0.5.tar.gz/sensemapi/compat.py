# external modules
import requests
from requests.compat import json as requestsjson
try:
    JSONDecodeError = requestsjson.JSONDecodeError
except AttributeError:
    JSONDecodeError = requestsjson.errors.JSONDecodeError

