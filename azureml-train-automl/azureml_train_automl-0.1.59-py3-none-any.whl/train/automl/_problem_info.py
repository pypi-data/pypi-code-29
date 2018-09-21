# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""A container for information about the problem being worked on.

This is used to pass information to the server to use to give
better pipelines to try next.
"""
import copy
import json

# from automl.client.core.common import constants
# from automl.client.core.common import resource_limits

# from automl.client.core.common.constants import (
# TimeConstraintEnforcement as time_constraint)
from . import constants
from . import _resource_limits

from .constants import (
    TimeConstraintEnforcement as time_constraint)


class _ProblemInfo(object):
    """Container object for metadata about the problem being worked on
    Provides more information that can be used to predict future pipelines
    This information is important for predicting the cost of a pipeline when
        the data is not directly available for inspection
    """
    def __init__(
            self, dataset_samples=0, dataset_features=0, dataset_classes=0,
            dataset_num_categorical=0, dataset_y_std=0,
            runtime_constraints=None,
            num_threshold_buffers=3,
            num_threads=1,
            is_sparse=False,
            constraint_mode=time_constraint.TIME_CONSTRAINT_PER_ITERATION,
            cost_mode=constants.PipelineCost.COST_FILTER,
            task=constants.Tasks.CLASSIFICATION,
            metric="AUC_macro"):
        """Constructor for _ProblemInfo
        :param dataset_samples: number of samples in the whole dataset
        :param dataset_features: number of features in the dataset
        :param dataset_classes: number of classes in the targets of the dataset
        :param dataset_num_categorical: number of categorical features in
            the dataset
        :param dataset_y_std: standard deviation of targets
        :param runtime_constraints:
        :param num_threshold_buffers:
        :param num_threads:
        :param is_sparse:
        :param constraint_mode:
        :param cost_mode: behavior to follow when filtering on costly pipelines
        :param task: machine learning task being executed
            (classification or regression)
        :param metric: metric to be optimized
        """
        self.dataset_samples = dataset_samples
        self.dataset_features = dataset_features
        self.dataset_classes = dataset_classes
        self.dataset_num_categorical = dataset_num_categorical
        self.dataset_y_std = dataset_y_std
        self.task = task
        self.metric = metric
        self.num_threads = num_threads
        self.is_sparse = is_sparse
        self.runtime_constraints = (
            runtime_constraints or _resource_limits.default_resource_limits)
        self.constraint_mode = constraint_mode
        self.cost_mode = cost_mode
        self._server_threshold_events = 0
        self._num_threshold_buffers = num_threshold_buffers
        self._start_time = None
        self._current_time = None

        # Used in total-cost mode.
        self._max_time = self.runtime_constraints[
            _resource_limits.TIME_CONSTRAINT]

    @staticmethod
    def from_dict(d):
        """Factory function for _ProblemInfo objects
        :param d: dictionary of dataset attributes
        :return: a _ProblemInfo object
        """
        ret = _ProblemInfo()
        ret.__dict__ = copy.deepcopy(d)
        return ret

    def to_dict(self):
        """Converts the current _ProblemInfo object into a dictionary
        :return: dictionary of dataset attributes
        """
        d = copy.deepcopy(self.__dict__)
        return d

    def __str__(self):
        """Gets a string representation of the problem info"""
        return '_ProblemInfo(' + json.dumps(self.to_dict()) + ')'

    def get_time_constraint(self):
        """Gets the time constraint placed on the experiment
        :return: the time constraint
        """
        return self.runtime_constraints[_resource_limits.TIME_CONSTRAINT]

    def set_time_constraint(self, new_constraint):
        """Sets the time constraint placed on the experiment
        :param new_constraint: the time constraint
        """
        self.runtime_constraints[
            _resource_limits.TIME_CONSTRAINT] = new_constraint

    def handle_server_code(self, status_code):
        """Called on the client side to interpret server codes.
        :param status_code: A code sent from the server, e.g.
            to increase the time constraint.
        :param runner: The Runner object to also update if necessary.
        """

        if (self.constraint_mode ==
            time_constraint.TIME_CONSTRAINT_PER_ITERATION and
            status_code and status_code ==
                constants.ServerStatus.INCREASE_TIME_THRESHOLD):
            self._server_threshold_events += 1
            if self._server_threshold_events >= self._num_threshold_buffers:
                self._server_threshold_events = 0
                new_threshold = int(
                    self.runtime_constraints[
                        _resource_limits.TIME_CONSTRAINT] * 1.5)
                print('Increasing time constraint to {0}'.format(
                    new_threshold))
                self.runtime_constraints[
                    _resource_limits.TIME_CONSTRAINT] = new_threshold

    def done(self):
        """Return true if client should halt training."""
        return (
            self.constraint_mode == time_constraint.TIME_CONSTRAINT_TOTAL and
            self.runtime_constraints[_resource_limits.TIME_CONSTRAINT] <= 0)

    def set_start_time(self, t):
        """Sets the start time"""
        self._start_time = t

    def update_time(self, t):
        """Updates the current time"""
        self._current_time = t
        if (self.constraint_mode == time_constraint.TIME_CONSTRAINT_TOTAL):
            self.runtime_constraints[_resource_limits.TIME_CONSTRAINT] = int(
                self._max_time - (self._current_time - self._start_time))

    def set_cost_mode(self):
        """Sets the cost mode for the problem"""
        if (self.dataset_samples is None or self.dataset_samples <= 0 or
            self.dataset_classes is None or self.dataset_classes <= 0 or
            self.dataset_features is None or self.dataset_features <= 0 or
            self.get_time_constraint() is None or
                self.get_time_constraint() <= 0):
            self.cost_mode = constants.PipelineCost.COST_NONE
