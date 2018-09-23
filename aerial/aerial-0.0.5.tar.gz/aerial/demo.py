# -*- coding: utf-8 -*-

from __future__ import print_function

import logging
import signal
import sys
import time

from .wrappers import received


logging.basicConfig(
    level=logging.INFO, format='[ PID %(process)d ] %(message)s')

symbols = [
    u'    →     ',
    u'     →    ',
    u'      →   ',
    u'       →  ',
    u'        → ',
    u'         →',
    u'         ↘',
    u'         ↓',
    u'         ↙',
    u'         ←',
    u'        ← ',
    u'       ←  ',
    u'      ←   ',
    u'     ←    ',
    u'    ←     ',
    u'   ←      ',
    u'  ←       ',
    u' ←        ',
    u'←         ',
    u'↖         ',
    u'↑         ',
    u'↗         ',
    u'→         ',
    u' →        ',
    u'  →       ',
    u'   →      ',
    u'    →     ',
    u'     ↷    ',
    u'     ↻    ',
    u'     ⟳    ',
]


def trick():
    """ Spin the spinner """
    for symbol in symbols:
        print(symbol, end='\r')
        sys.stdout.flush()
        time.sleep(.1)


def main():
    """ A demo that can be used to test functionality """
    logging.info('Hello, send me a SIGTERM to exit, or a SIGHUP for a trick')
    while not received(signal.SIGTERM):
        if received(signal.SIGHUP):
            trick()
            logging.info('Neat huh?')
        else:
            time.sleep(.5)
    logging.info('See you later')
