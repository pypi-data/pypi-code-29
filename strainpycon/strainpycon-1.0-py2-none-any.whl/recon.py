"""This module defines the StrainRecon class.

"""
from strainpycon import utils, psimplex, integration
import numpy as np

class StrainRecon:
    """Stores parameters and provides functions for strain computations.

    We use the word `reconstruction` when referring to a single pair of strains
    and their frequencies that minimizes, for a given measurement, the properly
    defined misfit, i.e., some (weighted) sum of squares. In probabilistic
    terms, reconstruction corresponds to the maximum a posteriori (MAP)
    estimate under the assumption that the measurement error is Gaussian and
    the prior distributions for the strains and their frequencies are uniform.

    This class can also be used to compute posterior statistics under the
    additional assumption that the frequencies are listed in decreasing order.
    More precisely, posterior mean and the square root of the diagonal of the
    posterior covariance can be computed. The posterior covariance is related
    to the uncertainty that stems from the measurement error and/or from the
    non-unique matrix-vector decomposition that mathematically connects the
    measurement to the underlying mixing model.

    Attributes
    ----------
    nopt : int, optional
        Number of random initial vectors in the block coordinate descent
        optimization scheme when computing the reconstruction. Larger values
        lead to more accurate results but require more time. Default is 50.
    nint : int, optional
        Number of integration nodes in the Monte Carlo method when computing
        posterior means and variances. Default is 5000. Can be overridden when
        calling `posterior_stats`.
    lsqtol : float, optional
        Stopping criterion parameter in the linear least-squares subproblem
        arising in the block coordinate descent method. See
        `pystrainrecon.psimplex.lstsq_simplex` for details.
    lsqiter : int, optional
        Another stopping criterion parameter for
        `pystrainrecon.psimplex.lstsq_simplex` method.

    """
    def __init__(self, nopt=50, nint=5000, lsqtol=1e-8, lsqiter=100):
        self.nopt = nopt
        self.nint = nint
        self.lsqtol = lsqtol
        self.lsqiter = lsqiter


    def compute(self, meas, nstrains, gamma=None, uncertainty=False):
        """Computes the reconstruction, optionally also posterior statistics.

        Parameters
        ----------
        meas : vector or 2D-array
            If `meas` is a vector with shape (m,), then the strains are binary
            and each element in `meas` represents the relative amount of ones.
            Otherwise, `meas` must have shape (c, m), where c is the number of
            possible categories in strains. Then the i'th row represents the
            relative amount of the i'th category.
        nstrains : int
            Number of strains in the reconstruction.
        gamma : None, scalar, vector, or 2D-array, optional
            The (assumed) standard deviation of the Gaussian measurement noise.
            If None (default) or a scalar, the noise level is assumed to be
            independent of the measurement location and an unweighted
            least-squares problem is considered. Otherwise, can have shape
            (m,), specifying the level for each location (whether or not `meas`
            is a vector), or shape (c, m), specifying the level separately for
            each measurement entry.
        uncertainty : bool, optional
            If True, calls `posterior_stats(meas, nstrains, gamma)` and
            appends the output to the returned tuple. If True, `gamma` must not
            be None, and a scalar `gamma` specifies the common noise level for
            all measurements. The default is False.

        Returns
        -------
        strainmat : (`nstrains`, m) integer matrix
            Strain barcode reconstruction. Contains integers {0, ..., c-1},
            where c=2 if `meas` is a vector. If `meas` contains nans, then the
            corresponding columns in `strainmat` are nan.
        freqvec : (`nstrains`,) vector
            Reconstructed strain frequencies. The frequencies appear in
            descending order and they correspond to the rows of `strainmat`.
        meanmat, meanvec, devmat, devvec : arrays
            See the return values of `posterior_stats`. These are returned only
            if `uncertainty` is True.

        Notes
        -----
        Each column in a 2D `meas` should sum up to one. In the current
        implementation, the first row is simply discarded and replaced with a
        value that makes the column sums exactly one.

        Similarly, in 2D `gamma` the values in the first row are never used.

        """
        if uncertainty:
            (meanmat, meanvec, devmat, devvec) = self.posterior_stats(meas, nstrains, gamma)

        (meas, gamma, cats, nanlocs) = utils.handle_input(meas, gamma)
        mat_blocks = utils.binary_blocks(nstrains, cats)

        (strainmat, freqvec) = psimplex.lstsq_bilin(
                mat_blocks, meas, gamma, self.nopt, vecstep=self.lsqtol, veciters=self.lsqiter)[0:2]

        # freqvec must be sorted in descending order
        sort_idx = freqvec.argsort()[::-1]
        strainmat = strainmat[:, sort_idx]
        freqvec = freqvec[sort_idx]

        strainmat = utils.binmat2intmat(strainmat, cats)
        strainmat = utils.addnanrows(strainmat, nanlocs)
        strainmat = strainmat.T

        if uncertainty:
            return strainmat, freqvec, meanmat, meanvec, devmat, devvec

        return strainmat, freqvec


    def misfits(self, meas, nrange, gamma=None):
        """Strain reconstruction misfits.

        Computes the (squared) StrainRecon.jl style misfits, i.e., negative
        log-likelihoods, for a list of different number of strains.
        
        Parameters
        ----------
        meas : vector or 2D-array
            See the description of `meas` parameter in `compute`.
        nrange : int iterable
            Number of strains in the reconstructions.
        gamma : None, scalar, vector, or 2D-array, optional
            See the description of `gamma` parameter in `compute`. A scalar
            `gamma` is the common standard deviation for all measurements and
            it has a scaling effect in the misfits.

        Returns
        -------
        misfitvec : vector
            Numpy vector with misfits. Same length as nrange.

        """
        (meas, gamma, cats, nanlocs) = utils.handle_input(meas, gamma)
        misfitvec = np.zeros(len(nrange))
        for n_idx in range(len(nrange)):
            nstrains = nrange[n_idx]
            mat_blocks = utils.binary_blocks(nstrains, cats)
            resnorm = psimplex.lstsq_bilin(
                    mat_blocks, meas, gamma, self.nopt, vecstep=self.lsqtol, veciters=self.lsqiter)[3]
            misfitvec[n_idx] = resnorm**2 / 2

        return misfitvec


    def posterior_stats(self, meas, nstrains, gamma, quad_nodes=None):
        """Posterior means and standard deviations for the matrix and vector.

        Parameters
        ----------
        meas : vector or 2D-array
            See the description of `meas` parameter in `compute`.
        nstrains : int
            Number of strains.
        gamma : scalar, vector, or 2D-array
            See the descriptions of `gamma` and `uncertainty` parameters in
            `compute`.
        quad_nodes : None, int, or 2D-array, optional
            If None, the quadrature nodes are drawn uniformly. The number of
            nodes is then determined by the `nint` attribute. An integer
            (scalar) argument can be used to override the number of nodes. The
            nodes can also be provided explicitly in a (k, `nstrains`) array,
            where k is a positive integer. Each node should be represented in
            descending order.

        Returns
        -------
        meanmat : 2D- or 3D-array
            Expected strain matrix (posterior mean). If the shape of `meas` is
            (m,), then `meanmat` has shape (`nstrains`, m). If `meas` is a
            (c, m) array, then the shape of `meanmat` is (c, `nstrains`, m) and
            each `meanmat[i]` contains the expected proportion of the i'th
            category.
        meanvec : vector
            Posterior mean of the frequency vector, shape is (`nstrains`,).
        devmat : 2D- or 3D-array
            Square roots of the posterior covariance for the strain matrix.
            Same shape as `meanmat`.
        devvec : vector
            Square roots of the posterior covariance for the frequency vector.

        Raises
        ------
        ValueError if gamma is None.

        """
        if gamma is None:
            raise ValueError("noise level required for posterior statistics")
        else:
            (meas, gamma, cats, nanlocs) = utils.handle_input(meas, gamma)

        if quad_nodes is None:
            quad_nodes = psimplex.rand_simplex(nstrains, self.nint, sort=-1)
        elif np.isscalar(quad_nodes):
            quad_nodes = psimplex.rand_simplex(nstrains, quad_nodes, sort=-1)

        mat_blocks = utils.binary_blocks(nstrains, cats)

        (meanmat, meanvec, varmat, varvec) = integration.mean_var(mat_blocks, meas, gamma, quad_nodes)
        devmat = np.sqrt(varmat)
        devvec = np.sqrt(varvec)

        if cats > 2:
            meanmat = np.reshape(meanmat, (-1, cats, nstrains)).swapaxes(0, 1)
            devmat = np.reshape(devmat, (-1, cats, nstrains)).swapaxes(0, 1)

        meanmat = utils.addnanrows(meanmat, nanlocs)
        devmat = utils.addnanrows(devmat, nanlocs)

        if cats > 2:
            meanmat = meanmat.swapaxes(1, 2)
            devmat = devmat.swapaxes(1, 2)
        else:
            meanmat = meanmat.T
            devmat = devmat.T

        return meanmat, meanvec, devmat, devvec


    def random_data(self, nmeas, nstrains, cats=None, gamma=None):
        """Random measurement vector or matrix.

        Generates a random measurement by drawing the strain barcode matrix and
        the frequency vector from uniform distributions.

        Parameters
        ----------
        nmeas : int
            Number of measurements. This is the length of the measurement
            vector or the number of columns in a measurement matrix.
        nstrains : int
            Number of strains when generating the data.
        cats : None or int, optional
            Number of categories, i.e., the number of different elements in the
            barcode. None (default) corresponds to two categories with a vector
            format.
        gamma : None, scalar, vector, or 2D-array, optional
            Noise in the measurement. If None (default), no measurement noise
            is added. Otherwise, `gamma` determines the standard deviation of
            the independent, zero-mean Gaussian random variables representing
            the measurement noise. See also the description of `gamma`
            parameter in `compute`.

        Returns
        -------
        meas : vector or 2D-array
            Measurement array. If `cats` is None, the shape is (`nmeas`,).
            Otherwise, the shape is (`cats`, `nmeas`). See also the description
            of the `meas` parameter in `compute`.
        strains : 2D array
            Strain barcodes in a (`nstrains`, `nmeas`) integer array. Elements
            are in {0, ..., cats-1}.
        freq : vector
            Strain frequencies. These are sorted in descending order and they
            correspond to the rows in `strains`.

        """
        freq = psimplex.rand_simplex(nstrains, sort=-1)

        if cats is None:
            strains = np.random.randint(0, 2, (nstrains, nmeas), dtype=int)
            meas = np.dot(freq, strains)
        else:
            strains = np.random.randint(0, cats, (nstrains, nmeas), dtype=int)
            binmat = utils.intmat2binmat(strains.T, cats-1)
            meas = np.dot(binmat, freq)
            meas = np.reshape(meas, (cats-1, nmeas), 'F')
            meas = np.vstack((1 - np.sum(meas, 0), meas))

        if gamma is not None:
            if not np.isscalar(gamma) and gamma.shape != meas.shape:
                # now gamma is 2D and meas is 3D
                gamma = np.tile(gamma, (np.size(meas, 0), 1))
            meas = meas + gamma * np.random.normal(size=meas.shape)

        return meas, strains, freq
