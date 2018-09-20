import string
import random


LETTERS = string.letters + ' '
SPECIAL_LETTERS = '{}[]<>.-_'


def map_to_inline(_map):
    return ';'.join(['{}:{}'.format(k, v) for k, v in _map.items()])


def inline_to_map(inline):
    _map = {}

    for item in inline.split(';'):
        kv = item.split(':')
        _map[kv[0]] = kv[1]

    return _map


def get_random(seed=1):
    return random.choice(LETTERS) +\
        ''.join(random.choice(SPECIAL_LETTERS) for i in range(0, seed / 16))


def get_encoding_map(_map={}):
    for char in LETTERS:
        r = get_random()
        i = 0
        while r in _map.values():
            r = get_random(i)
            i += 1

        _map[char] = r

    return _map


def encode(text):
    _map = get_encoding_map()
    delimeter = get_random(len(_map.items()))

    return (
        delimeter.join(
            [_map[char] if char in _map else char for char in text]
        ), delimeter, _map
    )


def decode(text, delimeter, tmap):
    tmap = inline_to_map(tmap) if isinstance(tmap, str) else tmap

    def get_key_by_value(tmap, value):
        for k, v in tmap.items():
            if v == value:
                return k
        return value

    return ''.join(
        [get_key_by_value(tmap, value) for value in text.split(delimeter)])
