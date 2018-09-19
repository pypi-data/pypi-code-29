from hashlib import blake2b
from itertools import product


class IdentifierMapper:
    def __init__(self, key):
        self.key = key
        nouns = [line.strip() for line in open('nounlist.txt')][:4096]
        self.noun_pairs = list(product(nouns, repeat=2))

    def __call__(self, identifier):
        hash_value = blake2b(
            identifier.encode('utf-8'),
            digest_size=3,
            key=self.key.encode(),
        ).digest()
        index = int.from_bytes(hash_value, byteorder='big')
        noun_pair = self.noun_pairs[index]
        return '_'.join(noun_pair)
