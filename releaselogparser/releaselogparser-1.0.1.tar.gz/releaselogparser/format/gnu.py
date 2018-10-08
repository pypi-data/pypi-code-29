# -*- coding: utf-8 -*-
"""
Implementation of the GNU-style 'NEWS' history format.

Usage:

  from releaselogparser import ReleaseLog, gnu
  ReleaseLog.regformat('GNU', gnu.ReleaseLogFormat)

NOTE: DON'T DO IT. This is normally done as a part of initialization of
the releaselogparser module.
"""

import re
from releaselogparser import ReleaseHistory

class ReleaseLogFormat(ReleaseHistory):
    format = ['GNU', 'NEWS']
    filename = 'NEWS'
    header = re.compile(r"""^(?:\*\s+)?    # optional initial section
          (?:(?i)version)\s+
          (?P<version>\d(?:[.,]\d+){1,2}  # At least MAJOR.MINOR
            (?:[\d._-])*)    # Optional patchlevel
          (?:.*[-,:]\s+(?P<date>.+))""", re.X)
