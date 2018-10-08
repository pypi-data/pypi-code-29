# -*- coding: utf-8 -*-
"""
Implementation of two release log formats used in most Python packages.

The two formats are:

* Each entry begins with the line

    v<Version>, <Date> -- <String>

where <String> is the beginning of the description. More description lines
may follow.

* Each entry begins with the line

    <Version> (<Date>)

followed by the description text. Incidentally, this format is used by some
non-Python software, such as e.g. GNU Texinfo.

The PythonLogFormat class discovers the actual format by finding the first
input line that matches any of the above patterns.

"""

import re
from releaselogparser import ReleaseHistory

class PythonLogFormat(ReleaseHistory):
    format = ['Python', 'python']
    filename = 'CHANGES.txt'
    header = None
    header_rx = [
        re.compile("""^[vV](?P<version>\d[\d.]*)\s*
                      ,\s*
                      (?P<date>.*?)
                      \s+-+\s*
                      (?P<rest>.*)$
                   """, re.X),
        re.compile("""^(?P<version>\d[\d.]*)
                      \s*
                      (?P<date>.*)
                   """, re.X)
    ]
    
    def parse_header(self, line):
        if self.header:
            return super(PythonLogFormat, self).parse_header(line)
        else:
            for rx in self.header_rx:
                if rx.match(line):
                    self.header = rx
                    return super(PythonLogFormat, self).parse_header(line)
        return (None, None, None)
        
