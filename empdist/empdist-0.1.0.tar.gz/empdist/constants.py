import numpy

RESAMPLE_FACTOR = 10
DEFAULT_PSEUDOCOUNT = 0
MAX_PSCORE = 744.44007192138122
MIN_PVALUE = numpy.exp(-MAX_PSCORE)
CONVOLVE_METHOD = 'direct' # could try going back to auto if we include a 0 floor on the frequencies