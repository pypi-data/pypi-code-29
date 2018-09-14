'''
A format checker that checks that the following for an object:
  - Each value has a "offset" and "len" integer key. "len" is also allowed to
    be a string, as long as the string is "all", indicating that this key is
    the only one.
  - Taken together, the "offset" and "len" keys carve out a contiguous set with
    no gaps, with the minimum entry being 0.
One example use of this format is in schemas describing offsets to bytes in
memory.

For example, the following is valid:
a:
  offset: 4
  len: 8
b:
  offset: 0
  len: 4
c:
  offset: 12
  len: 20

But the following is not valid:
a:
  offset: 4
  len: 8
b:
  offset: 0
  len: 5
c:
  offset: 11
  len: 20
'''


import jsonschema


FORMAT_NAME = 'contiguous-indices'


def check(d):
    '''Scans through a map of schema keys, adding up the offset and length
    properties and making sure the entire block is contiguous.'''
    if not isinstance(d, dict):
        raise jsonschema.exceptions.FormatError('not a map: %s' % d)

    # Validate offset properties for correctness.
    items = list(d.items())
    for k, v in items:
        try:
            offset = v['offset']
        except KeyError:
            raise jsonschema.exceptions.FormatError(
                'key "%s" is missing an offset property' % k)
        if not isinstance(offset, int):
            if offset == 'all':
                if len(items) != 1:
                    raise jsonschema.exceptions.FormatError(
                        'length "all" specified but schema length is not 1')
                else:
                    # We have only one offset ("all"), and it is valid. We are
                    # done.
                    return True
            else:
                raise jsonschema.exceptions.FormatError(
                    'offset for key "%s" must be int or "all"' % k)

    items.sort(key=lambda item: item[1]['offset'])

    offset = items[0][1]['offset']
    if offset != 0:
        raise jsonschema.exceptions.FormatError(
            'lowest offset is not 0 for key "%s"' % items[0][0])

    for i in range(1, len(items)-1):
        k, v = items[i]
        offset = v['offset']
        length = v['len']
        if length == 0:
            raise jsonschema.exceptions.FormatError('key %s has 0 length' % k)
        next_offset = items[i+1][1]['offset']
        if offset + length != next_offset:
            next_key = items[i+1][0]
            return ('in key "%s", offset + length overlaps with next key "%s"'
                    % (k, next_key))

    return True
