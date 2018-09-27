"""MyProxy client utils package - contains openssl module for parsing OpenSSL
config files.

NERC DataGrid Project
"""
__author__ = "P J Kershaw"
__date__ = "15/12/08"
__copyright__ = "Copyright 2018 United Kingdom Research and Innovation"
__license__ = """BSD - See LICENSE file in top-level package directory"""
__contact__ = "Philip.Kershaw@stfc.ac.uk"
from six.moves.configparser import SafeConfigParser


class CaseSensitiveConfigParser(SafeConfigParser):
    '''Subclass the SafeConfigParser - to preserve the original string case of
    config section names
    '''
    def optionxform(self, optionstr):
        '''Extend SafeConfigParser.optionxform to preserve case of option names
        '''
        return optionstr
