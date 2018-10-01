# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Defines a set of functions for retrieving model explanation result data from run history."""
import os
import pickle
import numpy as np

from .common import NUM_FEATURES, NUM_BLOCKS, module_logger, _sort_features


def _create_download_dir():
    # create the downloads folder
    download_dir = './download_explanation/'
    os.makedirs(download_dir, exist_ok=True)
    return download_dir


def _download_artifact(run, download_dir, artifact_name):
    path = os.path.join(download_dir, artifact_name + '.pkl')
    run.download_file(artifact_name + '.pkl', path)
    f = open(path, 'rb')
    values = pickle.load(f)
    f.close()
    return values


def _download_model_summary(run, download_dir, summary_name, top_k=None):
    metrics = run.get_metrics()
    storage_metadata = metrics.get(summary_name)
    if storage_metadata is None:
        return _download_artifact(run, download_dir, summary_name)
    else:
        num_columns_to_return = storage_metadata[NUM_FEATURES]
        num_blocks = storage_metadata[NUM_BLOCKS]
        if top_k is not None:
            num_columns_to_return = min(top_k, num_columns_to_return)
        summary = None
        concat_dim = None
        # Get the blocks
        for idx in range(num_blocks):
            block_name = summary_name + '_' + str(idx)
            block = _download_artifact(run, download_dir, block_name)
            if summary is None:
                summary = block
                concat_dim = len(summary.shape) - 1
            else:
                summary = np.concatenate([summary, block], axis=concat_dim)
            num_columns_read = summary.shape[concat_dim]
            if num_columns_read >= num_columns_to_return:
                break
        cols = slice(0, num_columns_to_return)
        return summary[..., cols]


def get_model_explanation(run):
    """Return the feature importance values.

    Parameters:
        run : azureml.core.run.Run
            An object that represents a model explanation run.

    Returns:
        feature_importance_values : numpy.ndarray or list[numpy.ndarray]
            For a model with a single output such as regression, this returns a matrix of feature
            importance values. For models with vector outputs this function returns a list of such
            matrices, one for each output. The dimension of this matrix is (# examples x # features).

        expected_values : numpy.ndarray
            The expected value of the model applied to the set of initialization examples.
            For SHAP values, when a version older than 0.20.0 is used, this value is None. The expected
            values are in the last columns of the matrices in feature_importance_values. In this case, the
            dimension of those matrix is (# examples x (# features + 1)). This causes each row to sum to
            the model output for that example.
    """
    download_dir = _create_download_dir()
    shap_values = _download_artifact(run, download_dir, 'shap_values')
    expected_values = None
    try:
        expected_values = _download_artifact(run, download_dir, 'expected_values')
    except Exception:
        module_logger.warning(
            "expected_values is not found in Artifact service")
    return shap_values, expected_values


def get_model_explanation_from_run_id(workspace, experiment_name, run_id):
    """Return the feature importance values.

    Parameters:
        workspace : azureml.core.workspace.Workspace
            An object that represents a workspace.

        experiment_name : str
            The name of the experiment.

        run_id : str
            A GUID that represents a run.

    Returns:
        feature_importance_values : numpy.ndarray or list[numpy.ndarray]
            For a model with a single output such as regression, this returns a matrix of feature
            importance values. For models with vector outputs this function returns a list of such
            matrices, one for each output. The dimension of this matrix is (# examples x # features).

        expected_values : numpy.ndarray
            The expected value of the model applied to the set of initialization examples.
            For SHAP values, when a version older than 0.20.0 is used, this value is None. The expected
            values are in the last columns of the matrices in feature_importance_values. In this case, the
            dimension of those matrix is (# examples x (# features + 1)). This causes each row to sum to
            the model output for that example.
    """
    try:
        from azureml.core import Experiment, Run
    except ImportError as exp:
        module_logger.error("Could not import azureml.core.run")
        raise exp
    experiment = Experiment(workspace, experiment_name)
    run = Run(experiment, run_id=run_id)
    shap_values, expected_values = get_model_explanation(run)
    return shap_values, expected_values


def get_model_summary_from_run_id(workspace, experiment_name, run_id, overall_summary_only=False, top_k=None):
    """Return the feature importance values.

    Parameters:
        workspace : azureml.core.workspace.Workspace
            An object that represents a workspace.

        experiment_name : str
            The name of an experiment_name.

        run_id : str
            A GUID that represents a run.

        overall_summary_only : bool
            A flag that indicates whether to return per class summary.

        top_k : int
            An integer that indicates the number of the most important features to return.

    Returns:
        overall_feature_importance_values : numpy.ndarray
            The model level feature importance values sorted in descending order.

        overall_important_features : numpy.ndarray
            The feature names sorted in the same order as in overall_summary or the indexes that would
            sort overall_summary.

        per_class_feature_importance_values :  numpy.ndarray
            The class level feature importance values sorted in descending order where a binary classification
            (this class or not) is evaluated. Only available for the classification case.

        per_class_important_features : numpy.ndarray
            The feature names sorted in the same order as in per_class_summary or the indexes that would
            sort per_class_summary. Only available for the classification case.
    """
    try:
        from azureml.core import Experiment, Run
    except ImportError as exp:
        module_logger.error("Could not import azureml.core.run")
        raise exp
    experiment = Experiment(workspace, experiment_name)
    run = Run(experiment, run_id=run_id)
    return get_model_summary(run, overall_summary_only, top_k)


def get_model_summary(run, overall_summary_only=False, top_k=None):
    """Return the feature importance values.

    Parameters:
        run : azureml.core.run.Run
            An object that represents a model explanation run.

        overall_summary_only : bool
            A flag that indicates whether to return per class summary.

        top_k : int
            An integer that indicates the number of the most important features to return.

    Returns:
        overall_feature_importance_values : numpy.ndarray
            The model level feature importance values sorted in descending order.

        overall_important_features : numpy.ndarray
            The feature names sorted in the same order as in overall_summary or the indexes that would
            sort overall_summary.

        per_class_feature_importance_values :  numpy.ndarray
            The class level feature importance values sorted in descending order where a binary classification
            (this class or not) is evaluated. Only available for the classification case.

        per_class_important_features : numpy.ndarray
            The feature names sorted in the same order as in per_class_summary or the indexes that would
            sort per_class_summary. Only available for the classification case.
    """
    download_dir = _create_download_dir()
    feature_names = None
    try:
        feature_names = _download_artifact(run, download_dir, 'feature_names')
    except Exception:
        module_logger.info(
            "feature_names is not found in Artifact service")
    overall_summary = _download_model_summary(run, download_dir, 'overall_summary', top_k)
    overall_importance_order = _download_model_summary(run, download_dir, 'overall_importance_order', top_k)
    overall_importance = overall_importance_order
    if (feature_names is not None):
            overall_importance = _sort_features(feature_names, overall_importance_order)
    model_type = run.get_metrics()['model_type']
    if model_type == "classification" and not overall_summary_only:
        per_class_summary = _download_model_summary(run, download_dir, 'per_class_summary', top_k)
        per_class_importance_order = _download_model_summary(run, download_dir, 'per_class_importance_order', top_k)
        per_class_importance = per_class_importance_order
        if (feature_names is not None):
            per_class_importance = _sort_features(feature_names, per_class_importance_order)
        return overall_summary, overall_importance, per_class_summary, per_class_importance
    else:
        return overall_summary, overall_importance


def get_classes(run):
    """Return the class names or None if not found in Artifact service.

    Parameters:
        run : azureml.core.run.Run
            An object that represents a model explanation run.

    Returns:
        class_names : numpy.ndarray
            The class names passed to explain_model.  The order of the class names matches the model output.
    """
    download_dir = _create_download_dir()
    classes = None
    try:
        classes = _download_artifact(run, download_dir, 'classes')
    except Exception:
        module_logger.warning(
            "classes is not found in Artifact service")
    return classes
