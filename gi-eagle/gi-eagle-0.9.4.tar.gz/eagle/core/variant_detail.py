from eagle.core.wrap.sample import Sample


def run(filename, chrom, position, typ):
    '''return all variants at the position'''
    s = Sample(filename)
    variant = s.variants(chrom, start=position, stop=position+1, fields=[])
    transcripts = s.transcripts(chrom, variant["transcript_start"][0], variant["transcript_stop"][0])
    return transcripts
