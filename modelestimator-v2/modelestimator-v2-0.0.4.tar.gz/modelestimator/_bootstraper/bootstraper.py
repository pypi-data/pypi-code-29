import copy
import random
import numpy as np
import math
import sys
import os

sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from _bw_estimator.bw_estimator import bw_estimator

#   Private functions
def _resample_columns(MULTIALIGNMENT_ARRAY):
    new_multialignment = np.empty_like(MULTIALIGNMENT_ARRAY)
    SEQUENCE_LENGTH = MULTIALIGNMENT_ARRAY.shape[1]

    for COLUMN_INDEX in range(SEQUENCE_LENGTH):
        RANDOM_INDEX = random.randint(0, SEQUENCE_LENGTH - 1)
        new_multialignment[:, COLUMN_INDEX] = MULTIALIGNMENT_ARRAY[:, RANDOM_INDEX]

    return new_multialignment

def _calculate_bw_for_resamplings(RESAMPLINGS, THRESHOLD, MULTIALIGNMENT):
    q_list = []
    eq_list = []
    number_of_times_bw_estimator_failed = 0

    for _ in range(RESAMPLINGS):
        RESAMPLED_MULTIALIGNMENT = _resample_columns(MULTIALIGNMENT)        
        RESAMPLED_MULTIALIGNMENT_LIST = [RESAMPLED_MULTIALIGNMENT]

        try:
            Q, EQ = bw_estimator(THRESHOLD, RESAMPLED_MULTIALIGNMENT_LIST)
            q_list.append(Q)
            eq_list.append(EQ)
        except:
            number_of_times_bw_estimator_failed +=1

    FAILED_PERCENTAGE = number_of_times_bw_estimator_failed / RESAMPLINGS
    return q_list, FAILED_PERCENTAGE

def q_diff_mean(REFERENCE_Q, RESAMPLED_Q_LIST):
    Q_DIFF_NORM_LIST = []

    for Q in RESAMPLED_Q_LIST:
        Q_DIFF = REFERENCE_Q - Q
        Q_DIFF_NORM = np.linalg.norm(Q_DIFF)
        Q_DIFF_NORM_LIST.append(Q_DIFF_NORM)

    Q_DIFF_MEAN = np.mean(Q_DIFF_NORM_LIST)

    return Q_DIFF_MEAN

#   Interface
def bootstraper(RESAMPLINGS, THRESHOLD, MULTIALIGNMENT):
    MULTIALIGNMENT_LIST = [MULTIALIGNMENT]
    try:
        REFERENCE_Q,_ = bw_estimator(THRESHOLD, MULTIALIGNMENT_LIST)
    except:
        raise ValueError("Failed to estimate a baseline Q matrix")

    RESAMPLED_Q_LIST, FAILED_PERCENTAGE = _calculate_bw_for_resamplings(RESAMPLINGS, THRESHOLD, MULTIALIGNMENT)
    Q_DIFF_MEAN = q_diff_mean(REFERENCE_Q, RESAMPLED_Q_LIST)
    Q_DIFF_MEAN *= 10000

    return Q_DIFF_MEAN, FAILED_PERCENTAGE