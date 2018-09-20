def map_to_inline(_map):
    return ';'.join(['{}:{}'.format(k, v) for k, v in _map.items()])


def get_chunk_size(text):
    return len(list(set(text)))


def inline_to_map(inline):
    _map = {}

    for item in inline.split(';'):
        kv = item.split(':')
        _map[kv[0]] = kv[1]

    return _map


def get_encoding_map(text, chunk_size):
    _map = {}

    for char in text:
        chunk = [0 for x in range(chunk_size)]

        i = 0
        while ''.join(str(c) for c in chunk) in _map.values():
            chunk[i] += 1
            i += 1

        _map[char] = ''.join(str(c) for c in chunk)

    return _map


def encode(text):
    chunk_size = get_chunk_size(text)
    _map = get_encoding_map(text, chunk_size)

    return (
        ''.join(
            [_map[char] if char in _map else char for char in text]
        ) + '.' + str(chunk_size), _map
    )


def decode(text, tmap):
    _text = ''
    tmap = inline_to_map(tmap) if isinstance(tmap, str) else tmap
    text = text.split('.')
    chunk_size = int(text[1])
    text = text[0]

    def get_key_by_value(tmap, value):
        for k, v in tmap.items():
            if v == value:
                return k
        return value

    chunk = ''
    for i, char in enumerate(text):
        chunk += char

        if (i+1) % chunk_size == 0:
            t = get_key_by_value(tmap, chunk) if (i + 1) % chunk_size == 0\
                else None

            if t:
                _text += t
                chunk = ''

    return _text
