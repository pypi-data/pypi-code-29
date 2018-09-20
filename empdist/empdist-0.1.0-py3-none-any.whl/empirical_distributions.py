import numpy
import pandas
from scipy.signal import convolve

from .constants import *


class EmpiricalDistribution:
    _BIN_OFFSET = -1

    def __init__(self, frequencies, support):
        assert support[1] >= support[0]

        self.a, self.b = support  # ToDo: Add setter methods to a and b properties to do type-checking
        self.num_bins = len(frequencies)

        self._frequencies = numpy.array(frequencies)
        self._cdf_values = numpy.cumsum(self._frequencies)
        self._sf_values = numpy.cumsum(self._frequencies[::-1])[
                          ::-1]  # Double reversal needed to avoid numerical round-off errors close to 1.

    @staticmethod
    def fit(data, bins='auto', pseudocount=DEFAULT_PSEUDOCOUNT):
        data = numpy.array(data)
        assert len(data) > 0, 'Data must have non-zero length'
        assert sum(numpy.isnan(data)) == 0, 'Data must not contain NaN'
        assert sum(numpy.isinf(data)) == 0, 'Data must not contain inf'
        assert sum(numpy.isneginf(data)) == 0, 'Data must not contain neginf'
        # print(bins)
        counts, bins = numpy.histogram(data, bins=bins)
        # print(bins)
        support = bins[0], bins[-1]
        counts += pseudocount
        frequencies = counts / counts.sum()

        return {'support': support, 'frequencies': frequencies}

    @classmethod
    def from_data(cls, data, bins='auto', pseudocount=0):
        return cls(**cls.fit(data=data, bins=bins, pseudocount=pseudocount))

    @property
    def frequencies(self):
        return pandas.Series(self._frequencies, index=self.bin_starts)

    @property
    def densities(self):
        return pandas.Series(self._frequencies / self.bin_size, index=self.bin_midpoints)

    @property
    def cdf_series(self):
        return pandas.Series(self._cdf_values, index=self.bin_midpoints)

    @property
    def support_size(self):
        return self.b - self.a

    @property
    def support(self):
        return self.a, self.b

    @property
    def bin_size(self):
        return (self.b - self.a) / self.num_bins

    @property
    def bin_starts(self):
        return numpy.linspace(self.a, self.b - self.bin_size, num=self.num_bins)

    @property
    def bin_midpoints(self):
        return self.bin_starts + self.bin_size / 2

    @property
    def bin_ends(self):
        return self.bin_starts + self.bin_size

    def __neg__(self):
        return type(self)(frequencies=self._frequencies[::-1], support=(-self.b, -self.a))

    def __add__(self, other):
        try:  # assume other is another EmpiricalDistribution
            new_frequencies = convolve(other.frequencies, self._frequencies, mode='full', method=CONVOLVE_METHOD)
            new_a = self.a + other.a
            new_b = self.b + other.b
            result = type(self)(frequencies=new_frequencies, support=(new_a, new_b))

        except AttributeError:  # if not, treat it as a scalar
            result = self.copy()
            result.a += other
            result.b += other

        return result

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return self.__add__(-other)

    def __rsub__(self, other):
        return -self.__add__(other)

    def __mul__(self, other):
        # Currently only supports scalars, multiplication by other distributions not implemented yet.
        result = self.copy()
        result.a = self.a * other
        result.b = self.b * other
        return result

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        # Currently only supports scalars, division by other distributions not implemented yet.
        result = self.copy()
        result.a = self.a / other
        result.b = self.b / other
        return result

    def copy(self):
        return type(self)(frequencies=self._frequencies, support=self.support)

    def mean(self):
        """
        Returns the expectation of the random variable described by this distribution
        """
        return numpy.sum(self._frequencies * self.bin_midpoints)

    def std(self):
        """
        Returns the standard deviation of the random variable described by this distribution
        """
        m = self.mean()
        return numpy.sqrt((((self.bin_midpoints - m) ** 2) * self.frequencies).sum())

    def resample(self, new_num_bins):
        """
        Return a copy where the frequencies have been re-sampled into :param new_num_bins: number of bins.
        """
        new_frequencies = numpy.interp(x=numpy.linspace(*self.support, new_num_bins),
                                       xp=numpy.linspace(*self.support, self.num_bins), fp=self.frequencies)
        new_frequencies /= new_frequencies.sum()

        return type(self)(frequencies=new_frequencies, support=self.support)

    def pdf(self, x):
        """
        Returns the PDF evaluated at the points in :param:`x`
        as the density of the overlapping bins.
        """
        freq_array = self._frequencies
        return freq_array[numpy.maximum(0, numpy.searchsorted(self.bin_starts, x) + self._BIN_OFFSET)] / self.bin_size

    def cdf(self, x):
        """
        Returns the CDF evaluated at the points in :param:`x`
        """
        return self._cdf_values[numpy.maximum(0, numpy.searchsorted(self.bin_starts, x) + self._BIN_OFFSET)]

    def sf(self, x):
        """
        Return the survival function (1 - cdf) at :param x:
        """
        return self._sf_values[numpy.maximum(0, numpy.searchsorted(self.bin_starts, x) + self._BIN_OFFSET)]

    def isf(self, x):
        """
        Return the inverse survival function (1 - sf) at :param x:
        """
        return 1 - self._sf_values[numpy.maximum(0, numpy.searchsorted(self.bin_starts, x) + self._BIN_OFFSET)]

    def logsf(self, x):
        # ToDo: Build in standard approximation (should never return 0 p-values)
        return numpy.log(numpy.maximum(self.sf(x), MIN_PVALUE))
