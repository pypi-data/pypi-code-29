from dataclasses import dataclass
import typing


@dataclass
class KeyEnsurer:
    """Dataclass that allows to deeply check that keys exist.
    """

    data: typing.Union[typing.Dict, 'collections.OrderedDict[str, typing.Any]']
    required_keys: typing.List[str]

    missing = []

    def key_exists(self, data, key):
        rest = ''
        if '.' in key:
            key, rest = key.split('.', 1)
        if key not in data:
            return False
        if rest:
            return self.key_exists(data[key], rest)
        return True

    def validate(self):
        self.missing = []
        for key in self.required_keys:
            if not self.key_exists(self.data, key):
                self.missing.append(key)
        return len(self.missing) == 0
                