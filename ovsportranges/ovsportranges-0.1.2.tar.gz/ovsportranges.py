from collections import namedtuple
from math import isnan

"""
    Module used for getting hex port ranges with mask for ovs rules
    
    MIT License

    Copyright (c) 2018 - Braintrace Inc
    
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
"""


class Error(Exception):
    pass


class PortError(Exception):
    """ Exception raised for errors with port input

    Attributes:
        start -- start port that was input by user
        end   -- end port that was input by user
        msg   -- error message
    """
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.msg = "Port numbers must be between 1 and 65535!"


class OvsPorts:
    """
        This class is used to get port ranges for ovs-ofctl rules.
    """
    def __init__(self):
        self.port_range = namedtuple('PortRange', ['port', 'bitmask'])

    def __bitwise_matches(self, start, end):
        """ Function to breakdown port range into bitwise matches with mask
        :param start: port range start number
        :param end: port range end number
        :return: tuple with a list of ranges found and current port
        """
        current_port = start
        bit = 1
        mask = 0xFFFF
        ranges_found = list()

        # Start loop at bit one and find port/mask ranges
        while start & mask:
            if current_port & bit:
                if current_port != mask:
                    ranges_found.append(
                        self.port_range(int(current_port), int(mask))
                    )
                if (current_port + bit) < 65536:
                    current_port += bit
                else:
                    break
            mask &= ~bit
            bit <<= 1

        # Start second loop at last bit found to find port/mask ranges
        while end & ~mask:
            bit >>= 1
            mask |= bit

            if end & bit:
                ranges_found.append(
                    self.port_range(int(current_port), int(mask))
                )
                current_port |= bit

        return ranges_found, current_port

    def get_port_ranges(self, start, end):
        """ Function to get all port/mask ranges between start and end port
        :param start: port range start number
        :param end: port range end number
        :return: list of port/mask ranges
        """
        # Check for invalid port values and raise an error when found
        if type(start) != int or type(end) != int:
            raise ValueError("Port numbers must be integers!")
        if isnan(start) or isnan(end):
            raise PortError(start, end)
        if not start or not end:
            raise PortError(start, end)
        if start > end:
            raise PortError(start, end)
        if start < 0 or end < 0:
            raise PortError(start, end)

        ranges = list()
        current = start
        if end != 65535:
            new_end = end + 1
        else:
            new_end = end

        try:
            while current < new_end:
                matches = self.__bitwise_matches(current, new_end)
                ranges += matches[0]
                current = matches[1]

            return ranges
        except Exception:
            raise


if __name__ == "__main__":
    ovsports = OvsPorts()
    ranges = ovsports.get_port_ranges(1000, 1999)
    for r in ranges:
        print("Port: {}, Bitmask: {}".format(r.port, r.bitmask))
