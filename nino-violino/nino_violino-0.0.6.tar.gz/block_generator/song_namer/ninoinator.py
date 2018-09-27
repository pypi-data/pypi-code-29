import haikunator


class Ninoinator(haikunator.Haikunator, object):
    _verbs = [
        'aching', 'ageing', 'aging', 'aping', 'awing', 'axing', 'baaing', 'basing', 'biking', 'boning', 'bring', 'buying', 'caging', 'caking', 'caring', 'cluing', 'coking', 'coning', 'cooing', 'coving', 'cozing', 'cubing', 'cuing', 'curing', 'dating', 'dazing', 'diking', 'dining', 'doling', 'doming', 'doping', 'dosing', 'dyking', 'eyeing', 'eying', 'faking', 'faming', 'faring', 'fating', 'feeing', 'feting', 'fifing', 'fiking', 'frying', 'fuming', 'fusing', 'fuzing', 'gaging', 'gaping', 'gating', 'gazing', 'giving', 'gluing', 'guying', 'hading', 'hating', 'hewing', 'hieing', 'hiking', 'hiring', 'hiving', 'hoeing', 'holing', 'hoping', 'hying', 'isling', 'jading', 'japing', 'jiving', 'joking', 'kiting', 'laving', 'lazing', 'liming', 'loping', 'luring', 'lying', 'lysing', 'mazing', 'miking', 'miming', 'miring', 'mixing', 'mooing', 'moping', 'muring', 'muting', 'naging', 'noting', 'oozing', 'pacing', 'paging', 'piing', 'piking', 'plying', 'poking', 'poling', 'raging', 'reding', 'riving', 'rosing', 'ruing', 'sawing', 'shying', 'siting', 'sowing', 'spying', 'suing', 'taring', 'teeing', 'tiring', 'toning', 'toping', 'tying', 'typing', 'urging', 'using', 'vising', 'voting', 'wading', 'waving', 'wifing', 'witing', 'wiving', 'wyting'
    ]
    

    def haikunate(self, delimiter='-', token_length=4, token_hex=False, token_chars='0123456789'):
        haiku = super(Ninoinator, self).haikunate(delimiter, token_length, token_hex, token_chars)
        haiku = self._random_element(self._verbs) + delimiter + haiku
        return haiku

    ninoinate = haikunate
