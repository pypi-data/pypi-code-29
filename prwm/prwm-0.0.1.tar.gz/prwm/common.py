from enum import Enum

class Endianness(Enum): #pylint: disable=too-few-public-methods
    __order__ = 'littleEndian bigEndian'
    littleEndian = 'little'
    bigEndian = 'big'

def get_struct_endianness(endianness):
    return '<' if endianness == Endianness.littleEndian else '>'

def get_prwm_endianness(endianness):
    return 0 if endianness == Endianness.littleEndian else 1
