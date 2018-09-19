#!/usr/bin/env python
# -*- coding: utf-8 -*- vim: ts=8 sts=4 sw=4 si et tw=79
"""\
debugable.py - Mixin-Klasse für Debugging-/Entwicklungszwecke
"""

__author__ = "Tobias Herp <tobias.herp@visaplan.com>"
VERSION = (0,
           1,   # initial version
           1,   # svn:keywords entfernt
           )
__version__ = '.'.join(map(str, VERSION))

from time import strftime
from os.path import dirname, abspath, join, basename

class Debugable:
    def __init__(self, fng=None, fileslog=None):
        if fng is None:
            fng = make_filenamegenerator()
        self._fng = fng
        if fileslog is None:
            fileslog = fng('.log')
            print "Logging to '%(fileslog)s'" % locals()
        self._fileslog = fileslog

    def writeIntermediate(self, method, ext, data):
        """
        method - which method is calling?
        ext - file extension, e.g. '.xml'
        data - content of the new file
        """
        fn = self._fng(ext)
        self.logIntermediate(method, fn, data)
        with open(fn, 'w') as f:
            f.write(data)

    def logIntermediate(self, method, fn, data):
        with open(self._fileslog, 'a') as logfile:
            logfile.write('%s: %s (%s.%s, %d [bytes])'
                          % (strftime('%H:%M:%S'),
                             basename(fn),
                             self.__class__.__name__,
                             method,
                             len(data)
                             ))


def make_filenamegenerator(fod=None):
    """
    fod -- file or directory
    """
    if fod is None:
        base = dirname(__file__)
    elif isdir(fod):
        base = fod
    else:
        base = dirname(fod)
    namestem = join(abspath(base), strftime('%Y-%m-%d_%H%M%S'))
    names = []
    mask = ('%s-%02d.%s',
            '%s-%02d%s',
            )
    def makename(ext):
        nr = len(names) + 1
        name = mask[ext.startswith('.')] \
                % (namestem, nr, ext)
        names.append(name)
        return name
    return makename


if __name__ == '__main__':
    fng = make_filenamegenerator()
    from sys import argv
    for ext in argv[1:] or ['.log', '.xml', '.html', '.pdf']:
        print fng(ext)
