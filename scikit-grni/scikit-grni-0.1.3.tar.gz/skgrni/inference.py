import pandas as _pd
import numpy as _np
from skgrni import model_selection as gsms
# from skgrni import linear_model as gslm
# from skgrni import metrics as gsm
import sklearn.metrics as metrics
from sklearn.linear_model import Lasso


def _dict2df(dictin):

    dictin = _pd.DataFrame(dictin).T
    dictin.index.names = ["z", "node", "cv"]
    ns = dictin.shape[1]
    dictin.columns = _pd.MultiIndex.from_tuples([("pred", i) for i in (range(ns // 2))] + [("true", i) for i in (range(ns // 2))])
    dictin = dictin.unstack(level=1)

    return dictin


def infer_networks(dataset, node_names=None, methods={"LASSO": Lasso}, zetavec=_np.logspace(-6, 0, num=100), methods_configs={}, CV=gsms.CVFilter(), **kwargs):

    for name, data in dataset.items():

        for method_name, func in methods.items():

            if method_name in methods_configs:
                confs = methods_configs[method_name]
            else:
                confs = {}

            X, Y = data.design_target()
            zetavec = _np.logspace(-6, 0, num=100)
            fitm_it = fit_method(X, Y, method=func, CV=CV, zetavec=zetavec, precompute=True, **confs, **kwargs)

            param_estimates = {}
            validation = {}
            training = {}
            for mtfit, g, cv, predictions in fitm_it:

                param_estimates[(mtfit.alpha, g, cv)] = mtfit.coef_.copy()
                validation[(mtfit.alpha, g, cv)] = _np.reshape(predictions["test"].copy(), -1)
                training[(mtfit.alpha, g, cv)] = _np.reshape(predictions["training"].copy(), -1)

            validation = _dict2df(validation)
            validation["dataset"] = name
            validation["method"] = method_name
            validation = validation.set_index(["dataset", "method"], append=True)

            training = _dict2df(training)
            training["dataset"] = name
            training["method"] = method_name
            training = training.set_index(["dataset", "method"], append=True)

            param_estimates = _pd.DataFrame(param_estimates).T
            param_estimates.index.names = ["z", "node", "cv"]
            if node_names is None:
                nodes = ["G" + str(i).zfill(2) for i in range(param_estimates.shape[1])]
            else:
                nodes = node_names

            param_estimates.columns = nodes
            param_estimates.columns.name = "node"

            param_estimates["dataset"] = name
            param_estimates["method"] = method_name
            param_estimates = param_estimates.set_index(["dataset", "method"], append=True)

            yield param_estimates, validation, training


def fit_method(X, Y, CV=None, method=Lasso, predictionmetrics={"r2": metrics.r2_score, "mse": metrics.mean_squared_error}, **kwargs):

    if CV is not None:
        for cv, (train, test) in enumerate(CV.split(X, Y)):

            X_train, Y_train = X.iloc[train], Y.iloc[train]
            X_test, Y_test = X.iloc[test], Y.iloc[test]

            prediction_data = {}
            for mtfit, g, cv in fit2target(X_train, Y_train, method=method, warm_start=True, cv=cv, **kwargs):

                y_pred = mtfit.predict(X_test)

                prediction_data["test"] = [y_pred, Y_test[g].values]

                y_pred = mtfit.predict(X_train)
                prediction_data["training"] = [y_pred, Y_train[g].values]

                yield mtfit, g, cv, prediction_data

    else:

        for mtfit, g, cv in fit2target(X, Y, method=method, warm_start=True, **kwargs):

            yield mtfit, g, cv


def fit2target(X, Y, **kwargs):

    for target in Y:
        y = Y[target]
        yield from penalize(X, y, **kwargs)


def penalize(X, y, zetavec=_np.logspace(-6, 0, num=10), method=Lasso, cv=0, fit_intercept=False, **kwargs):

    for z in zetavec:

        mth = method(alpha=z, fit_intercept=fit_intercept, **kwargs)
        # mth.set_params()
        mth.fit(X, y)
        yield mth, y.name, cv
