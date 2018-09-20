import numpy

from empdist.empirical_distributions import EmpiricalDistribution
from .constants import *

def cdf_to_pdf(cdf):
    """
    Converts the sampled values of a cumulative distribution function to the values of a probability
    distribution function at those same points.


    :param cdf:
    :return:
    """
    padded_cdf = numpy.zeros(len(cdf) + 1, dtype=cdf.dtype)
    padded_cdf[1:] = cdf
    pdf = numpy.diff(padded_cdf)
    return pdf


def pdf_to_cdf(pdf):
    """
    Converts the sampled values of a probability distribution function to the values of a cumulative
    distribution function at those same points.


    :param pdf:
    :return:
    """
    cdf = numpy.cumsum(pdf)
    return cdf


def distribution_minimum(distro_1, distro_2):
    """
    Given two EmpiricalDistribution instances, return an EmpiricalDistribution instance containing the expected
    distribution of an element-wise minimum operation between the *independent* random variables modeled by the input
    distributions.


    :param distro_1:
    :param distro_2:
    :return:
    """
    if distro_1.num_bins == distro_2.num_bins and not numpy.abs(distro_1.bin_starts - distro_2.bin_starts).sum() > 0:
        common_bins = distro_1.bin_midpoints
        joint_support = distro_1.support
    else:
        joint_support = min(distro_1.a, distro_2.a), max(distro_2.b, distro_2.b)
        new_num_bins = (distro_1.num_bins + distro_2.num_bins) * RESAMPLE_FACTOR
        common_bins = numpy.linspace(*joint_support, num=new_num_bins)

    pred_cdf = distro_1.cdf(common_bins) + distro_2.cdf(common_bins) - (
            distro_1.cdf(common_bins) * distro_2.cdf(common_bins))
    pred_pdf = cdf_to_pdf(pred_cdf)
    pred_frequencies = pred_pdf / pred_pdf.sum()

    return EmpiricalDistribution(frequencies=pred_frequencies, support=joint_support)


def distribution_maximum(distro_1, distro_2):
    """
    Given two EmpiricalDistribution instances, return an EmpiricalDistribution instance containing the expected
    distribution of an element-wise minimum operation between the *independent* random variables modeled by the input
    distributions.


    :param distro_1:
    :param distro_2:
    :return:
    """
    if distro_1.num_bins == distro_2.num_bins and not numpy.abs(distro_1.bin_starts - distro_2.bin_starts).sum() > 0:
        common_bins = distro_1.bin_midpoints
        joint_support = distro_1.support
    else:
        joint_support = min(distro_1.a, distro_2.a), max(distro_2.b, distro_2.b)
        new_num_bins = (distro_1.num_bins + distro_2.num_bins) * RESAMPLE_FACTOR
        common_bins = numpy.linspace(*joint_support, num=new_num_bins)

    pred_cdf = distro_1.cdf(common_bins) * distro_2.cdf(common_bins)

    pred_pdf = cdf_to_pdf(pred_cdf)
    pred_frequencies = pred_pdf / pred_pdf.sum()

    return EmpiricalDistribution(frequencies=pred_frequencies, support=joint_support)


def predict_distributions_independent_sums(input_empirical_distribution,
                                           max_sample_size):
    """
    Given an EmpiricalDistribution instance generated from a population sample, return a dictionary,
    keyed by sample size, of EmpiricalDistribution instances representing the expected distributions
    of the sum of samples taken from that population of sizes [1, :param:`max_sample_size`].

    :param input_empirical_distribution:
    :param max_sample_size:
    :return:
    """

    assert max_sample_size >= 1

    empirical_distros_by_region_size = {1: input_empirical_distribution}

    for sample_size in range(2, max_sample_size + 1):
        empirical_distros_by_region_size[sample_size] = empirical_distros_by_region_size[
                                                            sample_size - 1] + input_empirical_distribution

    return empirical_distros_by_region_size


def predict_distributions_independent_means(input_empirical_distribution,
                                            max_sample_size):
    """
    Given an EmpiricalDistribution instance generated from a population sample, return a dictionary,
    keyed by sample size, of EmpiricalDistribution instances representing the expected distributions
    of the mean of samples taken from that population of sizes [1, :param:`max_sample_size`].

    :param input_empirical_distribution:
    :param max_sample_size:
    :return:
    """
    assert max_sample_size >= 1

    sum_distributions = predict_distributions_independent_sums(
        input_empirical_distribution=input_empirical_distribution, max_sample_size=max_sample_size)

    return {sample_size: distribution / sample_size for sample_size, distribution in sum_distributions.items()}


def predict_distributions_independent_mins(input_empirical_distribution,
                                           max_sample_size):
    """
    Given an EmpiricalDistribution instance generated from a population sample, return a dictionary,
    keyed by sample size, of EmpiricalDistribution instances representing the expected distributions
    of the minimum of samples taken from that population of sizes [1, :param:`max_sample_size`].

    :param input_empirical_distribution:
    :param max_sample_size:
    :return:
    """
    assert max_sample_size >= 1

    empirical_distros_by_region_size = {1: input_empirical_distribution}

    for sample_size in range(2, max_sample_size + 1):
        empirical_distros_by_region_size[sample_size] = distribution_minimum(empirical_distros_by_region_size[
                                                                                 sample_size - 1],
                                                                             input_empirical_distribution)

    return empirical_distros_by_region_size


def predict_distributions_independent_maxes(input_empirical_distribution,
                                            max_sample_size):
    """
    Given an EmpiricalDistribution instance generated from a population sample, return a dictionary,
    keyed by sample size, of EmpiricalDistribution instances representing the expected distributions
    of the maximum of samples taken from that population of sizes [1, :param:`max_sample_size`].

    :param input_empirical_distribution:
    :param max_sample_size:
    :return:
    """
    assert max_sample_size >= 1

    empirical_distros_by_region_size = {1: input_empirical_distribution}

    for sample_size in range(2, max_sample_size + 1):
        empirical_distros_by_region_size[sample_size] = distribution_maximum(empirical_distros_by_region_size[
                                                                                 sample_size - 1],
                                                                             input_empirical_distribution)

    return empirical_distros_by_region_size
