import re


var_regex = re.compile(r"{(\w+)(?::([^}]+))?}")


def url_to_regex(url):
    regex = ''
    last_pos = 0
    for match in var_regex.finditer(url):
        regex += re.escape(url[last_pos:match.start()])
        var_name = match.group(1)
        expr = match.group(2) or '[^/]+'
        expr = '(?P<%s>%s)' % (var_name, expr)
        regex += expr
        last_pos = match.end()

    regex += re.escape(url[last_pos:])
    regex = '^%s$' % regex
    return regex
