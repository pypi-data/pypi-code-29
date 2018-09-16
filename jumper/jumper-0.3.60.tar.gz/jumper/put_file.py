import sys
from time import sleep
import requests

def _put_file(signed_url, data):
    post_res = requests.put(signed_url, data=data)
    post_res.raise_for_status()

filepath = sys.argv[1]
signed_url = sys.argv[2]
with open(filepath, 'rb') as data:
    _put_file(signed_url, data)
    