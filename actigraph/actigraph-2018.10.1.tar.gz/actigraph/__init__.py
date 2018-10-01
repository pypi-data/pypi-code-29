
"""Reference: https://www.ncbi.nlm.nih.gov/pubmed/28604558"""

import numpy as np
from scipy.signal import lfilter, firwin
from scipy.signal import resample as sp_resample

################################## Functions: ##################################

def aliasing_filter(accel,sr=30,low=0.01,high=7.0):
    """Aliasing filter to ensure compatibility with the Nyquist–Shannon sampling
    theorem.
    """
    numtaps = 20  # TODO: experiment with this
    if numtaps == 20 and low == 0.01 and high == 7.0 and sr == 30:
        # for speed, hard code the filter we always use
        h = [ 0.00255891, -0.00047885, -0.00760112, -0.00166226, 0.02380187,
              0.01220237, -0.06047104, -0.05457233, 0.16092131, 0.421052 ,
              0.421052 , 0.16092131, -0.05457233, -0.06047104, 0.01220237,
              0.02380187, -0.00166226, -0.00760112, -0.00047885, 0.00255891 ]
    else:
        h = firwin(numtaps, [low, high], pass_zero=False, fs=sr)
    accel_filtered = lfilter(h, 1.0, accel)
    return accel_filtered

def actigraph_filter(accel):
    """Frequency band-pass filter, implemented as a standard filter transfer
    function.
    """
    b = [0.04910898, -0.12284184, 0.14355788, -0.11269399, 0.05380374,
         -0.02023027, 0.00637785, 0.01851254, -0.03815411, 0.04872652, -0.05257721,
         0.04784714, -0.04601483, 0.03628334, -0.01297681, -0.00462621, 0.01283540,
         -0.00937622, 0.00344850, -0.00080972, -0.00019623]
    a = [1.00000000, -4.16372603, 7.57115309, -7.98046903, 5.38501191,
         -2.46356271, 0.89238142, 0.06360999, -1.34810513, 2.47338133, -2.92571736,
         2.92983230, -2.78159063, 2.47767354, -1.68473849, 0.46482863, 0.46565289,
         -0.67311897, 0.41620323, -0.13832322, 0.01985172]
    return lfilter(b, a, accel)

def resample(accel,old_sr,new_sr):
    """Resample a vector (accel, sampled at rate old_sr) to a new rate new_sr."""
    new_len = int(1.0*len(accel)*new_sr/old_sr)
    return sp_resample(accel, new_len)
    # TODO: try other resampling methods / parameters.  e.g.:
    # return resample_poly(accel, up, down)

def truncate(accel, min_g=None, max_g=None):
    """Truncate accel values to the range [min_g,max_g]."""
    accel_copy = accel.copy()
    if min_g != None:
        accel_copy[accel<min_g] = min_g
    if max_g != None:
        accel_copy[accel>max_g] = max_g
    return accel_copy

def truncate_max(accel, g=2.13):
    """Truncate accel values to within +/-g."""
    return truncate(accel, min_g=-g, max_g=g)

def rectify(accel):
    """Flip negative values in accel to positive values."""
    return abs(accel)

def dead_band(accel, g=0.068):
    """g was originally specified as 0.050."""
    accel_copy = accel.copy()
    accel_copy[abs(accel) < g] = 0
    return accel_copy

def res_convert(accel, min_g=0, max_g=2.13, nlevels=128):
    """Convert the acceleration data (accel) into the original 8-bit ADC resolution
    (128 levels across the 0-g to 2.13-g range).
    """
    # TODO?: should be 256 levels
    stepsize = float(max_g-min_g)/(nlevels-1)
    accel_copy = accel.copy()
    accel_copy -= min_g
    accel_copy /= stepsize
    accel_copy = np.rint(accel_copy)
    accel_copy *= stepsize
    accel_copy += min_g
    accel_copy = truncate(accel_copy, min_g=min_g, max_g=max_g)
    return accel_copy

def accumulate(accel):
    """Accumulate 10 consecutive samples into 1-s epoch counts."""
    if (len(accel) % 10) != 0:
        padding = np.zeros( 10 - (len(accel) % 10) )
    else:
        padding = np.array([])
    a_padded = np.concatenate((accel,padding))
    a_reshaped = np.reshape(a_padded, (-1,10))
    totals = np.sum(a_reshaped,axis=1)
    return totals

############################## Primary function: ###############################

def raw_to_counts(accel,sr):
    """Convert a vector of acceleration values (accel) to a vector of counts (one
    per second).
    """
    resampled = resample(accel,sr,30)
    alias_filtered = aliasing_filter(resampled)
    actigraph_filtered = actigraph_filter(alias_filtered)
    downsampled = resample(actigraph_filtered,30,10)
    truncated = truncate_max(downsampled)
    rectified = rectify(truncated)
    dead_banded = dead_band(rectified)
    res_converted = res_convert(dead_banded)
    accumulated = accumulate(res_converted)
    return accumulated

#################################### TODO: #####################################

# - make functions operate on accel in place to save some RAM?  just make one
#   copy of it initially.
# - handle delay added by filters (aliasing_filter and actigraph_filter) (note
#   that filtfilt is slower than lfilter but should get rid of the delay)
# - how to combine counts from 3 axes?  VM, probably.  otherwise we need to know
#   what the 'vertical' axis is.

################################################################################
