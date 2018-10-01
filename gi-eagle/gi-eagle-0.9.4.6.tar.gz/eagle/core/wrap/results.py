import numpy as np

class Result(dict):
    def __init__(self, *args, **kwargs):
        super(Result, self).__init__(*args, **kwargs)
        self.__dict__ = self

        self.samples = set()
        self.symbols = set()
        self.effect = 0
        self.qual = dict()
        self.maxqual = 0
        self.heterozygot = dict()
        self.rowheterozygot = 0
        self.minaf = 1.0
        self.maxaf = 0.0
        self.maximpact = 0

    def add_data(self, data, sample, position=None, chrom=None):
        self.chrom = chrom if chrom else data["chrom"]
        self.typ = data["typ"]
        self.position = position if position else data["position"]
        self.samples.add(sample.basename)
        transcripts = sample.transcripts(self.chrom,
                                    data["transcript_start"],
                                    data["transcript_stop"])
        self.symbols |= set(transcripts["gene_id"])  # r["gene_id"]
        self.effect |= data["effect"]
        self.qual[sample.basename] = int(data["qual"])
        self.maxqual = int(max(self.maxqual, data["qual"]))
        self.heterozygot[sample.basename] = data["het"]
        self.rowheterozygot |= 1 if data["het"] else 2
        self.ref = chr(data["ref"])
        self.context = data["context"]
        self.mq = data["mq"]
        self.minaf = min(self.minaf, data["alt_count"] / data["depth"])
        self.maxaf = max(self.maxaf, data["alt_count"] / data["depth"])
        self.maximpact = max(self.maximpact, np.max(transcripts["impact"]))

