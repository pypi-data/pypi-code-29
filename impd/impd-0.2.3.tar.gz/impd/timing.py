def parse_time(seconds, min_length=2):
    hms = _parse_seconds(seconds, [60, 60])
    if len(hms) < min_length:
        hms = [0] * (min_length - len(hms)) + hms
    return ':'.join(map(_padd_time, map(int, hms)))


def _padd_time(time):
    return '{:02d}'.format(time)


def _parse_seconds(seconds, formats):
    format_ = formats.pop(0)
    if formats == [] or seconds < format_:
        return [seconds]
    rem, new = divmod(seconds, format_)
    return _parse_seconds(rem, formats) + [new]
