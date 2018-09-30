"""
Incrementally decode bytes into strings and lines.
"""


import collections
import functools

from . import newlines, utils, value


class DecodeAccumulator(value.ValueObject):
    r"""
    Incrementally decode bytes into strings.
    Also split the input into lines.

    This class implements an incremental decoder: an object that may be
    fed bytes (one or several at a time) as they are e.g. read from
    a network stream or a subprocess's output, and that adds to a result
    string as soon as enough bytes have been accumulated to produce
    a character in the specified encoding.

    Note that DecodeAccumulator objects are immutable value objects:
    the add() method does not modify its invocant, but returns a new
    DecodeAccumulator object instead.

    Sample usage:

        while True:
            bb = subprocess.stdout.read(1024)
            if len(bb) == 0:
                break
            acc = acc.add(bb)
            assert(not acc.done)
            if acc.splitter.lines:
                # at least one full line was produced
                (acc, lines) = acc.pop_lines()
                print('\n'.join(lines)

        if acc.buf:
            print('Leftover bytes left in the buffer!', file=sys.stderr)

        if acc.splitter.buf:
            print('Incomplete line: ' + acc.splitter.buf)

        final = acc.add(None)
        assert(final.splitter.buf == '')
        assert(final.splitter.done)
        assert(final.done)
        if acc.splitter.buf:
            assert(len(final.splitter.lines) == len(acc.splitter.lines) + 1)
    """

    ByteAccumulator = collections.namedtuple('ByteAccumulator',
                                             ['buf', 'splitter'])

    def __init__(self, encoding=None, split=None, newline=None, _data=None):
        """
        Initialize a DecodeAccumulator object with the specified encoding.
        """
        if encoding is None:
            encoding = 'UTF-8'
        if split is None:
            split = True

        super(DecodeAccumulator, self).__init__(_data)
        self._data['encoding'] = self._data.get('encoding', encoding)
        self._data['buf'] = self._data.get('buf',
                                           ''.encode(self._data['encoding']))
        self._data['newline'] = self._data.get('newline', newline)
        self._data['split'] = self._data.get('split', split)
        self._data['done'] = self._data.get('done', False)

        if 'splitter' not in self._data:
            newline = self._data['newline']
            if not self._data['split']:
                splitter = newlines.NullSplitter()
            elif newline is None:
                splitter = newlines.UniversalNewlines()
            elif newline == '':
                splitter = newlines.UniversalNewlines(preserve=True)
            else:
                splitter = newlines.FixedEOLSplitter(eol=newline)
            self._data['splitter'] = splitter

    @property
    def encoding(self):
        """
        Return the name of the encoding used to decode text.
        """
        return self._data['encoding']

    @property
    def buf(self):
        """
        Return the buffer of bytes that have not formed a full character yet.
        """
        return self._data['buf']

    @property
    def split(self):
        """
        Return the "should text be split into lines" flag.
        """
        return self._data['split']

    @property
    def newline(self):
        """
        Return the line separator setting (None for universal newlines,
        '' for universal newlines with the separators included, any other
        value for a fixed line separator with the separators not included).
        """
        return self._data['newline']

    @property
    def splitter(self):
        """
        Return the TextSplitter object used for forming lines.
        """
        return self._data['splitter']

    @property
    def done(self):
        """
        Return the "no more incremental decoding" flag.
        """
        return self._data['done']

    def add(self, data):
        """
        Add the specified bytes to the internal buffer and try to decode
        as many characters from the buffer as possible.  If any newline
        characters were found in the decoded string, add new lines to
        the accumulator's lines member.

        If invoked with None as a parameter, finalizes the incremental
        encoding by adding the remaining decoded characters as a last line.
        """

        def add_byte(acc, byte):
            """
            Add a byte to the incremental decoding buffer, try to decode
            a full character; if successful, pass it to the splitter.
            """
            buf = acc.buf + utils.bytes_from_byte(byte)
            try:
                char = buf.decode(self.encoding)
                buf = ''.encode('us-ascii')
            except UnicodeDecodeError:
                return self.ByteAccumulator(buf=buf,
                                            splitter=acc.splitter)

            return self.ByteAccumulator(buf=''.encode(self.encoding),
                                        splitter=acc.splitter.add(char))

        if data is None:
            data = self._as_dict()
            data['done'] = True
            data['splitter'] = data['splitter'].add(None)
            return type(self)(_data=data)

        assert not self.done
        acc = functools.reduce(add_byte, data,
                               self.ByteAccumulator(buf=self.buf,
                                                    splitter=self.splitter))
        data = self._as_dict()
        data['buf'] = acc.buf
        data['splitter'] = acc.splitter
        return type(self)(_data=data)

    def pop_lines(self):
        """
        Return a tuple with two elements:
        - an object with the same incremental decoding state, but
          without the accumulated full lines
        - the full lines accumulated so far
        """
        data = self._as_dict()
        (data['splitter'], lines) = self.splitter.pop_lines()
        return (
            type(self)(_data=data),
            lines
        )

    def __str__(self):
        return 'DecodeAccumulator: encoding "{enc}", {rln} raw bytes, ' \
               '{sdone}done, splitter: {splitter}' \
               .format(enc=self.encoding, rln=len(self.buf),
                       sdone='' if self.done else 'not ',
                       splitter=self.splitter)

    def __repr__(self):
        data = self._as_dict()
        return 'DecodeAccumulator({data})' \
            .format(data=', '.join(['{var}={val}'.format(var=var,
                                                         val=repr(data[var]))
                                    for var in sorted(data.keys())]))
