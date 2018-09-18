"""Simple auxiliary functions performing conversions etc.

"""
import numpy as np
import itertools

def handle_input(meas, gamma):
    """Converts the user input for computational measurements and noise levels.

    Typically, the user should not call this function directly.
    """
    meas = np.array(meas)
    if meas.ndim == 2 and meas.shape[0] == 2:
        meas = meas[1]

    if gamma is None:
        gamma = np.ones(meas.shape)
    elif np.isscalar(gamma):
        gamma = gamma * np.ones(meas.shape)
    elif np.ndim(gamma) == 1 and np.ndim(meas) == 2:
        gamma = np.tile(gamma, (np.size(meas, 0), 1))
    else:
        gamma = np.array(gamma)

    if meas.ndim == 1:
        cats = 2
        nanlocs = np.isnan(meas)
        meas = meas[~nanlocs]
        gamma = gamma[~nanlocs]
    else:
        cats = np.size(meas, 0)
        nanlocs = np.isnan(np.amin(meas, 0))
        meas = meas[:, ~nanlocs]
        meas = meas[1:, :].flatten('F')
        gamma = gamma[:, ~nanlocs]
        gamma = gamma[1:, :].flatten('F')

    return meas, gamma, cats, nanlocs


def binary_blocks(n, cats=2):
    """All possible binary rows or blocks.

    Returns either all possible binary vectors having given number of elements,
    or all possible binary blocks having given number of columns and column
    sums of at most one.

    Parameters
    ----------
    n : int
        Number of elements in a vector or number of columns in a block.
    cats : int, optional
        Number of categories for each column in a block. Must be at least 2. If
        `cats` is 2 (default), then a column can be either 0 and 1, i.e., a
        scalar. Otherwise, there are cats-1 different columns having sum of at
        most one.

    Returns
    -------
    blocks : 2D- or 3D-array
        If cats is 2, the shape is (2**n, n). Otherwise, the shape is
        (cats**n, cats-1, n).

    Examples
    --------
    >>> from strainpycon.utils import binary_blocks
    >>> binary_blocks(2)
    array([[0, 0],
           [0, 1],
           [1, 0],
           [1, 1]])
    >>> binary_blocks(2, cats=3)
    array([[[0, 0],
            [0, 0]],
           [[0, 1],
            [0, 0]],
           [[0, 0],
            [0, 1]],
           [[1, 0],
            [0, 0]],
           [[1, 1],
            [0, 0]],
           [[1, 0],
            [0, 1]],
           [[0, 0],
            [1, 0]],
           [[0, 1],
            [1, 0]],
           [[0, 0],
            [1, 1]]])

    """
    int_blocks = np.array(list(itertools.product(range(0, cats), repeat=n)))

    if cats == 2:
        return int_blocks

    binary_blocks = intmat2binmat(int_blocks, cats-1)
    return np.reshape(binary_blocks, (-1, cats-1, n))


def intmat2binmat(intmat, maxint):
    """Converts non-negative integer matrix to a binary matrix.

    Every positive integer k is converted to a unit vector which has one in the
    k'th position (when counting starts from one) and zero in the remaining
    positions. Zero is converted to a zero vector. The returned matrix has the
    same number of columns as the input matrix, i.e., the conversion is
    performed vertically.

    Parameters
    ----------
    intmat : 2D-array
        Matrix with non-negative integers.
    maxint : int
        Maximum allowed integer in `intmat`. Determines the length of the unit
        vectors. Must be greater than or equal to the actual maximum value in
        `intmat`.

    Returns
    -------
    binmat : 2D-array
        If `intmat` has shape (m, n), then the shape of binmat is
        (maxint * m, n).

    See Also
    --------
    strainpycon.utils.binmat2intmat

    Examples
    --------
    >>> from strainpycon.utils import intmat2binmat
    >>> mat = np.array([[0, 1, 2], [2, 1, 0]])
    >>> mat
    array([[0, 1, 2],
           [2, 1, 0]])
    >>> intmat2binmat(mat, 2)
    array([[0, 1, 0],
           [0, 0, 1],
           [0, 1, 0],
           [1, 0, 0]])

    """
    intmat = np.array(intmat)
    (m, n) = intmat.shape
    binmat = np.zeros((maxint * m, n), dtype=int)
    for row_idx in range(m):
        block = np.zeros((maxint+1, n), dtype=int)
        block[intmat[row_idx, :], range(n)] = 1
        binmat[range(maxint * row_idx, maxint * (row_idx+1))] = block[1:, :]
    return binmat


def binmat2intmat(binmat, cats):
    """Converts binary block matrix to a non-negative integer matrix.

    This function is the inverse of pystrainrecon.utils.intmat2binmat function.

    Parameters
    ----------
    binmat : 2D array
        Binary block matrix where blocks have `cats`-1 rows and each column in
        a block sums up to 1 or 0.
    cats : int
        Size of the block plus one. Must be at least 2.

    Returns
    -------
    intmat : 2D array
        Matrix with integers {0, ..., cats-1}.

    See Also
    --------
    strainpycon.utils.binmat2intmat

    Example
    -------
    >>> mat = np.array([[0, 1, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0]])
    >>> mat
    array([[0, 1, 0],
           [0, 0, 1],
           [0, 1, 0],
           [1, 0, 0]])
    >>> binmat2intmat(mat, 3)
    array([[0, 1, 2],
           [2, 1, 0]])

    """
    mat = np.array(binmat).T # work with the transpose
    n = np.size(mat, 0)
    m = np.size(mat, 1) // (cats - 1)

    # add the "missing rows" (here, columns)
    mat = np.reshape(mat, (m * n, cats - 1))
    mat = np.column_stack((1 - np.sum(mat, 1), mat))

    # row indices of nonzero entries (here, column indices)
    mat = np.nonzero(mat)[1]

    mat = np.reshape(mat, (n, m))

    return mat.T


def addnanrows(mat, nanlocs):
    """Returns array with nan rows added to specific locations.

    Parameters
    ----------
    mat : 2D- or 3D-array
        If `mat` is 3D, then the rows are added to `mat[i]` for each i.
    nanlocs : bool vector
        Vector specifying the nan row indices in the returned matrix. True
        corresponds to nan. The shape must be (k,), where k equals (number of
        rows in mat) + (number of Trues in nanlocs).

    Returns
    -------
    mat : 2D- or 3D-array
        Array augmented with nans.

    """
    mat = np.array(mat)

    def addnanrows2d(mat2d):
        (m, n) = mat2d.shape
        m_full = m + np.sum(nanlocs)
        fullmat = np.empty((m_full, n))
        fullmat.fill(np.nan)
        fullmat[~nanlocs, :] = mat2d
        return fullmat

    if mat.ndim == 2:
        return addnanrows2d(mat)
    else:
        return np.array([addnanrows2d(mat2d) for mat2d in mat])
