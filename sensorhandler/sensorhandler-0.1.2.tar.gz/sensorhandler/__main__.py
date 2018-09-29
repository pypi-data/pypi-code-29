import os
import sys
import __init__ as sensorhandler

usage = 'Usage: python {} [config_file_path]'.format(__file__)

# config file
if len(sys.argv) > 1:
  configfilepath = sys.argv[1]
else:
  configfilepath = os.getcwd()+'/config.toml'

sensorhandler.read(configfilepath)