"""Power estimation for planning a paired-comparison experiment,
using simulations of an experiment with exactly TWO test systems, A and B.

The power of the test can be estimated for detecting either
a quality difference for a random individual in the population, or
the mean quality difference in the population.

*** Usage example:

*1: Guess true distribution of anticipated difference B - A > 0:

q_diff = a preliminary estimate of the true MEAN quality difference in the population,
q_std = a preliminary estimate of INTER-INDIVIDUAL STANDARD DEVIATION of q_diff,
(both defined in Thurstone d-prime scale units)

*2: Specify intended test procedure in a PairedCompFrame instance

*3: Choose desired power parameters (p_true_pos, p_false_pos),
    if different from the default values (0.9, 0.1)

*4: Estimate an approximate number of participants needed,
    by calling estimate_n_subjects

*5: Estimate the resulting test power more accurately,
    by calling power_ab_mean

If desired, estimate the power to detect the quality difference
    for a single individual randomly drawn from the population,
    by calling power_ab_individual

NOTE: The power calculations are rather slow, because they
run complete model learning procedures for many simulated data sets.
The script might take one-half hour to run.

*** Definition of result measures

p_true_pos = probability that the estimated quality difference is > 0,
    given the anticipated true q_diff and q_std in the population.
p_false_pos = probability that the estimated quality difference given true ZERO difference,
    is greater than the estimated quality difference given the true positive difference.
Thus, these two measures are not symmetric.

NOTE: The power result (p_true_pos, p_false_pos) for a RANDOM INDIVIDUAL
depends mainly on q_diff, q_std, and n_pres,
and improves very little with increasing number of subjects.

Given a population mean q_diff, and inter-individual standard deviation q_std,
it may be IMPOSSIBLE to reach a high value of p_true_pos for a RANDOM INDIVIDUAL in the population,
even if the quality parameters could be measured exactly for each test subject.

However, the power results for the population MEAN improves with the number of subjects.
Therefore, the function estimate_n_subjects(...) works only for the population MEAN.

NOTE: The accuracy of the resulting power parameters is quite crude.
Better accuracy can be achieved by increasing the parameter n_sim
in function calls, at a cost of longer computation time.
It is a good practice to run the power calculation twice,
to see the variability of estimated results.

Arne Leijon, 2018-08-08
"""

import logging

from PairedCompCalc import pc_logging
from PairedCompCalc.pc_data import PairedCompFrame
from PairedCompCalc import pc_power as pcp


# pc_logging.setup(result_path='.', log_file='run_power.log')  # to save the log file
pc_logging.setup()

logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)  # test
logger.setLevel(logging.INFO)


# ------------------------------------- Define Test Conditions:

# *** Anticipated mean quality difference B - A in the population:
q_diff = 0.5
# *** Inter-individual standard deviation of the quality difference:
q_std = 0.3

n_response_magn = 4
pcf = PairedCompFrame(attributes=['SimQ'],
                      systems=['A', 'B'],
                      response_labels=[f'Diff{i}' for i in range(n_response_magn)],
                      forced_choice=False)

# *** Number of pair presentations per test participant:
n_pres = 6

head_log = (f'*** Estimate Power with {n_pres} pair presentations,' +
            f' with difference mean = {q_diff:.1f}, std. = {q_std:.1f}')
logger.info(head_log)
logger.info(f'*** Using {n_response_magn} response magnitudes, forced_choice={pcf.forced_choice}:')

# ------------------------------ estimate_n_subjects:

n_estim = pcp.estimate_n_subjects(pcf, q_diff, q_std, n_pres)

# ------------------------------ calculate power with better precision:

(p_true_pos, p_false_pos) = pcp.power_ab_mean(pcf, q_diff, q_std, n_estim, n_pres)
result_log = (f'Estimated Power for Population Mean with {n_estim} subjects:\n' +
              f'p_true_pos = {p_true_pos:.1%}; p_false_pos = {p_false_pos:.1%}\n')
logger.info(result_log)

# ------------------------------ perhaps compare with other experimental condition:
n_response_magn = 3
pcf = PairedCompFrame(attributes=['SimQ'],
                      systems=['A', 'B'],
                      response_labels=[f'Diff{i}' for i in range(n_response_magn)],
                      forced_choice=True)
logger.info(f'*** Using {n_response_magn} response magnitudes, forced_choice={pcf.forced_choice}:')

# (p_true_pos, p_false_pos) = power_ab_individual(pcf, q_diff, q_std, n_subjects, n_pres)

(p_true_pos, p_false_pos) = pcp.power_ab_mean(pcf, q_diff, q_std, n_estim, n_pres)
result_log = (f'Estimated Power for Population Mean with {n_estim} subjects:\n' +
              f'p_true_pos = {p_true_pos:.1%}; p_false_pos = {p_false_pos:.1%}\n')
logger.info(result_log)

# ------------------------------ compare with other experimental condition:
n_response_magn = 1
pcf = PairedCompFrame(attributes=['SimQ'],
                      systems=['A', 'B'],
                      response_labels=[f'Diff{i}' for i in range(n_response_magn)],
                      forced_choice=True)
logger.info(f'*** Using {n_response_magn} response magnitudes, forced_choice={pcf.forced_choice}:')

# ------------------------------ test power_ab:

(p_true_pos, p_false_pos) = pcp.power_ab_mean(pcf, q_diff, q_std, n_estim, n_pres)
result_log = (f'Estimated Power for Population Mean with {n_estim} subjects:\n' +
              f'p_true_pos = {p_true_pos:.1%}; p_false_pos = {p_false_pos:.1%}\n')
logger.info(result_log)

# (p_true_pos, p_false_pos) = pcp.power_ab_individual(pcf, q_diff, q_std, n_estim, n_pres)
# result_log = (f'Estimated Power for Population Individual with {n_estim} subjects:\n' +
#               f'p_true_pos = {p_true_pos:.1%}; p_false_pos = {p_false_pos:.1%}\n')
# logger.info(result_log)

logging.shutdown()

