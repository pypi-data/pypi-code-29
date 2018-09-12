class ProbabilityClassIndexEncoder:
    def __init__(self,
        classes,
        other_class_q=True
    ):
        self.other_class_q = other_class_q
        self.classes = classes+["Other"] if other_class_q else classes

    def encode(self, index, ranges):
        encoded = [0 for c in self.classes]
        for rng in ranges:
            if index in rng:
                encoded[self.classes.index(rng.name)] = 1


        if 1 not in encoded and not self.other_class_q:
            raise ValueError(f'''
                Index {index} could not be encoded into one of the
                classes {self.classes} given the classe ranges {ranges}
            ''')
        if 1 not in encoded:
            encoded[-1] = 1

        s = sum(encoded)
        encoded = [e / s for e in encoded]

        return encoded
