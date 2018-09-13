import numpy as _np
from .linear_model import _select_variables_from_prior, _fill_in_from_prior


def subset_optimizer(X, Y, prior, optimizer, **kwargs):

    if not isinstance(X, _np.ndarray):
        X = _np.array(X)

    if not isinstance(prior, _np.ndarray):
        Y = _np.array(Y)

    if not isinstance(prior, _np.ndarray):
        prior = _np.array(prior)

    optz = optimizer.set_params(**kwargs)

    # e = []
    n = Y.shape[1]
    A = _np.array([])
    for j in range(n):
        a_j = prior[j, :]
        y = Y[:, j]

        if not a_j.any():
            # ypred = _np.zeros(Y.shape[0])
            coef = a_j.copy()

        else:
            X_v = X[:, _select_variables_from_prior(a_j)]
            optz.fit(X_v, y)

            coef = _fill_in_from_prior(optz.coef_, a_j)
            # ypred = optz.predict(X_v)

        # e.append(mean_squared_error(y_true=y, y_pred=ypred))

        if j == 0:
            A = _np.hstack([A, coef])
        else:
            A = _np.vstack([A, coef])

    return A


def activity_estimator(prior, y, estimator=_LinearRegression, **kwargs):

    estimator = estimator(**kwargs)

    pr = prior.unstack(0).fillna(0).to_sparse(fill_value=0)

    estimator.fit(pr, y)

    return estimator


def fit_subset(X, y, a_i, optimizer=LinearRegression, tol=_tol, verbal=False, fit_intercept=False, **kwargs):

    if not isinstance(X, _np.ndarray):
        X = _np.array(X)
        if len(X.shape) == 1:
            X = X[_np.newaxis]

    if not isinstance(y, _np.ndarray):
        y = _np.array(y)
        if len(y.shape) == 0:
            y = y[_np.newaxis]

    if not isinstance(a_i, _np.ndarray):
        a_i = _np.array(a_i)

    optz = optimizer(fit_intercept=fit_intercept, **kwargs)

    if not (a_i > tol).any():

        optz.fit(_np.zeros(X.shape), _np.zeros(y.shape))

        # coef = a_i.copy()
        # coef = optz.coef_
    else:
        X_v = X[:, _select_variables_from_prior(a_i)]
        optz.fit(X_v, y)

        try:
            coef = fill_in_from_prior(optz.estimator_.coef_.copy(), a_i)
            optz.estimator_.coef_ = coef.copy()
        except Exception as e:
            if verbal:
                print(e)

            coef = fill_in_from_prior(optz.coef_.copy(), a_i)
            optz.coef_ = coef.copy()

        # coef = _fill_in_from_prior(optz.coef_, a_i)
        # optz.coef_ = coef

    return optz


def fit_subset_all_variables(X, y, B, estimator=LinearRegression, tol=_tol, **kwargs):

    if isinstance(y, _pd.Series):
        y = _pd.DataFrame(y).T

    estimators = {}
    for c, i in enumerate(y):

        wB = fit_subset(X, y[i], B.loc[i], optimizer=estimator, **kwargs)
        estimators[i] = wB

    wB = _pd.DataFrame({k: v.coef_ for k, v in estimators.items()}, index=B.columns).T
    wB.index.name = "target"
    __ = wB.T.stack()
    __ = __[__ != 0]

    wB = __
    wB.name = "weight"

    return wB


def subset_fit(fit_fn):

    @_functools.wraps(fit_fn)
    def fit_wrapper(X, y, a_i=None):

        if a_i is not None:
            X, y = _check_X_y(X, y, accept_sparse=['csr', 'csc', 'coo'], y_numeric=True, multi_output=True)

            X_v = extract_variables_from_prior(X, a_i)

            obj = fit_fn(X_v, y)

            obj.coef_ = fill_in_from_prior(obj.coef_.copy(), a_i).copy()

        else:
            obj = fit_fn(X, y)

        return obj

    return fit_wrapper


# The answer is in one of these two. Currently built as the first one. But I'm not sure. Second one seemed tempting as it follows the classical inherit from cls formula.
# https://www.codementor.io/sheena/advanced-use-python-decorators-class-function-du107nxsv
# https://andrefsp.wordpress.com/2012/08/23/writing-a-class-decorator-in-python/
#
# Another example but not to promising https://stackoverflow.com/questions/34241905/python-class-method-decorator/34242305#34242305
def constrained_estimator(estimator):

    class ConstrainedEstimator:
        def __init__(self, *args, **kwargs):
            self.oInstance = estimator(*args, **kwargs)

        def __getattribute__(self, attr_name):
            obj = super(ConstrainedEstimator, self).__getattribute__(attr_name)
            if hasattr(obj, '__call__'):
                if obj.__name__ == "fit":
                    return subset_fit(obj)
                else:
                    return obj

    return ConstrainedEstimator


def subset_fitter(estimator):
    """The class decorator example"""
    class ConstrainedEstimator(estimator):
        "This is the overwritten class"
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def __getattribute__(self, attr_name):
            obj = super(ConstrainedEstimator, self).__getattribute__(attr_name)
            if hasattr(obj, '__call__') and attr_name == ["fit"]:
                return subset_fit(obj)
            return obj

    return ConstrainedEstimator
