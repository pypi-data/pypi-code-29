# -*- coding: utf-8 -*- äöü
# utils-Modul für userlog-Adapter

def sorted_items(dic):
    raw = dic.keys()
    sortable = []
    # Schlüssel für Gruppierung einfügen:
    for key in raw:
        if key in ('userId',
                   'username',
                   ):
            sortable.append((0, key))
        elif key.endswith('name'):
            sortable.append((1, key))
        elif key == 'email':
            sortable.append((2, key))
        elif key == 'by':
            sortable.append((9, key))
        elif key.endswith('password'):
            # Paßwörter nicht protokollieren!
            continue
        elif dic[key] is None:
            # Schlüssel mit leeren Werten ignorieren
            continue
        else:
            sortable.append((5, key))
    sortable.sort()
    return [(tup[1], dic[tup[1]])
            for tup in sortable
            ]
