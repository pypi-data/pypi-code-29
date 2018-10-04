import json
import ujson
import logging

from .store.item import Item

logging.basicConfig(level=logging.INFO)

def patch_json():
    json.__name__ = 'ujson'
    json.dumps = ujson.dumps
    json.loads = ujson.loads
