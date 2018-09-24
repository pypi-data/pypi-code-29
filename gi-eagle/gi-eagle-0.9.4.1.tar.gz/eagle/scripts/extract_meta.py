import argparse
import pysam
from pybedtools import BedTool
from collections import defaultdict
import random
import sys
import h5py

def region_out(region):
    return "{}:{}-{}".format(*region)


def chr_append(c):
    if c.lower().startswith("chr"):
        c = c[3:]

    for c in (c, "chr" + c, "Chr" + c, "CHR" + c):
        yield c


def main(args):
    idxstats = [x.split("\t") for x in pysam.idxstats(args.bam).split("\n")]
    unmapped_reads = sum([int(s[3]) for s in idxstats if len(s) > 1])
    mapped_reads = sum([int(s[2]) for s in idxstats if len(s) > 1])

    f = pysam.Samfile(args.bam ,"r")

    references = f.header.references
    reference_length = sum([f.header.get_reference_length(c) for c in references])
    references = set(references)


    #get x,y reads
    reads_on_x = 0
    for c in chr_append("X"):
        if c in references:
            reads_on_x = f.header.get_reference_length(c)
            break

    reads_on_y = 0
    for c in chr_append("Y"):
        if c in references:
            reads_on_y = f.header.get_reference_length(c)
            break

    #get some stats from idxstats

    duplicate_reads = 0
    region_reads = 0
    base_count = 0
    base_looked_count = 0
    base_count_greater = defaultdict(int)

    # load the bedfile
    bed = BedTool(args.capturekit)

    #observed_region_length = 0

    for region in bed:
        if random.random() > args.samplerate:
            continue
        region_chrom, region_start, region_end = region
        #print(region_chrom, region_start, region_end, sep="\t")

        if region_chrom not in references:
            if region_chrom.lower().startswith("chr"):
                region_chrom = region_chrom[3:] #remove the chrom

            print("WARNING: chromosome of", region_out(region), "not in contigs", end=" ", file=sys.stderr)

            # test for all combinations with chr
            if region_chrom in references:
                pass
            elif "chr" + region_chrom in references:
                region_chrom = "chr" + region_chrom
            elif "Chr" + region_chrom in references:
                region_chrom = "Chr" + region_chrom
            elif "CHR" + region_chrom in references:
                region_chrom = "CHR" + region_chrom
            else:
                print("no alternative found", file=sys.stderr)
                continue

            print("using", region_out((region_chrom, region_start, region_end)), file=sys.stderr)

        #observed_region_length += int(region_end) - int(region_start)

        for pileupIter in f.pileup(str(region_chrom),int(region_start),int(region_end), truncate=True):
            pileup_count = len([x for x in pileupIter.pileups if x.alignment.mapq >= 13 and not x.alignment.is_unmapped and not x.alignment.is_duplicate])
            #print(pileupIter.reference_name, pileupIter.reference_pos, pileup_count)
            base_count += pileup_count
            base_looked_count += 1
            for i in [0, 1, 5, 10, 20, 50, 100]:
                if pileup_count >= i:
                    base_count_greater[i] += 1

        for read in f.fetch(str(region_chrom),int(region_start),int(region_end)):
            region_reads += 1
            duplicate_reads += read.is_duplicate

            #if read.is_unmapped or read.is_duplicate or read.mapq < 13:
            #    continue

            # #determine covering bases
            # cigar = read.cigar
            #
            # for (t,length) in cigar:
            #     if t == 0: #match
            #         base_count += length
            #
            #  # remove overlapping bases of paired end reads
            # rend = read.qend + read.pos
            # if (read.tid == read.mrnm) and (read.pos < read.mpos) and (rend > read.mpos): # pairs overlap
            #     base_count -= (rend - read.mpos) # subtract overlap

#    print(base_count)
#    print(base_count_greater)
#    print(base_looked_count)


    def out(f, name, value):
        if f is None:
            print(name, value, sep="\t")
        else:
            f.attrs.create(name, str(value).encode())

    if len(args.w):
        f = h5py.File(args.w)
    else:
        f = None

    out(f, "All Reads", unmapped_reads + mapped_reads)
    out(f, "Duplication Rate", "{:.3f}".format(duplicate_reads / region_reads))
    out(f, "Mapping Rate", "{:.3f}".format(mapped_reads / (unmapped_reads + mapped_reads)))
    out(f, "Coverage", "{:.2f}".format(base_count / base_looked_count))
    for key, value in base_count_greater.items():
        if key == 0:
            continue
        out(f, f"Cov >= {key}", "{:.3f}".format(value / base_count_greater[0]))
    out(f, "_reads_on_x", reads_on_x)
    out(f, "_reads_on_y", reads_on_y)

    if f is not None:
        f.close()


def create_parser(parser):
    parser.add_argument("bam", help="a bam/sam/cram file")
    parser.add_argument("capturekit", help="a capturekit gff or bed file")
    parser.add_argument("--samplerate", help="only use this fraction of regions", default=1.0, type=float)
    parser.add_argument("-w", help="directly write the stats to this eagle file", default="")
    parser.set_defaults(func=main)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    create_parser(parser)
    args = parser.parse_args()

    main(args)
