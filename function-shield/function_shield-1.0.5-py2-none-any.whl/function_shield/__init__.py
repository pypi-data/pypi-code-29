import json
import os
from ctypes import cdll

dir_path = os.path.dirname(os.path.realpath(__file__))
function_shield_core_path = os.path.join(dir_path, 'lib', 'libfunctionshieldcore.so')
function_shield_core = cdll.LoadLibrary(function_shield_core_path)


def configure(options):
    options_str = json.dumps(options).encode('utf-8')
    function_shield_core.functionshieldcore_configure(options_str)
