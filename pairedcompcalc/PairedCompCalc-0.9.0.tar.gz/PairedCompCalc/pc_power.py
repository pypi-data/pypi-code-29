"""Functions for power estimation for planning a paired-comparison experiment,
using simulations of the experiment.

*** Definition of result measures:
p_true_pos = probability that the estimated quality difference is > 0,
    given the anticipated true q_diff and q_std.
p_false_pos = probability that the estimated quality difference given true ZERO difference,
    is greater than the estimated quality difference given the true positive difference.
Thus, these two measures are not symmetric.

NOTE: The power result (p_true_pos, p_false_pos) for a RANDOM INDIVIDUAL
depends mainly on q_diff, q_std, and n_pres,
and improves very little with increasing number of subjects.

Given a population mean q_diff, and inter-individual standard deviation q_std,
it may be IMPOSSIBLE to reach a high value of p_true_pos for a RANDOM INDIVIDUAL in the population,
even if the quality parameters could be measured exactly for each test subject.

However, he power results for the population MEAN improves with the number of subjects.
Therefore, the function estimate_n_subjects(...) works only for the population MEAN.

NOTE: The accuracy of the resulting power parameters is quite crude.
Better accuracy can be achieved by increasing the parameter n_sim
in function calls, at a cost of longer computation time.
Good to run the power calculation twice, to show the range of estimated results.

Arne Leijon, 2018-08-08
"""
# ************** p_false_pos is quite variable, estimate exact power, too ?? **************

import numpy as np
import logging

from .pc_simulator import PairedCompSimulator
from .pc_model import PairedCompResultSet

logger = logging.getLogger(__name__)


# ------------------------------------------------------------------------------
def estimate_n_subjects(pcf, q_diff, q_std, n_pres,
                        n_min=3, n_max=50,
                        p_true_pos=0.9, p_false_pos=0.1,
                        n_sim=3):
    """Estimate required number of test participants,
    to achieve a desired probability of correct detection of a difference (hit),
    AND a desired maximal probability of false positive detection.
    :param pcf: single PairedCompFrame instance defining experimental layout
    :param q_diff: scalar assumed mean quality difference in a population
    :param q_std: scalar assumed inter-individual standard deviation of q_diff in the population
    :param n_pres: number of paired-comparison presentations for each subject
    :param n_min: (optional) minimal feasible number of test participants
        NOTE: cannot be less than 3 for predictive population models
    :param n_max: (optional) maximal feasible number of test participants
    :param p_true_pos: (optional) scalar desired power of the experiment,
        i.e., probability of correct detection of the true positive difference.
    :param p_false_pos: (optional) scalar maximal probability of false positive detection,
        given zero true difference.
    :param n_sim: (optional) number of averaged simulation results for each estimate.

    :return: scalar integer n = required number of test participants.

    Method: Simple bisection. Crude sampled approximation
    """
    # ---------------------------------------
    def p_fcn(n):
        """Calling interface to criterion function
        :param n: tentative number of subjects
        :return: tuple (p1, p0) = (true positive, false positive)
        """
        (p1, p0) = np.mean([_cred_ab_mean(pcf, q_diff, q_std, n, n_pres, i, n_sim)
                            for i in range(n_sim)], axis=0)
        logger.info(f'Estimated p_true_pos = {p1:.1%}, p_false_pos = {p0:.1%} with {n} subjects')
        return p1, p0
    # ---------------------------------------
    (p1_max, p0_max) = p_fcn(n_max)
    # p_min = p_fcn(n_min)
    while p_true_pos < p1_max and p0_max < p_false_pos and n_max - n_min > 1:
        n_mid = (n_min + n_max) // 2  # bisection
        (p1_mid, p0_mid) = p_fcn(n_mid)
        if p1_mid < p_true_pos or p0_mid > p_false_pos:
            # keep upper interval
            n_min = n_mid
        else:
            # keep lower interval
            n_max = n_mid
            (p1_max, p0_max) = (p1_mid, p0_mid)
    return n_max


def power_ab_individual(pcf, q_diff, q_std, n_subjects, n_pres,
                        n_sim=10):
    """
    Calculate (prob_hit, prob_false_alarm) for given test conditions
    for an individual subject in the simulated population
    :param pcf: single PairedCompFrame instance to define experimental layout.
    :param q_diff: scalar assumed mean quality difference between two systems in a population
    :param q_std: scalar assumed inter-individual standard deviation of q_diff in the population
    :param n_subjects: number of test participants
    :param n_pres: number of pair presentations for each participant
    :param cred_fcn: (optional) function variant to calculate power
    :param n_sim: (optional) number of simulations for each calculated credibility value

    :return: array [p_true_pos, p_false_alarm], where
        p_true_pos = probability of correct detection of the difference.
        p_false_alarm = probability of incorrect indication of a difference, when systems are equal
    """
    return np.mean([_cred_ab_individual(pcf, q_diff, q_std, n_subjects, n_pres,
                                        i, n_sim)
                    for i in range(n_sim)], axis=0)


def power_ab_mean(pcf, q_diff, q_std, n_subjects, n_pres,
                  n_sim=10):
    """
    Calculate (prob_hit, prob_false_alarm) for given test conditions
    for the mean quality difference in the simulated population
    :param pcf: single PairedCompFrame instance to define experimental layout.
    :param q_diff: scalar assumed mean quality difference between two systems in a population
    :param q_std: scalar assumed inter-individual standard deviation of q_diff in the population
    :param n_subjects: number of test participants
    :param n_pres: number of pair presentations for each participant
    :param cred_fcn: (optional) function variant to calculate power
    :param n_sim: (optional) number of simulations for each calculated credibility value

    :return: array [p_true_pos, p_false_alarm], where
        p_true_pos = probability of correct detection of the difference.
        p_false_alarm = probability of incorrect indication of a difference, when systems are equal
    """
    return np.mean([_cred_ab_mean(pcf, q_diff, q_std, n_subjects, n_pres,
                                  i, n_sim)
                    for i in range(n_sim)], axis=0)


# --------------------------------------- Module help functions:

def _cred_ab_individual(pcf, q_diff, q_std, n_subjects, n_pres,
                        it, n_it):
    """Calculate one pair of credibility results
    for the quality difference for a random INDIVIDUAL in the simulated population.
    :param pcf: single PairedCompFrame instance to define experimental layout.
    :param q_diff: scalar assumed mean quality difference between two systems in a population
    :param q_std: scalar assumed inter-individual standard deviation of q_diff in the population
    :param n_subjects: number of test participants
    :param n_pres: number of pair presentations for each participant
    :param it: current iteration round
    :param n_it: total number of iteration rounds

    :return: tuple(p_true_pos, p_false_pos) where
        p_true_pos = prob[ q_B - q_A > 0 | given true diff = q_diff
        p_false_pos  = prob[ (q_B - q_A | true diff = 0) > (q_B - q_A | true diff = q_diff) ]
    """
    logger.info(f'Done {it} of {n_it} simulations with {n_subjects} subjects')
    pcm_d = _one_sim_ab(pcf, q_diff, q_std, n_subjects, n_pres)  # test group
    pcm_0 = _one_sim_ab(pcf, 0., q_std, n_subjects, n_pres)  # ref group with zero difference
    pred_d = pcm_d.predictive_population_individual()
    pred_0 = pcm_0.predictive_population_individual()
    q_d = pred_d.models[''][pcf.attributes[0]].quality_samples[:, 0, 1]
    q_0 = pred_0.models[''][pcf.attributes[0]].quality_samples[:, 0, 1]
    return ((0.5 + sum(q_d > 0.)) / (1 + len(q_d)),
            (0.5 + sum(q_0 > q_d)) / (1 + len(q_d)))


def _cred_ab_mean(pcf, q_diff, q_std, n_subjects, n_pres,
                  it=0, n_it=0):
    """Calculate one pair of credibility results
    for the MEAN quality difference in the simulated population.
    :param pcf: single PairedCompFrame instance to define experimental layout.
    :param q_diff: scalar assumed mean quality difference between two systems in a population
    :param q_std: scalar assumed inter-individual standard deviation of q_diff in the population
    :param n_subjects: number of test participants
    :param n_pres: number of pair presentations for each participant
    :param it: current iteration round
    :param n_it: total number of iteration rounds

    :return: tuple(p_true_pos, p_false_pos) where
        p_true_pos = prob[ q_B - q_A > 0 | given true diff = q_diff
        p_false_pos  = prob[ (q_B - q_A | true diff = 0) > (q_B - q_A | true diff = q_diff) ]
    """
    if n_it > 0:
        logger.info(f'Done {it} of {n_it} simulations with {n_subjects} subjects')
    pcm_d = _one_sim_ab(pcf, q_diff, q_std, n_subjects, n_pres)  # test group
    pcm_0 = _one_sim_ab(pcf, 0., q_std, n_subjects, n_pres)  # ref group with zero difference
    pred_d = pcm_d.predictive_population_mean()
    pred_0 = pcm_0.predictive_population_mean()
    q_d = pred_d.models[''][pcf.attributes[0]].quality_samples[:, 0, 1]
    q_0 = pred_0.models[''][pcf.attributes[0]].quality_samples[:, 0, 1]
    return ((0.5 + sum(q_d > 0.)) / (1 + len(q_d)),
            (0.5 + sum(q_0 > q_d)) / (1 + len(q_d)))


def _one_sim_ab(pcf, q_diff, q_std, n_subjects, n_pres):
    """Simulate one subject group with given properties
    :param pcf: single PairedCompFrame instance to define experimental layout.
    :param q_diff: scalar assumed mean quality difference between two systems in a population
    :param q_std: scalar assumed inter-individual standard deviation of q_diff in the population
    :param n_subjects: number of test participants
    :param n_pres: number of pair presentations for each participant
    :return: one learned PairedCompResultSet
    """
    pcs = PairedCompSimulator(pcf,
                              quality_mean=[0., q_diff],
                              quality_std=q_std,
                              n_replications=n_pres // 2,
                              lapse_prob=0.)
    return PairedCompResultSet.learn(pcs.gen_dataset(n_subjects=n_subjects))
