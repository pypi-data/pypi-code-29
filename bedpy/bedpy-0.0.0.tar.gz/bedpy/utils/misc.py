def field_len(zipped):
    return [max([len(list(s)) for s in col]) for col in zipped]

def stringify(array):
    return [str(e) for e in array]

def truncate_str(s, l):
    return s[:l] if len(list(s)) <= l else s[:l-3]+'...'

def str_max_len(str_list, l):
    return [truncate_str(s, l) for s in str_list]

def pretty_print_header_list(header, values, truncate):
    sheader = str_max_len(stringify(header), truncate)
    svalues = str_max_len(stringify(values), truncate)
    zipped = zip([str(c) for c in sheader], [str(c) for c in svalues])
    col_len = field_len(zipped)

    h = '\t'.join([s.ljust(col_len[i]) for i, s in enumerate(sheader)])
    v = '\t'.join([s.ljust(col_len[i]) for i, s in enumerate(svalues)])

    return '\n'.join([h,v])


def str_int_q(v):
    v = str(v).strip()
    return v=='0' or (v if v.find('..') > -1 else v.lstrip('-+').rstrip('0').rstrip('.')).isdigit()

def tally(array:list) -> dict:
    t = {}
    for element in array:
        if element not in t:
            t[element] = 0
        t[element] += 1
    return t

def percents(array:list) -> dict:
    total = len(array)
    return { element: count / total for element, count in tally(array).items()}

def pretty_print_percents(percents):
    s = '{\t'
    for e, p in percents.items():
        s += f'{e}: {str(round(p, 2))}%\t'
    s += '}'
    return s
