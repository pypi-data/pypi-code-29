#!/usr/bin/env python
"""Test local IPs for network membership.

As a script, determines if any of the local IP addresses are members of the
given network, optionally negating the result (machine is not part of a given 
network). Run with --help for accepted flags.

As a library, provides the following functions:

ip_for_iface(iface): Return the IP address for a given interface, or raise
    OSError (IOError in Python 2.6/2.7).
ifaces_ips(ifaces): Return a list of IP addresses for a given list of 
    interfaces.
in_network(ip, network, prefix): Return True if ip is in network.
from_cidr(): Return (address, prefix) from CIDR string, or raise ValueError.
all_ifaces(): Return a list of all network interfaces on local machine.
"""

from __future__ import print_function

import fcntl
import re
import socket
import struct

RE_cidr = re.compile("^(?P<network>([0-9]{1,3}\.){3}[0-9]{1,3})($|/(?P<prefix>([0-1]?[0-9]?[0-9])|([2][0-4][0-9])|(25[0-5])))$")

def ip_for_iface(iface):
    """Return the IP address associated with an interface.

    :param iface: The interface to query
    :type iface: str
    :return: IP address associated with interface
    :raises: OSError if given interface has no IP address.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', iface[:15].encode("UTF-8"))
        )[20:24])


def ifaces_ips(ifaces):
    """Return a list of IP addresses one for each provided interface name.

    :param ifaces: Iterable of interface names to check.
    :type ifaces: list of str
    :return: List of all local IP addresses
    :rtype: list of [str or None]
    """
    addresses = []
    for iface in ifaces:
        try:
            addresses.append(ip_for_iface(iface))
        except (OSError, IOError): # No IP address assigned
            addresses.append(None)
    return addresses

def in_network(address, network, prefix=32):
    """Return True if address is in network with given network-prefix length.

    :param address: IP address we which to determine the status of
    :param network: The network we wish to test against
    :param prefix: The prefit MSB bitlength (CIDR style) of the network
    :type address: str
    :type network: str
    :type prefix: int
    :return: True if address is in network with netmask prefix
    :rtype: bool
    """
    prefix = (1<<32) - (1<<32>>prefix)
    dec_addr, = struct.unpack('!I', socket.inet_aton(address))
    masked_addr = struct.pack('!I', (dec_addr & prefix))
    dec_network, = struct.unpack('!I', socket.inet_aton(network))
    masked_network = struct.pack('!I', (dec_network & prefix))
    return masked_addr == masked_network
    #return socket.inet_ntoa(masked_addr) == socket.inet_ntoa(masked_network)
    
def from_cidr(cidr):
    """Return network address and prefix from CIDR string.

    :param cidr: CIDR string (e.g. '10.50.3.0/24')
    :type cidr: str
    :return: (address, prefix)
    :rtype: tuple (str, int)
    :raises ValueError: If cidr is not a valid CIDR string
    """
    match = RE_cidr.match(cidr)
    if not match:
        raise ValueError('Invalid CIDR string: {}'.format(cidr))
    vals = match.groupdict()
    if vals['prefix'] == None:
        vals['prefix'] = 32
    return (vals['network'], int(vals['prefix']))

def all_ifaces():
    """Return all network interfaces and their indexes.
    
    :return: List of network interface indexes and names.
    :rtype: list of tuples (int index, str name)
    :raises: OSError on various issues.

    Prefers socket.if_nameindex() where present, but attempts to use the
    libc version of same when the socket library function is not available.
    """
    try:
        return socket.if_nameindex()
    except AttributeError:
        # Support for other operating systems should insert here.
        # For now, we support POSIX/libc implementations. Probably.
        return _libc_if_nameindex()

def _libc_if_nameindex():
    """Return interface indexes and names using libc's if_nameindex()

    :return: List of network interface indexes and names.
    :rtype: list of tuples (int index, str name)
    :raises: OSError is libc not found

    Almost certainly POSIX only, and only if libc supports if_nameindex().
    """
    import ctypes
    import ctypes.util
    from itertools import takewhile
    
    class IFace(ctypes.Structure):
        _fields_ = [('idx', ctypes.c_int), ('name', ctypes.c_char_p)]
        
    libc_s = ctypes.util.find_library('c')
    if libc_s is None:
        raise OSError('Could not locate libc')
    libc = ctypes.cdll.LoadLibrary(libc_s)
    if_nameindex = libc.if_nameindex
    if_nameindex.restype = ctypes.POINTER(IFace)
    c_ifaces = if_nameindex()
    ifaces = [(x.idx, x.name)
                  for x in takewhile(lambda i: i.idx != 0, c_ifaces)]
    libc.if_freenameindex(c_ifaces)
    return ifaces

def _main():
    """Entry point for script usage.

    Uses argparse for command line parsing, and sys.exit to return status.
    Returns 0 if a local IP is part of the network provided on the command 
    line, 1 otherwise. Result codes are inverted if the -n/--negate flag
    is present - returns 0 if no local IP address is part of provided network,
    1 otherwise.
    """
    import argparse
    import sys
    
    p = argparse.ArgumentParser(description="Check if local machine address "
                                "belongs to <network>")
    p.add_argument('-n', '--negate', help='Negate the test output',
                   action='store_true')
    p.add_argument('network', help="Network to test against, in CIDR notation",
                   type=str)
    p.add_argument('-i', '--iface', help='Name of interface to check against. '
                   'Option may be repeated.', action='append', type=str,
                       default=None, dest='ifaces', metavar='INTERFACE NAME')
    args = p.parse_args()
    net, prefix = from_cidr(args.network)
    try:
        local_ifaces = { iface[1] for iface in all_ifaces() }
    except OSError:
        sys.stderr.write('Could not enumerate network interfaces. Support '
                         'for if_nameindex() is required.\n')
        sys.exit(64)
    if args.ifaces is not None:
        test_ifaces = set(args.ifaces)
        unknown_ifaces = test_ifaces - local_ifaces
        if len(unknown_ifaces)>0:
            sys.stderr.write('Invalid interface{}: {}\n'.format(
                's' if len(unknown_ifaces)>1 else '',
                ', '.join(unknown_ifaces)))
            sys.exit(64) # Usage error. Should return 78 (config error)?
    else:
        test_ifaces = local_ifaces

    in_net = any([in_network(addr, net, prefix)
                  for addr in ifaces_ips(test_ifaces)
                      if addr is not None])

    exit_code = 0 if in_net else 1

    if args.negate:
        sys.exit(1-exit_code)
    else:
        sys.exit(exit_code)

if __name__ == '__main__':
    _main()
