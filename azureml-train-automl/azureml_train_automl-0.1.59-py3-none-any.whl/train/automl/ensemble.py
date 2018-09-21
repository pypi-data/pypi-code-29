# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""Module for ensembling previous AutoML iterations."""

from sklearn.base import BaseEstimator

from . import constants
from . import _ensemble_selector
from . import model_wrappers

import numpy as np


class Ensemble(BaseEstimator):
    """
    Class for ensembling previous AutoML iterations.
    The ensemble pipeline is initialized from a collection of already fitted pipelines.

    :param logger: Logger instance.
    :type logger: Logger
    :param estimators: array of tuples <AlgoName, FittedModel>.
    :type estimators: array<str,Pipeline>
    :param task_type: Whether it's a classification or regression.
    :type task_type: str
    :param primary_metric: The primary metric that is being used for selecting the fitted models.
    :type primary_metric: str
    :param iterations: Number of iterations for selecting the models that will be part of the ensemble.
    :type iterations: int
    :param algo_name: [Ensemble algorithm] (default: {"SoftVoting"}).
    :type algo_name: str
    :param greedy_selection_threshold: Threshold for the greedy phase of the selection,
        only pipelines that scored above threshold * best_score will be included (default: {0.5}).
    :type greedy_selection_threshold: int
    """
    def __init__(self,
                 logger,
                 estimators,
                 task_type: str,
                 primary_metric: str,
                 iterations: int,
                 algo_name: str = "SoftVoting",
                 greedy_selection_threshold: float = 0.5):
        """
        Creates an Ensemble pipeline out of a collection of already fitted pipelines.

        :param logger: Logger instance.
        :type logger: Logger
        :param estimators: array of tuples <AlgoName, FittedModel>.
        :type estimators: array<str,Pipeline>
        :param task_type: Whether it's a classification or regression.
        :type task_type: str
        :param primary_metric: The primary metric that is being used for selecting the fitted models.
        :type primary_metric: str
        :param iterations: Number of iterations for selecting the models that will be part of the ensemble.
        :type iterations: int
        :param algo_name: [Ensemble algorithm] (default: {"SoftVoting"}).
        :type algo_name: str
        :param greedy_selection_threshold: Threshold for the greedy phase of the selection,
            only pipelines that scored above threshold * best_score will be included (default: {0.5}).
        :type greedy_selection_threshold: int
        """
        # input validation
        if iterations < 1:
            raise ValueError("iterations parameter needs to be >= 1")
        if logger is None:
            raise ValueError("logger parameter should not be None")

        self.logger = logger
        self.estimators = estimators
        self.task_type = task_type
        self.primary_metric = primary_metric
        self.iterations = iterations
        self.algo_name = algo_name

    def fit(self, X, y):
        """
        Fits the ensemble based on the existing fitted pipelines.

        :param X: Input data.
        :type X: numpy.ndarray or scipy.spmatrix
        :param y: Input target values.
        :type y: array or numpy.ndarray
        :return: Returns a fitted ensemble including all the models selected.
        """
        algo_names, fitted_models = zip(*self.estimators)
        selector = _ensemble_selector \
            .EnsembleSelector(logger=self.logger,
                              fitted_models=fitted_models,
                              metric=self.primary_metric,
                              iterations=self.iterations,
                              task_type=self.task_type)

        unique_ensemble, unique_weights = selector.select(X, y)

        # TODO: when creating the ensemble_estimator_tuples we'll need to
        # get the fully trained models (not the partially trained ones)
        ensemble_estimator_tuples = [(algo_names[i], fitted_models[i])
                                     for i in unique_ensemble]
        unique_labels = np.unique(y).tolist()
        if self.task_type == constants.Tasks.CLASSIFICATION:
            self.estimator = model_wrappers.PreFittedSoftVotingClassifier(
                estimators=ensemble_estimator_tuples,
                weights=unique_weights,
                classification_labels=unique_labels)
        elif self.task_type == constants.Tasks.REGRESSION:
            self.estimator = model_wrappers.PreFittedSoftVotingRegressor(
                estimators=ensemble_estimator_tuples,
                weights=unique_weights)

        # cleanup the instance for pickling
        del self.estimators
        del self.task_type
        del self.primary_metric
        del self.iterations
        del self.algo_name
        del self.logger

        return self.estimator

    def predict(self, X):
        """
        Predicts the target for the provided input.

        :param X: Input test samples.
        :type X: numpy.ndarray or scipy.spmatrix
        :return: Prediction values.
        """
        return self.estimator.predict(X)

    def predict_proba(self, X):
        """
        Returns the probability estimates for the input dataset.

        :param X: Input test samples.
        :type X: numpy.ndarray or scipy.spmatrix
        :return: Prediction probabilities values.
        """
        return self.estimator.predict_proba(X)
