class OneHotCharacterEncoder:
    def __init__(self, chars):
        self.chars = chars
    def encode(self, char):
        i = self.chars.index(char)
        return [0 if c != i else 1 for c in range(len(self.chars))]
    def decode(self, arr):
        return self.chars[arr.index(1)]
