import sys
from sys import stdout, version_info
import json
import globals
import Service
from subprocess import Popen, PIPE
import jsonpickle




class Callbacks(object):

  def __init__(self):
    pass

  @staticmethod
  def process (type, operation, data=None):
    for callback in globals.call_backs:
      globals.logger.info("Calling callback " + callback )
      try:
        pipe = Popen(callback, stdin=PIPE, shell=True )
        if data:
          j_object = { "type":type, "operation": operation, "data":  data.__dict__   }
#          j_object = data
          _data = jsonpickle.encode (j_object)
#          _data = json.dumps(j_object)
        else:
          j_object = { "type":type, "operation": operation, "data": {} }
#          j_object = data
          _data = jsonpickle.encode (j_object)
#          _data = json.dumps(j_object)
        pipe.stdin.write(_data.encode('utf-8'))
        pipe.stdin.write( "\n" )
        pipe.stdin.flush()
        pipe.stdin.close()
      except Exception as ex:
        globals.logger.error ("caught error in calling callback " + callback ) 
        globals.logger.error ("ex: " +  str(ex) )
        pass

