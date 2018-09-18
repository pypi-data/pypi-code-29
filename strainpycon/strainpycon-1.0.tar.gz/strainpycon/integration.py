"""Functions related to posterior density integration.

"""
import numpy as np

def mean_var(mat_blocks, d, gamma, quad_nodes):
    """Computes the posterior mean and variance for the strain components.

    This function is not meant to be called directly. See `posterior_stats`
    method in `StrainRecon` class for a more convenient function.

    Parameters
    ----------
    mat_blocks : 2D- or 3D-array
        All possible binary rows (2D) or blocks (3D) in the matrix.
    d : vector
        The measurement vector in StrainRecon.jl format.
    gamma : vector
        Standard deviation of the assumed Gaussian measurement noise. Same
        shape as `d`.
    quad_nodes : 2D array
        Each row is a quadrature node. Nodes have equal weights.

    Returns
    -------
    meanmat : 2D array
        Posterior mean of the matrix. Full matrix is returned instead of
        StrainRecon.jl format, if `mat_blocks` is 3D.
    meanvec : vector
        Posterior mean of the vector.
    varmat : 2D array
        Diagonal elements of the posterior covariance of the matrix. Full
        matrix is returned if `mat_blocks` is 3D.
    varvec : vector
        Diagonal elements of the posterior covariance of the vector.

    Notes
    -----
    See [#]_ for the algorithm.

    References
    ----------
    .. [#] "A Bayesian framework for molecular strain identification from mixed
           diagnostic samples", L. Mustonen et al, https://doi.org/10.1088/1361-6420/aad7cd

    """
    gamma2 = -.5 * gamma**(-2)

    if mat_blocks.ndim == 2:
        cats = 2
        mat_blocks_vect = mat_blocks
        dmat = d
    else:
        cats = mat_blocks.shape[1] + 1
        if cats == 2:
            raise ValueError("3D array with only 2 categories")
        dmat = np.reshape(d, (-1, cats - 1))
        gamma2 = np.reshape(gamma2, dmat.shape)
        mat_blocks_vect = np.array([block.flatten() for block in mat_blocks])

    S = len(quad_nodes)
    q = len(d)
    m = q // (cats - 1)
    n = np.size(mat_blocks, -1)
    mask = np.eye(m) != 1

    # compute max-lambda
    lambdas = np.empty(S)
    for s in range(S):
        w = quad_nodes[s]
        row_prods = np.dot(mat_blocks, w)
        if cats == 2:
            U = [gamma2[k] * np.abs(row_prods - d[k]).min()**2 for k in range(m)]
        else:
            U = [np.sum(gamma2[k] * (row_prods - dmat[k])**2, -1).max() for k in range(m)]
        lambdas[s] = np.sum(U)
    max_lambda = lambdas.max()

    # means
    I1 = 0
    Imat = np.zeros((m, n*(cats-1))) # each block is vectorized
    Ivec = np.zeros(n)
    Ivec2 = np.zeros(n) # squared w
    for s in range(S):
        w = quad_nodes[s]
        row_prods = np.dot(mat_blocks, w)
        P = np.empty(m)
        G = np.empty((m, n*(cats-1)))
        for k in range(m):
            L = gamma2[k] * (row_prods - dmat[k])**2
            if cats > 2:
                L = np.sum(L, 1)
            U = L.max()
            expLU = np.exp(L-U)
            P[k] = np.sum(expLU)
            G[k] = np.dot(expLU, mat_blocks_vect)

        Pprod = P.prod() * np.exp(lambdas[s] - max_lambda)
        I1 += Pprod
        Ivec += w * Pprod
        Ivec2 += w**2 * Pprod
        Imat_incr = np.array([G[k] * P[mask[k]].prod() for k in range(m)])
        Imat += Imat_incr * np.exp(lambdas[s] - max_lambda)

    meanmat = Imat / I1

    # add "missing rows"
    if cats > 2:
        # meanmat is now (m, n*(cats-1))
        meanmat = np.reshape(meanmat, (q, n))
        meanmat = np.reshape(meanmat, (cats-1, -1), 'F')
        meanmat = np.row_stack((1 - np.sum(meanmat, 0), meanmat))
        meanmat = np.reshape(meanmat, (-1, n), 'F')

    meanvec = Ivec / I1
    meanvec2 = Ivec2 / I1

    varmat = np.maximum(meanmat - meanmat**2, np.zeros(meanmat.shape))
    varvec = np.maximum(meanvec2 - meanvec**2, np.zeros(meanvec.shape))

    return meanmat, meanvec, varmat, varvec
