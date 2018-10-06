""" Game fix for Spiral Knights
Using details from https://spcr.netlify.com/app/99900
"""
#pylint: disable=C0103


import os
import sys


def main():
    """ Set the STEAM_RUNTIME_PREFER_HOST_LIBRARIES environment variable to 0
    """

    print('Applying Spiral Knights Game Fixes')

    # Disable host libraries
    os.environ['STEAM_RUNTIME_PREFER_HOST_LIBRARIES'] = '0'
