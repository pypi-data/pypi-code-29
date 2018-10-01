'''determine the sample's variants in a given region'''

import argparse
from collections import defaultdict, namedtuple

import numpy as np

from eagle.core.wrap.sample import Sample
from eagle.core.wrap.results import Result

Region = namedtuple("Region", "chrom start stop")


def parse_region(r):
    '''parse the region string and return region namedtuple'''
    if r.upper().startswith("CHR"):
        r = "CHR" + r[3:]
    chrom, position_range = r.split(":")
    if position_range.find("-") > -1:
        start, stop = position_range.split("-")
    else:
        start = int(position_range)
        stop = position_range
        print(start, stop)
    return Region(chrom, int(start), int(stop)+1)


def run(samples, regions):
    sample_objects = [Sample(sample) for sample in samples]

    d = defaultdict(lambda: Result())
    fields = ["key", "qual", "ref", "rsid", "effect",
              "transcript_start", "transcript_stop",
              "context", "mq", "alt_count", "depth"]
    for s in sample_objects:
        for region in regions:
            if not s.has_variants(chrom=region.chrom, start=region.start,
                                  stop=region.stop):
                continue
            variants = s.variants(chrom=region.chrom, start=region.start,
                                  stop=region.stop, fields=fields, decodekey=True)
            for v in variants:
                key = v["key"]
                item = d[key]
                item.add_data(v, s)

    return d.values()


index_to_base = "ACGTMIDE"

def out(variants):
    for var in variants:
        for v in var:
            print(v["chrom"], v["position"], v["qual"], v["mq"], chr(v["ref"]),
                  index_to_base[v["typ"]], sep="\t")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("sample")
    parser.add_argument("region")
    args = parser.parse_args()

    regions = [parse_region(args.region)]
    out(run(args.sample, regions))


if __name__ == "__main__":
    main()
