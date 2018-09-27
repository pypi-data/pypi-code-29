import configparser
from inspect import signature

from fyrgo import DataLoader

fallback = signature(DataLoader.__init__).parameters['planet_files_formats'].default

def read_format(filename):
    conf = configparser.ConfigParser()
    conf.read(filename)
    return conf
    
def read_keys(filename, key):
    conf = read_format(filename)
    keys = conf['Planet Files'].get(key).split()
    return keys

# tests ------------------------------------------------------------
def test_format_get():
    conf = read_format(fallback)
    assert(conf['Planet Files'] is not None)

def test_format_read_planet():
    keys = read_keys(fallback, 'planet')
    assert(keys==['output', 'x', 'y', 'vx', 'vy', 'mass', 'time'])

def test_format_read_orbit():
    keys = read_keys(fallback, 'orbit')
    assert(keys==['time', 'e', 'a', 'M', 'V', 'perihelionPA'])

def test_format_read_acc():
    keys = read_keys(fallback, 'acc')
    assert(keys==['time', 'mass', 'color'])
