"""
ReleaseLog class

Most software packages keep a history of last releases in some form. This
module provides an abstraction for handling such information.

Release history is represented by a ReleaseLog class. Each log contains a
list of history entries in reverse chronological order.

"""

from __future__ import print_function
from __future__ import unicode_literals

import re
import dateparser

class Release(object):
    """Release - a single release history entry object

    Attributes:

    date     -- datetime of the release
    version  -- release version number
    descr    -- textual description of the release

    """
    date = None
    version = None
    descr = None
    def __init__(self, version, date, descr):
        self.version = version
        self.date = date
        self.descr = descr
    def __str__(self):
        return "Version %s, released at %s" % (self.version, self.date)


class ReleaseHistory(object):
    """ReleaseHistory - base class for ReleaseLog implementations

    Class Attributes:

    format     - array of names for this format
    filename   - name of the file normally used to keep the log file

    header     - a compiled regular expression that returns a match for
                 history entry heading lines
    end_of_entry_rx - a compiled regular expression returning a match for
                   end of entry. Can be None

    Instance Attributes:
    
    history    - a list of Release objects. Normally not needed, since
                 it is accessed by indexing the object.
    """
    
    history = []

    end_of_entry_rx = re.compile('^(\f|^\s*=+\s*$)')
    
    def __len__(self):
        return len(self.history)

    def __getitem__(self, i):
        return self.history[i]
    
    def append(self, arg):
        """Appends new release to the end of release history list"""
        if isinstance(arg, Release):
            self.history.append(arg)
        else:
            raise TypeError('argument to append must be a Release')

    def parse_header(self, line):
        """Match input line against the history header regexp. On match,
        return a tuple (date, version, startdescr), where date is the
        release date (datetime), version is the release version number, and
        startdescr is the first line of the description or None.
        On failure, return (None, None, None).
        """
        date = None
        version = None
        rest = None
        m = self.header.match(line)
        if m:
            version = m.group('version')
            date = dateparser.parse(m.group('date'))
            try:
                rest = m.group('rest')
                if len(rest) == 0:
                    rest = None
            except IndexError:
                pass
        return date, version, rest

    def is_end_of_entry(self, line):
        return (self.end_of_entry_rx.match(line)
                if self.end_of_entry_rx else False)
    
    def __init__(self, lines, **kwargs):
        """Create a new history object from the list of lines. The list is
        split into history entries by lines that match the header compiled
        regexp. Matches should contain at least two groups:

           version - part of line containing the release version
           date    - part of line containing the release date

        The line is matching only if both groups are not None.

        Additionally, a line starting with form-feed character (\f) or
        containing a line of contiguous equals signs, optionally surrounded
        by whitespace, is considered to terminate the current history entry.
        
        Keyword arguments:

        start=N
           Start from the entry N
        stop=N
           Stop parsing on Nth entry
        count=N
           Collect at most N entries

        If all three keywords are given, the actual range of history entries
        is computed as

           [start, min(start+count, stop)]

        Entries are numbered from 0.
        """
        self.history = []
        
        date = None
        version = None
        descr = []

        start = None
        stop = None
        count = None
        for kw, val in kwargs.items():
            if kw == 'start':
                start = val
            elif kw == 'stop':
                stop = val
            elif kw == 'count':
                count = val
            else:
                raise KeyError ('keyword %s is not known' % kw)

        if count:
            if start:
                if not (stop and stop < start + count):
                    stop = start + count
            elif stop:
                start = stop - count
                if start < 0:
                    start = 0
            else:
                start = 0
                stop = start + count
                
        i = 0        
        for line in lines:
            (d, v, r) = self.parse_header(line)
            if d:
                if date:
                    self.append(Release(version, date, descr))
                    date = None
                    version = None
                    descr = []

                i += 1
                if start and i <= start:
                    continue
                if stop and i > stop:
                    break

                date = d
                version = v
                descr = []
                if r:
                    descr.append(r)
            elif self.is_end_of_entry(line):
                if date:
                    self.append(Release(version, date, descr))
                    date = None
                    version = None
                    descr = []
            elif date:
                descr.append(line.rstrip("\n"))
        if date:
            self.append(Release(version, date, descr))

    def __iter__(self):
        for r in self.history:
            yield(r)

class ReleaseLog(object):
    """A release log class.

    It is a fabric returning actual release history implementation, depending
    on the first argument to constructor. Typical usage

      cl = ReleaseLog('GNU', lines, count=1)
    
    """
    formatdb = {}

    def __new__(cls, fmt, *args, **kwargs):
        """Object constructor:

            ReleaseLog(fmt, lines, [start=N], [stop=N], [count=N]

        Arguments:

        fmt
           History log format. E.g. 'GNU' for GNU-style NEWS file, or
           'Changes', for CPAN-style Changes file.
        lines
           List of history lines.

        Keyword arguments are the same as in ReleaseHistory.
        """
        
        return cls.formatdb[fmt](*args, **kwargs)

    @classmethod
    def regformat(cls, fmt, impl):
        """Register a new history format implementation. Typical usage:

          ReleaseLog.deftype(format, class)

        Arguments:

        format
           Format name. It will subsequently be used as the format argument
           to ReleaseLog constructor in order to require this particular
           implementation.
        class
           Name of the class implementing the format.
        """
        if isinstance(fmt, list):
            for f in fmt:
                cls.regformat(f, impl)
        else:
            cls.formatdb[fmt] = impl

    @classmethod
    def formats(cls):
        """Return a list of supported release log formats. Each item in
        the list is a list of alternative format names.
        """
        rev = {}
        for fmt in cls.formatdb:
            if cls.formatdb[fmt] not in rev:
                rev[cls.formatdb[fmt]] = []
            rev[cls.formatdb[fmt]].append(fmt)
        return rev.values()

    @classmethod
    def filename(cls, name):
        """Returns the accepted log file name for the given format."""
        return cls.formatdb[name].filename

        
# Initialize the ReleaseLog implementations
import pkgutil
import importlib

for (loader, name, ispkg) in pkgutil.iter_modules([dir for dir in
                                                   map(lambda x: x + '/format',
                                                       __path__)]):
    importlib.import_module('.' + name, __package__ + '.format')

for cls in ReleaseHistory.__subclasses__():
    try:
        ReleaseLog.regformat(cls.format, cls)
    except AttributeError:
        pass
