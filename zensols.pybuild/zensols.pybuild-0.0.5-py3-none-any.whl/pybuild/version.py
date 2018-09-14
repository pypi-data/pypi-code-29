import re


class Version(object):
    def __init__(self, major=0, minor=0, debug=1):
        self.major = major
        self.minor = minor
        self.debug = debug

    @classmethod
    def from_string(clz, s):
        m = re.search('^v?(\d+)\.(\d+)\.(\d+)$', s)
        if m is not None:
            return Version(int(m.group(1)), int(m.group(2)), int(m.group(3)))

    def format(self, prefix='v'):
        return prefix + '{major}.{minor}.{debug}'.format(**self.__dict__)

    def increment(self, decimal='debug', inc=1):
        if decimal == 'major':
            self.major += inc
        elif decimal == 'minor':
            self.minor += inc
        elif decimal == 'debug':
            self.debug += inc
        else:
            raise ValueError('uknown decimal type: {}'.format(decimal))

    def __lt__(self, o):
        if self.major < o.major:
            return True
        if self.major > o.major:
            return False

        if self.minor < o.minor:
            return True
        if self.minor > o.minor:
            return False

        if self.debug < o.debug:
            return True
        if self.debug > o.debug:
            return False

        # equal
        return False

    def __le__(self, o):
        if self.major <= o.major:
            return True
        if self.major >= o.major:
            return False

        if self.minor <= o.minor:
            return True
        if self.minor >= o.minor:
            return False

        if self.debug <= o.debug:
            return True
        if self.debug >= o.debug:
            return False

        # equal
        return False

    def __eq__(self, o):
        return self.__dict__ == o.__dict__

    def __str__(self):
        return self.format()

    def __repr__(self):
        return self.__str__()
