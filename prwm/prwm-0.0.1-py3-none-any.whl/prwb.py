'''
Packed Raw WebGL Bundle

Look: https://github.com/kchapelier/PRWM/issues/3#issuecomment-338490008

Header:
version = 1 byte
endianness = 1 bit of byte, other bits are reserved
number of files = 2 bytes

File block:
identifier = ASCII null terminated string
type: 1 byte, 0 - PRWM
offset: 4 bytes unsigned int
length: 4 bytes unsigned int
'''

from enum import Enum
from collections import namedtuple
import struct

from .common import Endianness, get_struct_endianness, get_prwm_endianness

PrwbFile = namedtuple('PrwbFile', (
    'name',
    'type',
    'file'
))

class FilesType(Enum):
    __order__ = 'PRWM'
    PRWM = 0

class PRWB(object):
    version = 2

    def __init__(self):
        self.files = []

    def add_file(self, file_):
        self.files.append(file_)

    def to_bytes(self, endianness=Endianness.littleEndian):
        ''' Return PRWM v2 binary data '''
        struct_endianness = get_struct_endianness(endianness)
        header = struct.pack(
            struct_endianness + 'BBH',
            self.version,
            get_prwm_endianness(endianness),
            len(self.files)
        )

        header_length = (
            sum((
                len(f.name) + 1
                for f in self.files
            )) +
            len(self.files) * (1 + 4 + 4)
        )
        header_padded_length = (header_length + 3) // 4 * 4
        padding = '\0' * (header_padded_length - header_length)

        offset = header_padded_length + len(header)
        files_header = []
        for f in self.files:
            file_length = len(f.file)
            files_header.append(
                f.name + '\0' +
                struct.pack(
                    struct_endianness + 'BII',
                    f.type.value,
                    offset,
                    file_length
                )
            )
            offset += file_length

        return header + ''.join((
            files_header +
            [padding] +
            [f.file for f in self.files]
        ))
