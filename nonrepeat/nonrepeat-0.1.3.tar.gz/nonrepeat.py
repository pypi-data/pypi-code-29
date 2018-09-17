import re
import os


def nonrepeat_filename(filename, primary_suffix=None, separator='-', start=0, root=''):
    original = filename

    while os.path.exists(os.path.join(root, filename)):
        if re.search(r'.*\d+', os.path.splitext(original)[0]) and filename == original:
            filename += separator

        stem, suffix = os.path.splitext(filename)
        if primary_suffix:
            if not re.search(r'.*{}({}\d+)?'.format(re.escape(primary_suffix),
                                                    re.escape(separator)),
                             stem):
                stem += separator + primary_suffix
                filename = stem + suffix
                continue

        match_obj = re.search(r'(.*)(?<!\d)(\d+)$', stem)
        if match_obj is None:
            if stem[-1].isdigit():
                stem += separator
            stem += str(start)
        else:
            if primary_suffix and stem.endswith(primary_suffix):
                stem += separator + str(start)
            else:
                stem0, num = match_obj.groups()
                stem = stem0 + str(int(num) + 1)
        filename = stem + suffix

    return filename


def nonrepeat(name, pool, primary_suffix=None, separator='-', start=0):
    """

    :param name:
    :param pool:
    :param primary_suffix:
    :param separator:
    :param start:
    :return:
    >>> from nonrepeat import nonrepeat
    >>> nonrepeat('foo', pool=['foo', 'foo0', 'foo1'])
    'foo2'
    """
    pool = set(pool)
    while name in pool:
        if primary_suffix:
            if primary_suffix not in name:
                name += separator + primary_suffix
                continue

        match_obj = re.search(r'(.*)(?<!\d)(\d+)$', name)
        if match_obj is None:
            if name[-1].isdigit():
                name += separator
            name += str(start)
        else:
            if primary_suffix and name.endswith(primary_suffix):
                name += separator + str(start)
            else:
                name0, num = match_obj.groups()
                name = name0 + str(int(num) + 1)

    return name


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
