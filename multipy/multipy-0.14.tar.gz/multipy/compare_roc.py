# TODO: tpr fpr axes in incorrect order.
# This kind of plot might not be good after all, since the
# the procedures attempt to control false positives,
# which makes the points line up.

# -*- encoding: utf-8 -*-
"""Compare different correction techniques using data generated
according to the Bennett et al. model.

Author: Tuomas Puoliväli
Email: tuomas.puolivali@helsinki.fi
Last modified: 11th September 2018
License: Revised 3-clause BSD
"""

import matplotlib.pyplot as plt

import numpy as np

from data import square_grid_model

from fdr import lsu, qvalue, tst
from fwer import sidak, holm_bonferroni, hochberg
from rft import rft_2d
from permutation import tfr_permutation_test

from viz import plot_grid_model

from util import grid_model_counts, roc

fig = plt.figure()
ax = fig.add_subplot(111)

"""Generate the test data."""
nl, sl = 90, 30
N, delta = 25, 0.7
alpha = 0.05

for i in np.arange(0, 10):
    delta = 0.1 + float(i) / 10.0

    X, X_tstats, X_raw, Y_raw = square_grid_model(nl, sl, N, delta)

    """Apply each correction technique to the generated dataset."""
    Y_sidak = sidak(X.flatten(), alpha=alpha)
    Y_sidak = Y_sidak.reshape(nl, nl)

    Y_fdr = lsu(X.flatten(), q=alpha)
    Y_fdr = Y_fdr.reshape(nl, nl)

    Y_qvalue, _ = qvalue(X.flatten(), threshold=alpha)
    Y_qvalue = Y_qvalue.reshape(nl, nl)

    Y_rft, _, _ = rft_2d(X_tstats, fwhm=30, alpha=alpha, verbose=True)
    # No reshape needed since already in correct form.

    Y_tst = tst(X.flatten(), q=alpha)
    Y_tst = Y_tst.reshape(nl, nl)

    Y_permutation = tfr_permutation_test(X_raw, Y_raw, n_permutations=100,
                                         alpha=alpha, threshold=1)

    Y_holm = holm_bonferroni(X.flatten(), alpha=alpha)
    Y_holm = Y_holm.reshape(nl, nl)

    Y_hochberg = hochberg(X.flatten(), alpha=alpha)
    Y_hochberg = Y_hochberg.reshape(nl, nl)

    """ROC plot."""

    sidak_fpr, sidak_tpr = roc(grid_model_counts(Y_sidak, nl, sl))
    ax.plot(sidak_fpr, sidak_tpr, 'r.')

    permutation_fpr, permutation_tpr = roc(grid_model_counts(Y_permutation, nl, sl))
    ax.plot(permutation_fpr, permutation_tpr, 'b.')

    rft_fpr, rft_tpr = roc(grid_model_counts(Y_rft, nl, sl))
    ax.plot(rft_fpr, rft_tpr, 'k.')

    fdr_fpr, fdr_tpr = roc(grid_model_counts(Y_fdr, nl, sl))
    ax.plot(fdr_fpr, fdr_tpr, 'y.')

    qvalue_fpr, qvalue_tpr = roc(grid_model_counts(Y_qvalue, nl, sl))
    ax.plot(qvalue_fpr, qvalue_tpr, 'm.')

    uncor_fpr, uncor_tpr = roc(grid_model_counts(X<alpha, nl, sl))
    ax.plot(qvalue_fpr, qvalue_tpr, 'c.')

ax.plot(np.linspace(0, 1, 100), np.linspace(0, 1, 100), '-')

plt.show()
