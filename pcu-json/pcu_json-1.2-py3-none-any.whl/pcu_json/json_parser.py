import json
import codecs
import os

from pcu_json.json_configuration import getKeys
from pcu_json.json_configuration import setKeys

def replaceExtension(path, newextension):
    """Replace extension of a path.
    Parameter :
    path -- target path (for example test.json)
    newextension -- the new extension to be added to the path (for example .txt)
    Return :
    newpath -- target path without its original extension, but with new extension (according to the example, test.txt)
    """
    res=os.path.splitext(path) # split path name and extension
    return res[0]+newextension # add new extension to path name

def restrictKeys(file, data, keys):
    """Restrict parsing to values associates with keys set in configuration file.
    Parameter :
    file -- JSON file to parse
    data -- actual parsed data
    """
    restrict=getKeys().splitlines() # get keys 
    if(restrict!=[]): # if there are keys for parsing restriction
        with codecs.open(file, "w", encoding = 'utf-8') as f: # open text file
            for elt in data: # for each element in JSON file
                for r in restrict: # for each restriction key
                    try:
                        line = elt[r] # get value associated to the restriction key
                    except KeyError:
                        pass # if the element has no value for the key, pass
                    line = line.replace("\r\n", " ").replace("\n", " ") # line break standardization
                    f.write(line) # write line in text file 
                    f.write("\n") # write line break in text file
    else:
        with codecs.open(file, "w", encoding = 'utf-8') as f: # open text file
            for elt in data: # for each element in JSON file
                for k in keys : # for each key
                    try:
                        line=elt[k] # get value associated to the key
                    except KeyError:
                        pass # if the element has no value for the key, pass
                    line = line.replace("\r\n", " ").replace("\n", " ") # line break standardization
                    f.write(line) # write line in text file
                    f.write("\n") # write line break in text file
    return file

def JSONParser(file):
    """
    Parse JSON file and create associated text file.
    Parameter :
    file -- JSON file to parse 
    """
    data = [] 
    keys = set() # keys in JSON file
    with codecs.open(file, "r", encoding = 'utf-8') as f: # open JSON file
        for line in f: # for each line in JSON file
            process_line = json.loads(line) # read line
            for ids in process_line.keys(): # for each key
                keys.update([ids]) # update keys
            data.append(process_line) # add processed line to data
    textfile = restrictKeys(replaceExtension(file, '.txt'), data, keys) # create associated text file according to the key restriction parameter
    return textfile

if __name__ == '__main__':
    setKeys("_id\nname_fr")
    textfile = JSONParser("data/test.json")

