import codecs


def mkfile(filepath, content):
    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(content)
