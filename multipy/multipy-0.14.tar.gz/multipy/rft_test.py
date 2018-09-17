import mne
from mne import read_evokeds
from mne.time_frequency import stft, stftfreq

import numpy as np

"""Load the sample dataset from disk."""
data_path = mne.datasets.sample.data_path()
fname = data_path + '/MEG/sample/sample_audvis-ave.fif'

evoked = read_evokeds(fname)

"""Prepare the data for testing RFT methods."""
# Left auditory
window_length = 64
X_lh_aud = stft(evoked[0]._data, wsize=window_length, tstep=32, verbose=True)
f_lh_aud = stftfreq(window_length, evoked[0].info['sfreq'])
t_lh_aud = np.linspace(evoked[0].times[0], evoked[0].times[-1],
                       np.shape(X_lh_aud)[2])

# Right auditory
window_length = 64
X_rh_aud = stft(evoked[1]._data, wsize=window_length, tstep=32, verbose=True)
f_rh_aud = stftfreq(window_length, evoked[0].info['sfreq'])
t_rh_aud = np.linspace(evoked[1].times[0], evoked[1].times[-1],
                       np.shape(X_rh_aud)[2])

# next compute stats
