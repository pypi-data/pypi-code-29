import ctypes

from dataclasses import dataclass


@dataclass(order=True)
class RemoteSensorsType(object):
    """RemoteSensors Type."""

    raw: bytearray
    word_size: int

    @property
    def value(self):
        raise NotImplementedError('Please implement this method')


@dataclass
class Char(RemoteSensorsType):
    """Char Content"""

    def __str__(self):
        return self.data

    @property
    def value(self):
        return self.data

    @property
    def data(self):
        if self.word_size == 0x01:  # 1 byte
            return self.raw.decode('ascii')
        return self.raw.decode('utf-8')  # fallback to utf-8

    @data.setter
    def data(self, raw_data: bytearray):
        self.raw = raw_data


@dataclass
class Numeric(RemoteSensorsType):
    """Unsigned integer.


        https://docs.python.org/3/library/ctypes.html#fundamental-data-types
    """


@dataclass
class Unsigned(Numeric):
    """Unsigned number."""

    def __str__(self):
        return self.data

    @property
    def value(self):
        return self.data

    @property
    def data(self):
        c_repr = None
        raw = bytearray(self.raw)
        if self.word_size == 0x01:  # is a uint_8
            c_repr = ctypes.c_uint8.from_buffer(raw)
        elif self.word_size == 0x02:  # uint_16
            c_repr = ctypes.c_ushort.from_buffer(raw)
        elif self.word_size == 0x04:  # uint32
            c_repr = ctypes.c_uint.from_buffer(raw)
        elif self.word_size == 0x08:  # uint64
            c_repr = ctypes.c_ulonglong.from_buffer(raw)
        else:
            raise NotImplemented('The Content Type does not match')

        return c_repr.value

    @data.setter
    def data(self, raw: bytearray):
        self.raw = raw


@dataclass
class Signed(Numeric):
    """Signed Number."""

    def __str__(self):
        return self.data

    @property
    def value(self):
        return self.data

    @property
    def data(self):
        raw = bytearray(self.raw)
        if self.word_size == 0x01:  # int_8
            c_repr = ctypes.c_int8.from_buffer(raw)
        elif self.word_size == 0x02:  # int_16
            c_repr = ctypes.c_short.from_buffer(raw)
        elif self.word_size == 0x04:  # int32
            c_repr = ctypes.c_int.from_buffer(raw)
        elif self.word_size == 0x08:  # int64
            c_repr = ctypes.c_longlong.from_buffer(raw)
        else:
            raise NotImplemented('The Content Type does not match')

        return c_repr.value

    @data.setter
    def data(self, raw: bytearray):
        self.raw = raw


@dataclass
class Float(Numeric):

    def __str__(self):
        return self.data

    @property
    def value(self):
        return self.data

    @property
    def data(self):
        raw = bytearray(self.raw)
        return ctypes.c_float.from_buffer(raw).value

    @data.setter
    def data(self, raw: bytearray):
        self.raw = raw


def get(content_type: str, raw: bytearray, word_size: int) -> RemoteSensorsType:
    """Factory for Contents."""
    class_type = None

    if word_size == 0:  # default to empty char
        return Char(raw=bytearray([0x00]), word_size=1)

    if content_type == 'UNSIGNED':
        class_type = Unsigned
    if content_type == 'SIGNED':
        class_type = Signed
    if content_type == 'CHAR':
        class_type = Char
    if content_type == 'FLOAT':
        class_type = Float

    if not class_type:
        raise NotImplemented()
    return class_type(raw=raw, word_size=word_size)
