"""
Separate a stream of text into lines.
"""


import abc
import functools

import six

from . import value


@six.add_metaclass(abc.ABCMeta)
class TextSplitter(value.ValueObject):
    """
    Base class for building text splitters: objects that are fed
    characters and spit out fully-formed lines.
    """

    def __init__(self, _data=None):
        """
        Initialize the base TextSplitter object, either with data
        from an existing value object, or with the default values -
        an empty buffer, an empty list of lines, a false done flag.
        """
        super(TextSplitter, self).__init__(_data)
        self._data['buf'] = self._data.get('buf', '')
        self._data['lines'] = self._data.get('lines', [])
        self._data['done'] = self._data.get('done', False)

    @property
    def buf(self):
        """
        Return the buffer of characters not yet forming a line.
        """
        return self._data['buf']

    @property
    def lines(self):
        """
        Return the buffer of full lines formed so far.
        """
        return self._data['lines']

    @property
    def done(self):
        """
        Return the "no more incoming text" flag.
        """
        return self._data['done']

    @abc.abstractmethod
    def add(self, char):
        """
        Process a character or, if passed None, finalize the splitting of
        incoming characters into lines as needed.

        Note: this method only handles the None case; derived classes must
        override it to actually process characters and form lines.
        """
        assert char is None
        data = self._as_dict()
        if data['buf']:
            data['lines'] = data['lines'] + [data['buf']]
            data['buf'] = ''
        data['done'] = True
        return type(self)(_data=data)

    def pop_lines(self):
        """
        Return a tuple with two elements:
        - an object with the same incomplete line buffer, but
          without the accumulated full lines
        - the full lines accumulated so far
        """
        if not self.lines:
            return (self, [])

        data = self._as_dict()
        lines = data['lines']
        data['lines'] = []
        return (type(self)(_data=data), lines)

    @abc.abstractmethod
    def __str__(self):
        return '{tname}: {ln} lines + {lbuf} characters, {sdone}done' \
               .format(tname=type(self).__name__,
                       ln=len(self.lines), lbuf=len(self.buf),
                       sdone='' if self.done else 'not ')

    def __repr__(self):
        data = self._as_dict()
        return '{tname}({data})' \
            .format(tname=type(self).__name__,
                    data=', '.join(['{var}={val}'.format(var=var,
                                                         val=repr(data[var]))
                                    for var in sorted(data.keys())]))


class UniversalNewlines(TextSplitter):
    """
    Split a string into text lines in a manner similar to the file class's
    universal newlines mode: detect LF, CR/LF, and bare CR line terminators.
    """

    def __init__(self, preserve=None, _data=None):
        """
        Initialize a UniversalNewlines splitter object with the specified
        "preserve the line terminators in the returned lines" flag.
        """
        if preserve is None:
            preserve = False

        super(UniversalNewlines, self).__init__(_data)
        self._data['preserve'] = self._data.get('preserve', preserve)
        self._data['cr'] = self._data.get('cr', False)

    @property
    def preserve(self):
        """
        Return the "preserve line terminators in returned lines" flag.
        """
        return self._data['preserve']

    @property
    def cr(self):
        """
        Return the "was the last character a CR" flag.
        """
        return self._data['cr']

    def add(self, char):
        """
        Add a character to the object's buffer and split out a line if
        needed depending on the character being CR, LF, and the previous
        state of the buffer (e.g. detecting CR/LF combinations).
        """

        def newline(data, eol):
            """
            Turn the accumulated buffer into a new line and reset
            the "last character was a CR" flag.
            """
            line = data['buf'] + (eol if data['preserve'] else '')
            data['lines'] = data['lines'] + [line]
            data['buf'] = ''
            data['cr'] = False

        if char is None:
            if self.cr:
                data = self._as_dict()
                newline(data, '\r')
                return type(self)(_data=data).add(char)
            else:
                return super(UniversalNewlines, self).add(char)

        assert not self.done
        data = self._as_dict()
        if data['cr']:
            if char == '\n':
                newline(data, '\r\n')
            else:
                newline(data, '\r')
                return type(self)(_data=data).add(char)
        elif char == '\n':
            newline(data, '\n')
        elif char == '\r':
            data['cr'] = True
        else:
            data['buf'] = data['buf'] + char

        return type(self)(_data=data)

    def __str__(self):
        return 'UniversalNewlines: {ln} lines + {lbuf} characters, ' \
               '{sdone} done, {spres}preserve ' \
               .format(ln=len(self.lines), lbuf=len(self.buf),
                       sdone='' if self.done else 'not ',
                       spres='' if self.preserve else 'do not ')


class NullSplitter(TextSplitter):
    """
    Do not split the text at all.
    """
    def add(self, char):
        """
        Add a character to the object's buffer without any checks for
        line terminators since no splitting is done.
        """
        if char is None:
            return super(NullSplitter, self).add(char)

        assert not self.done

        data = self._as_dict()
        data['buf'] = data['buf'] + char
        return type(self)(_data=data)

    def __str__(self):
        return super(NullSplitter, self).__str__()


class FixedEOLSplitter(TextSplitter):
    r"""
    Split a string into lines using a fixed line separator possibly
    consisting of more than one character, e.g. '\r\n'.
    """

    def __init__(self, eol=None, _data=None):
        """
        Initialize a FixedEOLSplitter object with the specified separator.
        """
        if eol is None:
            eol = '\n'

        super(FixedEOLSplitter, self).__init__(_data)
        self._data['eol'] = self._data.get('eol', eol)
        self._data['in_eol'] = self._data.get('in_eol', 0)

    @property
    def eol(self):
        """
        Return the sequence of characters used as a line separator.
        """
        return self._data['eol']

    def add(self, char):
        """
        Process a new character, checking whether it is part of
        an already-started line separator, of a newly-started one,
        or just a normal text character.
        """
        if char is None:
            data = self._as_dict()
            if data['in_eol'] > 0:
                data['buf'] = data['buf'] + data['eol'][:data['in_eol']]
                data['in_eol'] = 0
                return type(self)(_data=data).add(char)
            else:
                return super(FixedEOLSplitter, self).add(char)

        assert not self.done
        data = self._as_dict()
        if char == data['eol'][data['in_eol']]:
            data['in_eol'] = data['in_eol'] + 1
            if data['in_eol'] == len(data['eol']):
                data['lines'] = data['lines'] + [data['buf']]
                data['buf'] = ''
                data['in_eol'] = 0
        elif data['in_eol'] > 0:
            data['buf'] = data['buf'] + data['eol'][0]
            to_add = data['eol'][1:data['in_eol']] + char
            data['in_eol'] = 0
            return functools.reduce(lambda spl, add_char: spl.add(add_char),
                                    to_add, type(self)(_data=data))
        else:
            data['buf'] = data['buf'] + char
        return type(self)(_data=data)

    def __str__(self):
        return '{tname}: {ln} lines + {lbuf} characters, {sdone}done, ' \
               'eol {eol}' \
               .format(tname=type(self).__name__,
                       ln=len(self.lines), lbuf=len(self.buf),
                       sdone='' if self.done else 'not ', eol=repr(self.eol))
