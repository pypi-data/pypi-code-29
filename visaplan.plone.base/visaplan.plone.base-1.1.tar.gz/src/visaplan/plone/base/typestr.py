# -*- coding: utf-8 -*- vim: ts=8 sts=4 sw=4 si et tw=79
"""
Typ-Strings für Unitracc

Dieses Modul stellt drei Dictionaries bereit, die verschiedene Zeichenketten
für die Unitracc-Portaltypen bereitstellen.

>x> type_string['article']
{'New thingy': 'New article',
 'Our thingies': 'Our articles',
 'Own thingies': 'Own articles',
 'Thingies': 'UnitraccArticle_plural',
 'Thingy': 'Article',
 'UnitraccThingy': 'UnitraccArticle',
 'a_thingy': 'a article',
 'add_text': 'Add new article',
 'add_url': '/@@temp/addArticle',
 'import_text': 'Import articles via XML',
 'my-thingies': 'my-articles',
 'our-thingies': 'our-articles',
 'portal_type': 'UnitraccArticle',
 'thingies': 'articles',
 'thingy': 'article',
 'unitraccthingy_view': 'unitraccarticle_view'}

In einer Form, die das doctests-Modul mag (das leider im Unterschied zu pprint
anders sortiert - wie genau?! §:-| - und nicht umgebrochen:

>>> sorted(type_string['article'].items())
[('New thingy', 'New article'), ('Our thingies', 'Our articles'), ('Own thingies', 'Own articles'), ('Thingies', 'UnitraccArticle_plural'), ('Thingy', 'Article'), ('UnitraccThingy', 'UnitraccArticle'), ('a_thingy', 'a article'), ('add_text', 'Add new article'), ('add_url', '/@@temp/addArticle'), ('import_text', 'Import articles via XML'), ('my-thingies', 'my-articles'), ('our-thingies', 'our-articles'), ('portal_type', 'UnitraccArticle'), ('thingies', 'articles'), ('thingy', 'article'), ('unitraccthingy_view', 'unitraccarticle_view')]

Dieselben Dictionarys sind über verschiedene Schlüssel zugänglich:

>>> pt_string['UnitraccArticle'] is type_string['article']
True

>>> plu_string['articles'] is type_string['article']
True

Diese Zeichenketten sind *nicht übersetzt*; die Übersetzung wird nachgelagert
vorgenommen.  Zur Verwendung dieses Moduls ist daher kein Kontext nötig.
Der Zugriff aus Seitentemplates kann über den Browser "untranslated" erfolgen.

Die folgenden werden für die Generierung von Breadcrumbs verwendet:

>>> view2plu['unitraccarticle_view']
'articles'
>>> plu2tup['articles']
(('Own articles', 'my-articles'), ('Our articles', 'our-articles'))
>>> plu2import_label['articles']
'Import article'
>>> pt2tup['UnitraccArticle']
(('Own articles', 'my-articles'), ('Our articles', 'our-articles'))
>>> pt2tup['UnitraccArticle'] is plu2tup['articles']
True

Beim direkten Aufruf von der Kommandozeile werden die Doctests ausgeführt, und
es wird der i18n-Honigtopf für diese Zeichenketten neu generiert (siehe unten).

Achtung:
Die so generierte Datei ist ebenfalls versioniert; nach Neugenerierung (die nur
nötig sein sollte, wenn neue Schlüssel hinzugekommen sind) muß sie gesichtet
werden, weil einige Default-Werte (z. B. "an audio file") durch generische
Defaults (z. B. "an audio") ersetzt worden sein werden.
"""

__all__ = (
        'type_string',  # thingy --> dict
        'pt_string',    # UnitraccThingy --> dict
        'plu_string',   # thingies --> dict
        'view2pt',
        'plu2tup',
        'pt2tup',
        'plu2import_label', # thingies -> Import thingy
        )

def pluralize(sing):
    """
    Gib die Pluralform des übergebenen Worts zurück
    (einfacher Algorithmus, für Message-IDs)

    >>> pluralize('thing')
    'things'
    >>> pluralize('thingy')
    'thingies'
    """
    if sing.endswith('s'):
        return sing
    elif sing.endswith('y'):
        return sing[:-1] + 'ies'
    else:
        return sing + 's'

def _a_sing(sing):
    """
    Nur für die Generierung des Honigtopfs
    >>> _a_sing('file')
    'a file'
    >>> _a_sing('audio')
    'an audio'
    """
    if sing[0] in 'aeiou':
        return 'an '+sing
    return 'a '+sing

def mktup(sing):
    """
    Tupel-Factory fuer 'Eigene Artikel'

    >>> mktup('thingy')
    ('UnitraccThingy', 'thingy', 'thingies')
    """
    return ('Unitracc%s' % sing.capitalize(),
            sing,
            pluralize(sing),
            )

def mkdict(pt, sing, plu):
    """
    für pt_string, plu_string
    """
    assert ' ' not in plu
    assert isinstance(pt, basestring)
    Sing = sing.capitalize()
    return {'portal_type': pt,
            'thingy': sing,
            'Thingy': Sing,
            'UnitraccThingy': pt,
            'thingies': plu,
            'Thingies': '%(pt)s_plural' % locals(),
            'a_thingy': 'a %(sing)s' % locals(),
            # 'filter': mkfilter(pt), # ['portal_type=...']
            'my-thingies': 'my-%(plu)s' % locals(),
            'our-thingies': 'our-%(plu)s' % locals(),
            'Own thingies': 'Own %(plu)s' % locals(),
            'Our thingies': 'Our %(plu)s' % locals(),
            'New thingy': 'New %(sing)s' % locals(),
            'add_url': '/@@temp/add%(Sing)s' % locals(),
            'add_text': 'Add new %(sing)s' % locals(),
            'import_text': 'Import %(plu)s via XML' % locals(),
            'unitraccthingy_view': 'unitracc%(sing)s_view' % locals(),
            }

def mkview(pt):
    """
    >>> mkview('UnitraccThingy')
    'unitraccthingy_view'
    """
    return '%s_view' % pt.lower()

type_string = {}    # thingy --> dict
pt_string = {}      # UnitraccThingy --> dict
plu_string = {}     # thingies --> dict
view2pt = {}        # unitraccthingy_view --> UnitraccThingy
view2plu = {}       # unitraccthingy_view --> thingies
plu2tup = {}
pt2tup = {}
plu2import_label = {}
for word in ('news',
             'article',
             'event',
             'image',
             'table',
             'glossary',
             'literature',
             'formula',
             'standard',
             'animation',
             'video',
             'audio',
             'course',
             'binary',
             ):
    pt, sing, plu = mktup(word)
    dic = mkdict(pt, sing, plu)
    type_string[sing] = dic
    pt_string[pt] = dic
    plu_string[plu] = dic
    view = mkview(pt)
    if not view in view2pt:
        view2pt[view] = pt
        view2plu[view] = plu
    plu2tup[plu] = ((dic['Own thingies'],
                     dic['my-thingies'],
                     ),
                    (dic['Our thingies'],
                     dic['our-thingies'],
                     ))
    pt2tup[pt] = plu2tup[plu]
    plu2import_label[plu] = 'Import %(thingy)s' % dic


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    from os.path import sep, join, normpath, dirname, splitext, basename
    base = splitext(basename(__file__))[0]
    prog = base + '.py'
    href = '/'.join(('..', '..', prog))
    fn = join(dirname(__file__), 'i18n', 'honeypot', base+'.html')
    HEAD = """<html>
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title lang="de">i18n-Honigtopf für %(base)s.py</title>
    </head>
    <body>
    <h1 lang="de">i18n-Honigtopf für <tt>%(base)s.py</tt></h1>
    <p>Generiert durch Aufruf von <tt><a href="%(href)s">Products/unitracc/%(prog)s</a></tt></p>
    <p>Bei neuer Generierung bitte stets sichten und
    unbeabsichtigte Änderungen revertieren!
    </p>
    <h1>Zeichenketten</h1>\n""" % locals()
    fo = open(fn, 'w')
    fo.write(HEAD)
    keys = sorted(pt_string.keys())

    def make_def(key, dic, default=None):
        res = ['<dt><tt>%(key)s</tt></dt>' % locals()]
        liz = ['<dd><tt ']
        if default is None:
            liz.extend(['i18n:translate="">',
                        dic[key],
                        ])
        else:
            liz.extend(['i18n:translate="%s">' % dic[key],
                        default,
                        ])
        liz.append('</tt></dd>')
        res.extend([''.join(liz), ''])
        return '\n    '.join(res)

    for key in keys:
        dic = pt_string[key]
        fo.write('  <h2>%(portal_type)s</h2>\n  <dl>\n    ' % dic)
        fo.write(make_def('portal_type', dic, dic['Thingy']))
        Plu = pluralize(dic['Thingy'])
        fo.write(make_def('Thingies', dic, Plu))
        plu = Plu.lower()
        fo.write(make_def('Own thingies', dic, 'Own '+plu))
        fo.write(make_def('Our thingies', dic, 'Our '+plu))
        fo.write(make_def('a_thingy', dic, _a_sing(dic['thingy'])))
        fo.write(make_def('add_text', dic))
        fo.write(make_def('New thingy', dic, dic['New thingy']))
        fo.write(make_def('import_text', dic,
                          'Import %s via XML' % pluralize(dic['thingy'])))
        fo.write('</dl>\n')
    fo.write('</body></html>\n')
    print '%(fn)s neu geschrieben; bitte sichten!' % locals()
    if 0 and 'Beispiel für Docstring generieren':
        from pprint import pprint
        print '## lesbar, zur Dokumentation:'
        pprint(type_string['article'])
        print
        print '## für Doctest:'
        print ">>> sorted(type_string['article'].items())"
        print sorted(type_string['article'].items())
        print

        def print_test(dicname, key):
            print '>>> %(dicname)s[%(key)r]' % locals()
            print repr(globals()[dicname][key])

        print_test('plu2tup', 'articles')
        print_test('pt2tup', 'UnitraccArticle')
        print_test('plu2import_label', 'articles')
        print_test('view2plu', 'unitraccarticle_view')
