#!/usr/bin/env python

# coding=utf-8


##########################################################################################
import json


##########################################################################################
def fn_get_json_from(response):
    try:
        return response.json()
    except NameError:
        return json.loads(response.content)


##########################################################################################
def fn_python_mordanize():
    try:
        input = raw_input
    except NameError:
        pass


##########################################################################################
def is_tool(program):
    import os
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None

##########################################################################################

def fn_check_environment():
    if is_tool('docker') == False:
        print('Docker command line tool is required')
        return False

    #   check osifservice.json file exists




    return True;

##########################################################################################

