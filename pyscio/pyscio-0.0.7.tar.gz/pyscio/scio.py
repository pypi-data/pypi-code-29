# from . import scio_extension
# from pyscio.pyscio import scio_extension
import scio_extension
import numpy as np

"""

Command to generate interface file
f2py -h scio_extension.pyf -m scio_extension ../../src/scio.f90

Command to recompile:
f2py -c scio_extension.pyf ../../src/scio.f90

Command to install 
python -m pip install --index-url https://test.pypi.org/simple/ pyscio

Command to upload
twine upload --repository-url https://test.pypi.org/legacy/ dist/*



scio(s,w,rhomat,thr,maxit,nniter,jerr,isym,[n])

Wrapper for ``scio``.

Parameters
----------
s : input rank-2 array('d') with bounds (n,n)
w : input rank-2 array('d') with bounds (n,n)
rhomat : input rank-2 array('d') with bounds (n,n)
thr : input float
maxit : input int
nniter : input int
jerr : input int
isym : input int

Other Parameters
----------------
n : input int, optional
    Default: shape(s,0)
    
    
------------------------------------------------------------

sciopath(wlist,s,w,rholist,thr,maxit,nniter,jerrlist,idiag,isym,[n,nrho])

Wrapper for ``sciopath``.

Parameters
----------
wlist : input rank-3 array('d') with bounds (n,n,nrho)
s : input rank-2 array('d') with bounds (n,n)
w : input rank-2 array('d') with bounds (n,n)
rholist : input rank-1 array('d') with bounds (nrho)
thr : input float
maxit : input int
nniter : input int
jerrlist : input rank-1 array('i') with bounds (nrho)
idiag : input int
isym : input int

Other Parameters
----------------
n : input int, optional
    Default: shape(wlist,0)
nrho : input int, optional
    Default: shape(wlist,2)
    
"""


def scio_path(s, lambda_list=None, threshold=0.0001, max_iterations=10000, pen_diag=False, symmetric=True):
    p = s.shape[0]
    if lambda_list is None:
        lambda_list = np.linspace(np.max(np.abs(s)) / 10, np.max(np.abs(s)), num=10)
    lambda_list.sort()

    assert(len(lambda_list.shape) == 1)
    n_lambda = np.size(lambda_list)

    jerr_list = np.zeros(n_lambda, dtype='i')
    nn_iter = 1

    w = np.zeros_like(s)
    np.fill_diagonal(w, 1 / np.diag(s))
    w_list = np.zeros((p, p, n_lambda))

    idiag = int(pen_diag)
    isym = int(symmetric)

    scio_extension.sciopath(wlist=w_list,
                            s=s,
                            w=w,
                            rholist=lambda_list,
                            thr=threshold,
                            maxit=max_iterations,
                            nniter=nn_iter,
                            jerrlist=jerr_list,
                            idiag=idiag,
                            isym=isym,
                            nrho=n_lambda)
    w_list, w_list.reshape((n_lambda, p, p))
    w_list = np.transpose(w_list, (2, 0, 1))
    return w_list, lambda_list


def scio_cv(x, lambda_max=1, alpha=0.95, max_iterations=100, *args):
    num_rows, num_cols = x.shape

    num_tr = int(np.round(num_rows / 2))
    num_te = num_rows - num_tr

    tr = np.random.permutation(num_rows)
    s_tr = np.cov(x[tr[:num_tr], :].T)
    s_te = np.cov(x[tr[num_te:], :].T)

    lambda_val = lambda_max
    lambda_cv = lambda_max

    loss_min = likelihood(s_te, scio(s_tr, lambda_val, *args))

    i = 0
    for i in range(1, max_iterations + 1):
        lambda_val *= alpha

        tmp = likelihood(s_te, scio(s_tr, lambda_val, *args))
        if tmp <= loss_min:
            loss_min = tmp
            lambda_cv = lambda_val
        else:
            break

    if i >= max_iterations:
        print("WARNING: Maximum CV iterations exceeded! Consider increasing max_iterations")

    w = scio(np.cov(x.T), lambda_cv, *args)
    return w, lambda_cv


def likelihood(sigma, omega):
    sign, logdet = np.linalg.slogdet(omega)

    if sign <= 0:
        print("WARNING: Precision matrix estimate is not positive definite.")
    tmp = np.sum(np.diag(sigma.dot(omega))) - np.abs(logdet) - omega.shape[0]

    if np.isfinite(tmp):
        return tmp
    else:
        return np.inf


def scio(s, lambda_value, thr=1e-4, max_iterations=1e4, pen_diag=False, sym=True):
    if len(s.shape) != 2:
        raise Exception("Matrix S must be rank 2")
    if s.shape[0] != s.shape[1]:
        raise Exception("Matrix S must be symmetric")

    nn_iter = 10
    ierr = 0

    w = np.zeros_like(s)
    np.fill_diagonal(w, np.diag(s))

    lambda_mat = lambda_value
    if np.isscalar(lambda_value):
        lambda_mat = np.full(s.shape, lambda_value)

    if not pen_diag:
        np.fill_diagonal(lambda_mat, 0)

    a = scio_extension.scio(s, w, lambda_mat, thr, max_iterations, nn_iter, ierr, int(sym))
    return w



