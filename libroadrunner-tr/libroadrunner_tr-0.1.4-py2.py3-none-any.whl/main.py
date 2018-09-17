from __future__ import print_function, division, absolute_import

from os.path import join

from roadrunner import RoadRunner

class SettingsParser:
    @classmethod
    def from_file(cls, file_name):
        p = SettingsParser()
        with open(file_name) as f:
            s = f.read()
        for line in s.splitlines():
            if line.startswith('start:'):
                p.start = float(line.split('start:')[1])
            elif line.startswith('duration:'):
                p.duration = float(line.split('duration:')[1])
            elif line.startswith('steps:'):
                p.steps = int(line.split('steps:')[1])
            elif line.startswith('variables:'):
                p.variables = [''.join(v.split(' ')) for v in line.split('variables:')[1].split(',')]
            elif line.startswith('absolute:'):
                p.absolute = float(line.split('absolute:')[1])
            elif line.startswith('relative:'):
                p.relative = float(line.split('relative:')[1])
            elif line.startswith('amount:'):
                p.amount = [''.join(v.split(' ')) for v in line.split('amount:')[1].split(',') if ''.join(v.split(' ')) != '']
            elif line.startswith('concentration:'):
                p.concentration = ['[{}]'.format(''.join(v.split(' '))) for v in line.split('concentration:')[1].split(',') if ''.join(v.split(' ')) != '']
        return p

class TestRunner:
    def run(self, d, n, o, l, v):
        settings_file = join(d,n,
                             '{n}-settings.txt'.format(n=n))
        settings = SettingsParser.from_file(settings_file)
        sbml_file = join(d,n,
                         '{n}-sbml-l{l}v{v}.xml'.format(n=n,l=l,v=v))
        r = RoadRunner(sbml_file)
        r.selections = ['time'] + settings.amount + settings.concentration
        results = r.simulate(settings.start, settings.duration, settings.steps+1)
        from pandas import DataFrame
        print(r.selections)
        DataFrame(results, columns=r.selections).to_csv(join(o,'.'.join([n,'csv'])), index=False, encoding='utf-8')
