from sys import stdout, version_info
import json
import globals
from Service import Service



class Monitors(object):

  def __init__(self):
    pass

  @staticmethod
  def process (data):
    data_t = data["Type"]
    if data_t == "service":
      Service.process(data)
#        json.dump(data,stdout)


