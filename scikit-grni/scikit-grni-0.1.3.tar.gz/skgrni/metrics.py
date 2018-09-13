import sklearn.metrics as _metrics
import pandas as _pd

# def wighted_mean_squared_error(y_true, y_pred, cov):


def _calc_metrics(truey, predy, metrics2calc={}):

    M = {}
    for m, f in metrics2calc.items():

        M[m] = f(truey, predy)

    M = _pd.Series(M)

    return M


def calc_prediction_metrics(truey, predy, predictionmetrics={"r2": _metrics.r2_score, "mse": _metrics.mean_squared_error}):

    return _calc_metrics(truey, predy, predictionmetrics)


def calc_classification_metrics(truey, predy, classmetrics={"mcc": _metrics.matthews_corrcoef, "f1": _metrics.f1_score, "acc": _metrics.accuracy_score, "pre": _metrics.precision_score}):

    return _calc_metrics(truey, predy, classmetrics)
