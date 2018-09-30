"""
Utility functions for Python 2.x/3.x compatibility when
handling bytes.
"""

import sys


if sys.version_info[0] < 3:
    def bytes_from_ints(values):
        """Encode a list of integers into bytes using Python 2's chr()."""
        return ''.join([chr(c) for c in values])

    def bytes_from_byte(byte):
        """
        Turn a single byte into a bytes array for Python 2.x.
        """
        return byte
else:
    def bytes_from_ints(values):
        """Encode a list of integers into bytes using Python 3's bytes()."""
        return bytes(values)

    def bytes_from_byte(byte):
        """
        Turn a single byte into a bytes array for Python 3.x.
        """
        return bytes([byte])
