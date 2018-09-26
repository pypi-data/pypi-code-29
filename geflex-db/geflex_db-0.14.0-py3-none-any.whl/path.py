DEFAULT_SYMBOLS = {'\\': '{#01}',
                   '/': '{#02}',
                   ':': '{#03}',
                   '*': '{#04}',
                   '?': '{#05}',
                   '"': '{#06}',
                   '<': '{#07}',
                   '>': '{#08}',
                   '|': '{#09}',
                   '+': '{#10}'}


def _code(s: str, decode_mode: bool, symbols: dict = None):
    if symbols is None:
        symbols = DEFAULT_SYMBOLS
    for symbol, code in symbols.items():
        if decode_mode:
            s = s.replace(symbol, code)
        else:
            s = s.replace(code, symbol)
    return s


def decode(s: str, symbols: dict = None) -> str:
    return _code(s, decode_mode=True, symbols=symbols)


def encode(s: str, symbols: dict = None) -> str:
    return _code(s, decode_mode=False, symbols=symbols)


class Coding:
    __slots__ = 'map',

    def __init__(self, map_obj: dict):
        self.map = map_obj

    def decode(self, s: str):
        return decode(s, self.map)

    def encode(self, s: str):
        return encode(s, self.map)


class Path:
    __slots__ = ('_path', '_parent_path')

    def __init__(self, parent_path: str, path: str=''):
        parent_path = parent_path.replace('/', '\\')

        self._path = ''
        if path.startswith('\\') or '\\' not in path:
            self._parent_path = '\\'.join((p for p in parent_path.split('\\') if p))
        self.path = path

    @property
    def abs_path(self):
        return self._parent_path + self._path

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        assert type(value) is str
        path = value.replace('/', '\\')
        if path is '':
            self._path = path
        elif path.startswith('\\') or '\\' not in value:
            self._path = '\\' + '\\'.join((p for p in value.split('\\') if p))
        else:
            self._parent_path = ''
            self._path = value

    @property
    def parent_path(self):
        return self._parent_path

    @parent_path.setter
    def parent_path(self, value):
        if self._path.startswith('\\'):
            self._path = ''
        self._parent_path = value

    def get_child(self, path: str):
        assert type(path) is str
        return Path(self.abs_path, path)

    def __str__(self):
        return str(self.abs_path)

    def __repr__(self):
        return f'{type(self).__name__}({repr(self.parent_path)}, {repr(self.path)})'

    def __eq__(self, other):
        if type(other) is str:
            if other.startswith('\\'):
                return other == self._path
            elif '\\' not in other and other is not '':
                return f'\\{other}' == self._path
            else:
                return other == self.abs_path
        elif type(other) is Path:
            return self.abs_path == other.abs_path
