import re
import sre_constants
import subprocess


def cmd_output(*cmd, **kwargs):
    retcode = kwargs.pop('retcode', 0)
    popen_kwargs = {'stdout': subprocess.PIPE, 'stderr': subprocess.PIPE}
    popen_kwargs.update(kwargs)
    proc = subprocess.Popen(cmd, **popen_kwargs)
    stdout, stderr = proc.communicate()
    stdout = stdout.decode('UTF-8')
    if stderr is not None:
        stderr = stderr.decode('UTF-8')
    if retcode is not None and proc.returncode != retcode:
        raise subprocess.CalledProcessError(cmd, retcode, proc.returncode, stdout, stderr)
    return stdout


class RexList(list):
    """
        list class where each entry is a valid regular expression

    >>> r = RexList(["a.*"])
    >>> r.append("[0-9]*")
    >>> "1" in r
    True

    >>> ['abc', 'ccc', '10'] - r
    ['ccc']

    >>> ('abc', 'ccc', '10') - r
    ('ccc',)

    >>> "cc" in r
    False

    >>> "abc" in r
    True

    >>> print(r)
    ['a.*', '[0-9]*']

    >>> r[0] = '.*'

    >>> r[0] = '[0-'
    Traceback (most recent call last):
        ...
    ValueError: [0- is not a valid regular expression
    """

    def __init__(self, seq=None):
        regexx = []
        if seq:
            for el in seq:
                regexx.append(self._compile(el))
        super(RexList, self).__init__(regexx)

    def __repr__(self):
        return str([r.pattern for r in self])

    def _compile(self, pattern, index=None):
        try:
            return re.compile(pattern)
        except (TypeError, re.error, sre_constants.error):
            raise ValueError(str(pattern))

    def __setitem__(self, i, pattern):
        rex = self._compile(pattern)
        super(RexList, self).__setitem__(i, rex)

    def append(self, pattern):
        rex = self._compile(pattern)
        super(RexList, self).append(rex)

    def __contains__(self, target):
        t = str(target)
        for rex in self:
            m = rex.match(t)
            if m and m.group():
                return True
        return False

    def __rsub__(self, other):
        if other:
            if isinstance(other, (list, tuple)):
                t = type(other)
                return t([a for a in other if a not in self])
