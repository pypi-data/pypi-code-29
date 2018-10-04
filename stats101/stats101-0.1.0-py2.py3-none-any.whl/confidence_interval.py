# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from scipy import stats


def mean(conf_level, data):
    """
    Return the confidence interval of your data for a given
    confidence level

    Parameters
    ----------
    conf_level: float in [0, 1)
        Value of your confidence level
    data: list, pandas.Series, or numpy.ndarray

    Returns
    -------
    tuple:
        Lower and upper bounds for your given confidence level
    """
    pHat, stdErr, degFreedom = _interval_data(data)

    return stats.t.interval(conf_level, df=degFreedom, loc=pHat, scale=stdErr)


def proportion(conf_level, data):
    """
    Return the confidence interval of your data for a given
    confidence level

    Parameters
    ----------
    conf_level: float in [0, 1)
        Value of your confidence level
    data: list, pandas.Series, or numpy.ndarray

    Returns
    -------
    tuple:
        Lower and upper bounds for your given confidence level
    """
    pHat, stdErr, degFreedom = _interval_data(data)

    return stats.norm.interval(conf_level, loc=pHat, scale=stdErr)


def _interval_data(data):
    if isinstance(data, pd.Series):
        data = data.values

    if isinstance(data, list):
        data = np.array(data)

    assert isinstance(data, np.ndarray)

    pHat = np.mean(data)
    stdErr = stats.sem(data)
    degFreedom = len(data) - 1

    return pHat, stdErr, degFreedom
