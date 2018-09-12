class LabelRangesIndexEncoder:
    def __init__(self, labels, use_other_q=True):
        self.use_other_q = use_other_q
        self.labels = labels + (['Other'] if use_other_q else [])

    def encode(self, index, ranges):
        encoded = [0 for l in self.labels]
        for rng in ranges:
            if index in rng:
                encoded[self.labels.index(rng.name)] = 1

        if 1 not in encoded and self.use_other_q:
            encoded[-1] = 1
        return encoded
