i = [['Fe', 'Pt'], ['W'], ['W', 'Fe', 'Pt']]

def gen(species):
    slug = []

    def _chars_left():
        return 4 - sum([len(x) for x in slug])

    for s in species:
        if len(s) <= _chars_left():
            slug.append(s)

    slug += ['X'] * _chars_left()

    return slug

for s in i:
    print(gen(s))



