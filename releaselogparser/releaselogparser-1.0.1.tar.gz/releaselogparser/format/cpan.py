# -*- coding: utf-8 -*-
"""
Implementation of the CPAN 'Changes' history format.

Usage:

  from releaselogparser import ReleaseLog, cpan
  ReleaseLog.regformat('Changes', cpan.ReleaseLogFormat)

NOTE: DON'T DO IT. This is normally done as a part of initialization of
the releaselogparser module.
"""
import re
from releaselogparser import ReleaseHistory


class ReleaseLogFormat(ReleaseHistory):
    format = ['CPAN', 'Changes']
    filename = 'Changes'
    header = re.compile('^(?P<version>\d[\d.]*)\s+(?P<date>.+?)\s*$')

