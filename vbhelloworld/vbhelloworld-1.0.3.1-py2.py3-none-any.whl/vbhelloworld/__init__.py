import sys
import yaml
from os.path import expanduser
from os.path import isfile
from os.path import abspath
from os.path import dirname

def handle_file(filepath):
    filex=open( filepath ) 
    conf=filex.read()
    filex.close()
    yamlConf = yaml.load(conf)

    if len(sys.argv) > 1:
        print("%s %s"%( yamlConf['banner'] ,  sys.argv[1]) )
    else:
        print("%s"%( yamlConf['banner'] ) )

def create_file(filepath):
    print("Configuration file %s doesn't exist"%(filepath))
    print("Creating file %s ..."%(filepath))
    f = open(filepath,'w')
    yaml.dump( {"banner":"Hello world create"} , f , default_flow_style=False) 
    f.close()
    
def main(conf_file=''):
    """Entry point for the application script"""
    here = abspath(dirname(__file__))
    print('Current module location %s'%(here) )
    filepath = expanduser('~/.local/etc/helloworld.conf')
    
    if conf_file!='':
        filepath=conf_file

    if isfile(filepath):
        handle_file(filepath)
    else:
        create_file(filepath)
        handle_file(filepath)
    
def add(arg1,arg2):
    """ Add two values arg1 and arg2 """
    return arg1+arg2
