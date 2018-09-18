# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
***
Module: keychestbot - KeyChest Bot - monitoring bot for KeyChest service
***

# Copyright (C) Radical Prime Limited, registered in the United Kingdom.
# Unauthorized copying of this file, via any medium is strictly prohibited
#
# This file is subject to license, see the "LICENSE" file, which is
# included in this software package for details.
#
# Written by Dan Cvrcek <support@radicalprime.com>, August 2018
"""
import sys
import getopt

__author__ = "Petr Svenda, Dan Cvrcek"
__copyright__ = 'Enigma Bridge Ltd'
__email__ = 'support@enigmabridge.com'
__status__ = 'Beta'


def print_help():
    print("The program accepts the following parameters:")
    print("  -h -  this help")
    print("  -p<port> - port where the proxy listens")
    print("  -s<url:port> - address of the CloudFoxy RESTful API, e.g., http://server.cloudfoxy.com:8081")


def main():
    custom_port = None
    custom_server = None
    if len(sys.argv) > 1:
        try:
            opts, args = getopt.getopt(sys.argv[1:], "hp:s:")
        except getopt.GetoptError:
            # print help information and exit:
            print_help()
            sys.exit(2)

        for o, a in opts:
            if o == '-h':
                print_help()
            else:
                if o == '-p':
                    if a.isdigit():
                        custom_port = int(a)
                if o == '-s':
                    custom_server = a.strip()

    # we need to check the environment with information about the previous runs of this program

    # we may want to run a scan for existing keys and/or certificates

    # and we check expiry of certificates and if the current ones are installed


if __name__ == '__main__':
    main()
