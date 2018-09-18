
from sklearn.base import BaseEstimator, TransformerMixin
from .onepara_func import onepara


class OnePara(BaseEstimator, TransformerMixin):
    def __init__(self):
        """No settings required"""

    def fit(self, X, y=None):
        """Do nothing and return the estimator unchanged"""
        return self

    def transform(self, X):
        return onepara(X)
