from ..utils.constants import FASTA_CODEX, FASTA_DECODEX
class FastaCharacterEncoder:
    def __init__(self, u=False, tandem_repeats=False):
        self.u = u
        self.tandem_repeats = tandem_repeats

    def encode(self, char:str) -> list:
        lookup_char = list(char.lower())[0]

        if not self.u:
            lookup_char = lookup_char.replace('u', 't')
            encoded = FASTA_CODEX[lookup_char]
        elif lookup_char == 'u':
            encoded = [0,0,0,0,1]
        else:
            encoded = FASTA_CODEX[lookup_char]

        if self.u:
            encoded += [1] if lookup_char in 'uykwbdhn' else [0]
        if self.tandem_repeats:
            encoded += [1] if char.islower() else [0]
        return encoded


    def decode(self, arr:list) -> str:
        core = arr[:3] # take first four values (a,c,t,g)
        char = FASTA_DECODEX[tuple(core)]

        # the first four values are all zero and the fifth is 1 then its u
        if self.u and char == '-' and arr[4] == 1: return 'u'

        # tr will always be last
        if self.tandem_repeats and not arr[-1]:  char = char.upper()
        return char
