# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Defines utilities to explain and visualize the feature importances of a model."""
import os
import pickle
import numpy as np
import pandas as pd
import logging
import shap
import scipy as sp
import math

module_logger = logging.getLogger(__name__)
module_logger.setLevel(logging.INFO)
new_shap_api = True
minimum_shap__version = '0.20.0'
maximum_shap__version = '0.24.0'
MAX_NUM_BLOCKS = "max_num_blocks"
BLOCK_SIZE = "block_size"
NUM_FEATURES = "num_features"
NUM_BLOCKS = "num_blocks"

try:
    import pkg_resources
    from distutils.version import StrictVersion
    shap_version = pkg_resources.get_distribution("shap").version
    new_shap_api = StrictVersion(shap_version) >= StrictVersion(minimum_shap__version)
    if not new_shap_api:
        module_logger.warning(
            "An older version of SHAP than the mimimum requirement %s is used", minimum_shap__version)
    if StrictVersion(shap_version) > StrictVersion(maximum_shap__version):
        module_logger.warning(
            "A newer version of SHAP than the supported version %s is used", maximum_shap__version)
except ImportError:
    module_logger.debug("Failed to determine the version of SHAP")


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


def _sort_features(features, order):
        return np.array(features)[order]


def get_model_explanation(run):
    """Return the feature importance values.

    Parameters:
        run : azureml.core.run.Run
            An object that represents a model explanation run.

    Returns:
        feature_importance_values : numpy.ndarray or list[numpy.ndarray]
            For a model with a single output such as regression, this returns a matrix of feature
            importance values. For models with vector outputs this function returns a list of such
            matrices, one for each output. The dimension of these matrix is (# examples x # features).

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
            matrices, one for each output. The dimension of these matrix is (# examples x # features).

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

        overall_important_features : list[str] or numpy.ndarray
            The feature names sorted in the same order as in overall_summary or the indexes that would
            sort overall_summary.

        per_class_feature_importance_values :  numpy.ndarray
            The class level feature importance values sorted in descending order where a binary classification
            (this class or not) is evaluated. Only available for the classification case.

        per_class_important_features : list[list[str]] or numpy.ndarray
            The feature names sorted in the same order as in per_class__summary or the indexes that would
            sort per_class__summary. Only available for the classification case.
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

        overall_important_features : list[str] or numpy.ndarray
            The feature names sorted in the same order as in overall_summary or the indexes that would
            sort overall_summary.

        per_class_feature_importance_values :  numpy.ndarray
            The class level feature importance values sorted in descending order where a binary classification
            (this class or not) is evaluated. Only available for the classification case.

        per_class_important_features : list[list[str]] or numpy.ndarray
            The feature names sorted in the same order as in per_class__summary or the indexes that would
            sort per_class__summary. Only available for the classification case.
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
            overall_importance = _sort_features(feature_names, overall_importance_order).tolist()
    model_type = run.get_metrics()['model_type']
    if model_type == "classification" and not overall_summary_only:
        per_class_summary = _download_model_summary(run, download_dir, 'per_class_summary', top_k)
        per_class_importance_order = _download_model_summary(run, download_dir, 'per_class_importance_order', top_k)
        per_class_importance = per_class_importance_order
        if (feature_names is not None):
            per_class_importance = _sort_features(feature_names, per_class_importance_order).tolist()
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


def summarize_data(X, k, to_round_values=True):
    """Summarize a dataset.
    For dense dataset, use k mean samples weighted by the number of data points they
    each represent.
    For sparse dataset, use a sparse row for the background with calculated
    median for dense columns.

    Parameters:
        X : numpy.array, pandas.DataFrame or scipy.sparse.csr_matrix
            Matrix of data samples to summarize (# samples x # features).

        k : int
        Number of cluster centroids to use for approximation.

        to_round_values : bool
        When using kmeans, for each element of every cluster centroid to match the nearest value
        from X in the corresponding dimension. This ensures discrete features
        always get a valid value.  Ignored for sparse data sample.

    Returns:
        It returns a DenseData or SparseData object of type iml.datatypes.DenseData or iml.datatypes.SparseData.
    """
    from shap.common import DenseData
    is_sparse = sp.sparse.issparse(X)
    if not isinstance(X, DenseData):
        if is_sparse:
            # instead of using kmeans, pass in background of zeros
            # for dense columns, calculate median of data
            # TODO: calculate median of data here
            return sp.sparse.csr_matrix((1, X.shape[1]), dtype=X.dtype)
        elif len(X) > 10 * k:
            # use kmeans to summarize the examples for initialization
            # if there are more than 10 x k of them
            return shap.kmeans(X, k, to_round_values)
    return X


def explanation_policy(allow_eval_sampling=False, max_dim_clustering=50, explain_subset=None, **kwargs):
    """A set of parameters that can be tuned to speed up or improve the accuracy of the
    explain_model function. For execution time improvement, samples the evaluation
    data and/or reduces the set of features explained.

    Parameters:
        allow_eval_sampling : bool
            Default to 'False'. Specify whether to allow sampling of evaluation data.
            If 'True', cluster the evaluation data and determine the optimal number
            of points for sampling. Set to 'True' to speed up the process when the
            evaluation data set is large and the user only wants to generate model
            summary info.

        max_dim_clustering : int
            Default to 50 and only take effect when 'allow_eval_sampling' is set to 'True'.
            Specify the dimensionality to reduce the evaluation data before clustering for sampling.
            When doing sampling to determine how aggressively to downsample without getting poor
            explanation results uses a heuristic to find the optimal number of clusters. Since
            KMeans performs poorly on high dimensional data PCA or Truncated SVD is first run to
            reduce the dimensionality, which is followed by finding the optimal k by running
            KMeans until a local minimum is reached as determined by computing the silhouette
            score, reducing k each time.

        explain_subset : list[int]
            List of feature indices. If specified, only selects a subset of the features in the
            evaluation dataset for explanation, which will speed up the explanation process when
            number of features is large and the user already knows the set of interested features.
            The subset can be the top-k features from the model summary.

    Returns:
            kwargs : dict
                The arguments for the sampling policy
    """
    kwargs["allow_eval_sampling"] = allow_eval_sampling
    kwargs["max_dim_clustering"] = max_dim_clustering
    kwargs["explain_subset"] = explain_subset
    return kwargs


class BaseExplainer:
    """The base class for explainers."""
    def __init__(self, workspace=None, experiment_name=None, run_id=None):
        """Initializes the explainer.

        Parameters:
            workspace : azureml.core.workspace.Workspace
                An object that represents a workspace.

            experiment_name : str
                The name of an experiment.

            run_id : str
                A GUID that represents a run.
        """
        self.run = None
        self.storage_policy = {MAX_NUM_BLOCKS: 3, BLOCK_SIZE: 100}
        args_none = [arg is None for arg in [workspace, experiment_name]]
        # Validate either all the arguments above are specified or all are None
        if not any(args_none):
            try:
                from azureml.core import Experiment, Run
            except ImportError as exp:
                module_logger.error(
                    "Could not import azureml.core, required if specifying workspace and experiment name")
                raise exp
            experiment = Experiment(workspace, experiment_name)
            if run_id is None:
                # Create a new run
                self.run = experiment.start_logging()
            else:
                # Create a run object to reference the original one with the same run_id
                self.run = Run(experiment, run_id=run_id)
        elif not all(args_none):
            raise ValueError("Both or neither of workspace and experiment name need to be specified")

    def _order_imp(self, summary):
        if new_shap_api:
            return summary.argsort()[..., ::-1]
        else:
            module_logger.debug(
                "An older version of SHAP than the mimimum requirement %s is used", minimum_shap__version)
            return summary[..., 0:-1].argsort()[..., ::-1]

    def _create_upload_dir(self):
        # create the outputs folder
        upload_dir = './upload_explanation/'
        os.makedirs(upload_dir, exist_ok=True)
        return upload_dir

    def _upload_artifact(self, upload_dir, artifact_name, values):
        # serialize the shap values on disk in the special 'outputs' folder
        path = os.path.join(upload_dir, artifact_name + '.pkl')
        f = open(path, 'wb')
        pickle.dump(values, f)
        f.close()
        self.run.upload_file(artifact_name + '.pkl', path)

    def _get_num_of_blocks(self, num_of_columns):
        block_size = self.storage_policy[BLOCK_SIZE]
        num_blocks = math.ceil(num_of_columns / block_size)
        max_num_blocks = self.storage_policy[MAX_NUM_BLOCKS]
        if num_blocks > max_num_blocks:
            num_blocks = max_num_blocks
        return num_blocks

    def _upload_model_summary(self, upload_dir, name, summary):
        num_columns = summary.shape[len(summary.shape) - 1]
        num_blocks = self._get_num_of_blocks(num_columns)
        block_size = self.storage_policy[BLOCK_SIZE]
        storage_metadata = dict()
        storage_metadata[MAX_NUM_BLOCKS] = [self.storage_policy[MAX_NUM_BLOCKS]]
        storage_metadata[BLOCK_SIZE] = [self.storage_policy[BLOCK_SIZE]]
        storage_metadata[NUM_FEATURES] = [num_columns]
        storage_metadata[NUM_BLOCKS] = [num_blocks]
        # Save metadata for this summary to Run History
        self.run.log_table(name, storage_metadata)
        # Chunk the summary and save it to Artifact
        start = 0
        for idx in range(num_blocks - 1):
            cols = slice(start, start + block_size)
            block = summary[..., cols]
            block_name = name + "_" + str(idx)
            self._upload_artifact(upload_dir, block_name, block)
            start += block_size
        # The last block
        cols = slice(start, num_columns)
        block = summary[..., cols]
        block_name = name + "_" + str(num_blocks - 1)
        self._upload_artifact(upload_dir, block_name, block)

    def get_storage_policy(self):
        """Returns the current storage policy.

        Returns:
                storage_policy : dict
                    The storage policy represented as a dictionary of settings.
        """
        # return the current storage policy
        return self.storage_policy

    def set_storage_policy(self, block_size=None, max_num_blocks=None):
        """Sets the current storage policy.

        Parameters:
            block_size : int
                The size of each block for the summary stored in artifacts storage.

            max_num_blocks : int
                The maximum number of blocks to store.
        """
        if block_size is not None:
            self.storage_policy[BLOCK_SIZE] = block_size
        if max_num_blocks is not None:
            self.storage_policy[MAX_NUM_BLOCKS] = max_num_blocks


class TabularExplainer(BaseExplainer):
    """Explain a model trained on a tabular dataset."""
    def __init__(self, workspace=None, experiment_name=None, run_id=None):
        """Initializes the Tabular Explainer.

        Parameters:
            workspace : azureml.core.workspace.Workspace
                An object that represents a workspace.

            experiment_name : str
                The name of an experiment.

            run_id : str
                A GUID that represents a run.
        If workspace and experiment_name are provided, a new Run will be created and the model
        explanation data will be stored and managed by Run History service. The explanation
        data will be associated with this new Run and can be retrieved at a later time,
        for example, through its ID. If workspace, experiment_name and run_id are all provided,
        the explanation data will be associated with the Run that has the same Run ID.
        Otherwise, the data are only available locally.
        """
        BaseExplainer.__init__(self, workspace, experiment_name, run_id)

    def _reduce_eval_examples(self, evaluation_examples, max_dim_clustering=50):
        """Reduces the dimensionality of the evaluation examples if dimensionality is higher
        than max_dim_clustering.  If the dataset is sparse, we mean-scale the data and then run
        truncated SVD to reduce the number of features to max_dim_clustering.  For dense
        dataset, we also scale the data and then run PCA to reduce the number of features to
        max_dim_clustering.
        This is used to get better clustering results in _find_k.
        """
        from sklearn.decomposition import TruncatedSVD, PCA
        from sklearn.preprocessing import StandardScaler
        num_cols = evaluation_examples.shape[1]
        # Run PCA or SVD on input data and reduce to about 50 features prior to clustering
        components = min(max_dim_clustering, num_cols)
        reduced_eval_examples = evaluation_examples
        if components != num_cols:
            if sp.sparse.issparse(evaluation_examples):
                normalized_eval_examples = StandardScaler(with_mean=False).fit_transform(evaluation_examples)
                reducer = TruncatedSVD(n_components=components)
            else:
                normalized_eval_examples = StandardScaler().fit_transform(evaluation_examples)
                reducer = PCA(n_components=components)
            module_logger.info("reducing dimensionality to " + str(components) + " components for clustering")
            reduced_eval_examples = reducer.fit_transform(normalized_eval_examples)
        return reduced_eval_examples

    def _find_k_kmeans(self, evaluation_examples, max_dim_clustering=50):
        """Uses k-means to downsample the evaluation examples.
        Starting from k_upper_bound, cuts k in half each time and run k-means
        clustering on the evaluation_examples.  After each run, computes the
        silhouette score and stores k with highest silhouette score.
        We use optimal k to determine how much to downsample the evaluation_examples.
        """
        from sklearn.cluster import KMeans
        from sklearn.metrics import silhouette_score
        from math import log, isnan, ceil
        reduced_eval_examples = self._reduce_eval_examples(evaluation_examples, max_dim_clustering)
        num_rows = evaluation_examples.shape[0]
        # TODO: Eventually use OPTICS which automatically
        # determines clusters, in next sklearn release, eg:
        # opt = OPTICS(min_samples=1).fit(reduced_eval_examples)
        k_upper_bound = 2000
        k_list = []
        k = min(num_rows / 2, k_upper_bound)
        for i in range(int(ceil(log(num_rows, 2) - 7))):
            k_list.append(int(k))
            k /= 2
        prev_highest_score = -1
        prev_highest_index = 0
        opt_k = int(k)
        for k_index, k in enumerate(k_list):
            module_logger.info("running KMeans with k: " + str(k))
            km = KMeans(n_clusters=k).fit(reduced_eval_examples)
            clusters = km.labels_
            num_clusters = len(set(clusters))
            k_too_big = num_clusters <= 1
            if k_too_big or num_clusters == reduced_eval_examples.shape[0]:
                score = -1
            else:
                score = silhouette_score(reduced_eval_examples, clusters)
            if isnan(score):
                score = -1
            module_logger.info("KMeans silhouette score: " + str(score))
            # Find k with highest silhouette score for optimal clustering
            if score >= prev_highest_score and not k_too_big:
                prev_highest_score = score
                prev_highest_index = k_index
        opt_k = k_list[prev_highest_index]
        module_logger.info("best silhouette score: " + str(prev_highest_score))
        module_logger.info("found optimal k for KMeans: " + str(opt_k))
        return opt_k

    def _find_k_hdbscan(self, evaluation_examples, max_dim_clustering=50):
        import hdbscan
        num_rows = evaluation_examples.shape[0]
        reduced_eval_examples = self._reduce_eval_examples(evaluation_examples, max_dim_clustering)
        hdbs = hdbscan.HDBSCAN(min_cluster_size=2).fit(reduced_eval_examples)
        clusters = hdbs.labels_
        opt_k = len(set(clusters))
        clustering_threshold = 5
        samples = opt_k * clustering_threshold
        module_logger.info("found optimal k for hdbscan: " + str(opt_k) +
                           ", will use clustering_threshold * k for sampling: " + str(samples))
        return min(samples, num_rows)

    def _sample_evaluation_examples(self, evaluation_examples, max_dim_clustering=50, sampling_method="hdbscan"):
        """Samples the evaluation examples.  First does random downsampling to upper_bound rows,
        then tries to find the optimal downsample based on how many clusters can be constructed
        from the data.  If sampling_method is hdbscan, uses hdbscan to cluster the evaluation
        data and then downsamples to that number of clusters.  If sampling_method is k-means,
        uses different values of k, cutting in half each time, and chooses the k with highest
        silhouette score to determine how much to downsample the data.
        The danger of using only random downsampling is that we might downsample too much
        or too little, so the clustering approach is a heuristic to give us some idea of
        how much we should downsample to.
        """
        from sklearn.utils import resample
        lower_bound = 200
        upper_bound = 10000
        num_rows = evaluation_examples.shape[0]
        module_logger.info("sampling evaluation examples")
        # If less than lower_bound rows, just return the full dataset
        if num_rows < lower_bound:
            return evaluation_examples
        # If more than upper_bound rows, sample randomly
        elif num_rows > upper_bound:
            module_logger.info("randomly sampling to 10k rows")
            evaluation_examples = resample(evaluation_examples, n_samples=upper_bound, random_state=7)
            num_rows = upper_bound
        if sampling_method == "hdbscan":
            try:
                opt_k = self._find_k_hdbscan(evaluation_examples, max_dim_clustering)
            except Exception as ex:
                module_logger.warning("Failed to use hdbscan due to error: " + str(ex) +
                                      "\nEnsure hdbscan is installed with: pip install hdbscan")
                opt_k = self._find_k_kmeans(evaluation_examples, max_dim_clustering)
        else:
            opt_k = self._find_k_kmeans(evaluation_examples, max_dim_clustering)
        # Resample based on optimal number of clusters
        if (opt_k < num_rows):
            return resample(evaluation_examples, n_samples=opt_k, random_state=7)
        return evaluation_examples

    # Single node explain model function
    def explain_model(self, model, initialization_examples, evaluation_examples=None,
                      features=None, classes=None, nsamples='auto', nclusters=10,
                      top_k=None, **kwargs):
        """Explain a model by explaining its predictions on samples.

        Parameters:
            model : object
                An object that represents a model. It is assumed that for the classification case
                it has a method of predict_proba() returning the prediction probabilities for each
                class and for the regression case a method of predict() returning the prediction value.

            initialization_examples : numpy.array, pandas.DataFrame, iml.datatypes.DenseData or
                                      scipy.sparse.csr_matrix
                A matrix of feature vector examples (# examples x # features) for initializing the
                explainer. For small problems this set of examples for initialization can be the whole
                training set, but for larger problems consider using a single reference value or using
                the built-in kmeans function to summarize the whole or downsampled training set by
                specifying nclusters (the number of cluster centroids). A function summarize_data is
                also provided to summarize the initialization_examples separately. The output of this
                function can be passed to this method.

            evaluation_examples : numpy.array, pandas.DataFrame or scipy.sparse.csr_matrix
                A matrix of feature vector examples (# examples x # features) on which to explain the
                model's output.

            features : list[str]
                A list of feature names.

            classes : array_like[str]
                Class names, in any form that can be converted to an array of str. This includes lists,
                lists of tuples, tuples, tuples of tuples, tuples of lists and ndarrays. The order of
                the class names should match that of the model output.

            nsamples : "auto" or int
                Number of times to re-evaluate the model when explaining each prediction. More samples
                lead to lower variance estimates of the feature importance values, but incur more
                computation cost. When "auto" is provided, the number of samples is computed according
                to a heuristic rule.

            nclusters : int
                Number of means to use for approximation. A dataset is summarized with nclusters mean samples
                weighted by the number of data points they each represent. When the number of initialization
                examples is larger than (10 x nclusters), those examples will be summarized with k-means where
                k = nclusters.

            top_k : int
                Number of the top most important features in model summary. If specified, only the model summary
                data corresponding to the top K most important features will be returned/stored.

        Returns:
                run : azureml.core.run.Run
                    An object that represents an model explanation run. Only
                    availabe if workspace and experiment_name
                    are both provided.

                feature_importance_values : numpy.ndarray or list[numpy.ndarray]
                    For a model with a single output such as regression, this returns a matrix of feature
                    importance values. For models with vector outputs this function returns a list of such
                    matrices, one for each output. The dimension of these matrix is (# examples x # features).

                expected_values : numpy.ndarray
                    The expected value of the model applied to the set of initialization examples.
                    For SHAP values, when a version older than 0.20.0 is used, this value is None. The expected
                    values are in the last columns of the matrices in feature_importance_values. In this case, the
                    dimension of those matrix is (# examples x (# features + 1)). This causes each row to sum to
                    the model output for that example.

                overall_feature_importance_values : numpy.ndarray
                    The model level feature importance values sorted in descending order.

                overall_important_features : list[str] or numpy.ndarray
                    The feature names sorted in the same order as in overall_summary or the indexes that would
                    sort overall_summary.

                per_class_feature_importance_values :  numpy.ndarray
                    The class level feature importance values sorted in descending order where a binary classification
                    (this class or not) is evaluated. Only available for the classification case.

                per_class_important_features : list[list[str]] or numpy.ndarray
                    The feature names sorted in the same order as in per_class__summary or the indexes that would
                    sort per_class__summary. Only available for the classification case.
        """
        if evaluation_examples is None:
            raise ValueError("evaluation_examples is required")
        explainer = None
        expected_values = None
        explain_subset = kwargs.get("explain_subset", None)
        try:
            module_logger.debug("Attempting to use TreeExplainer")
            # try to use TreeExplainer which is more accurate first
            explainer = shap.TreeExplainer(model)

            # for now convert evaluation examples to dense format if they are sparse
            # until TreeExplainer csr support is added
            def get_tree_examples(examples):
                if sp.sparse.issparse(examples):
                    return examples.toarray()
                return examples

            shap_values = explainer.shap_values(get_tree_examples(evaluation_examples))
            classification = isinstance(shap_values, list)
            if explain_subset:
                if classification:
                    for i in range(shap_values.shape[0]):
                        shap_values[i] = shap_values[i][:, explain_subset]
                else:
                    shap_values = shap_values[:, explain_subset]
        except Exception as ex:
            # if TreeExplainer is not supported use KernelExplainer
            module_logger.debug("Could not use tree explainer, using KernelExplainer instead: " + str(ex))
            if explain_subset:
                original_evaluation = evaluation_examples
                if isinstance(original_evaluation, pd.DataFrame) or isinstance(original_evaluation, pd.Series):
                    original_evaluation = original_evaluation.values
                evaluation_examples = original_evaluation[:, explain_subset]
                if isinstance(initialization_examples, pd.DataFrame) or isinstance(initialization_examples, pd.Series):
                    initialization_examples = initialization_examples.values
                initialization_examples = initialization_examples[:, explain_subset]
            summary = summarize_data(initialization_examples, nclusters)
            # sample the evaluation examples
            allow_eval_sampling = kwargs.get('allow_eval_sampling', False)
            if allow_eval_sampling:
                max_dim_clustering = kwargs.get("max_dim_clustering", 50)
                sampling_method = kwargs.get("sampling_method", "hdbscan")
                evaluation_examples = self._sample_evaluation_examples(evaluation_examples, max_dim_clustering,
                                                                       sampling_method=sampling_method)

            def shap_values_on_prediction(f, summary):
                # Note: we capture index and f in the wrapper function below around the model prediction function.
                # When enumerating over the examples this values is updated and the update is visible in the
                # wrapper function below.  This is necessary to determine which example to tile when translating
                # back to the model's input domain.
                idx = 0

                def wrapper(data):
                    """
                    A private wrapper around the prediction function to add back in the removed columns
                    when using the explain_subset parameter.
                    We tile the original evaluation row by the number of samples generated
                    and replace the subset of columns the user specified with the result from shap,
                    which is the input data passed to the wrapper.
                    :return: The prediction function wrapped by a helper method.
                    """
                    tiles = int(data.shape[0])
                    evaluation_row = original_evaluation[idx]
                    if sp.sparse.issparse(evaluation_row):
                        if not sp.sparse.isspmatrix_csr(evaluation_row):
                            evaluation_row = evaluation_row.tocsr()
                        nnz = evaluation_row.nnz
                        rows, cols = evaluation_row.shape
                        rows *= tiles
                        shape = rows, cols
                        if nnz == 0:
                            examples = sp.sparse.csr_matrix(shape, dtype=evaluation_row.dtype).tolil()
                        else:
                            new_indptr = np.arange(0, rows * nnz + 1, nnz)
                            new_data = np.tile(evaluation_row.data, rows)
                            new_indices = np.tile(evaluation_row.indices, rows)
                            examples = sp.sparse.csr_matrix((new_data, new_indices, new_indptr),
                                                            shape=shape).tolil()
                    else:
                        examples = np.tile(original_evaluation[idx], tiles).reshape((data.shape[0],
                                                                                    original_evaluation.shape[1]))
                    examples[:, explain_subset] = data
                    return f(examples)

                model_func = f
                if explain_subset:
                    model_func = wrapper
                explainer = shap.KernelExplainer(model_func, summary)
                if explain_subset:
                    output_shap_values = None
                    for ex_idx, example in enumerate(evaluation_examples):
                        idx = ex_idx
                        tmp_shap_values = explainer.shap_values(example, nsamples=nsamples)
                        classification = isinstance(tmp_shap_values, list)
                        if classification:
                            if output_shap_values is None:
                                output_shap_values = tmp_shap_values
                                for i in range(len(output_shap_values)):
                                    cols_dim = len(output_shap_values[i].shape)
                                    concat_cols = output_shap_values[i].shape[cols_dim - 1]
                                    output_shap_values[i] = output_shap_values[i].reshape(1, concat_cols)
                            else:
                                for i in range(len(output_shap_values)):
                                    cols_dim = len(tmp_shap_values[i].shape)
                                    # col_dim can only be 1 or 2 here, depending on data passed to shap
                                    if cols_dim != 2:
                                        out_cols_dim = len(output_shap_values[i].shape)
                                        output_size = output_shap_values[i].shape[out_cols_dim - 1]
                                        tmp_shap_values_2d = tmp_shap_values[i].reshape(1, output_size)
                                    else:
                                        tmp_shap_values_2d = tmp_shap_values[i]
                                    # Append rows
                                    output_shap_values[i] = np.append(output_shap_values[i],
                                                                      tmp_shap_values_2d, axis=0)
                        else:
                            if output_shap_values is None:
                                output_shap_values = tmp_shap_values
                            else:
                                output_shap_values = np.append(output_shap_values, tmp_shap_values, axis=0)
                    return output_shap_values, explainer
                else:
                    return explainer.shap_values(evaluation_examples, nsamples=nsamples), explainer

            def classification_shap_values(model, summary):
                f = model.predict_proba
                return shap_values_on_prediction(f, summary)

            def regression_shap_values(model, summary):
                f = model.predict
                return shap_values_on_prediction(f, summary)

            try:
                # try to use predict_proba for classification scenario
                shap_values, explainer = classification_shap_values(model, summary)
            except AttributeError as ae:
                module_logger.info(
                    "predict_proba not supported by given model, assuming regression model and trying predict: " +
                    str(ae))
                # try predict instead since this is likely a regression scenario
                shap_values, explainer = regression_shap_values(model, summary)
            classification = isinstance(shap_values, list)
        if explainer is not None and hasattr(explainer, "expected_value"):
            expected_values = explainer.expected_value
        is_projection_required = False if top_k is None else True
        if classification:
            # calculate the summary
            per_class_summary = np.mean(np.absolute(shap_values), axis=1)
            i = np.arange(len(per_class_summary))[:, np.newaxis]
            per_class_order = self._order_imp(per_class_summary)
            overall_summary = np.mean(per_class_summary, axis=0)
            overall_order = self._order_imp(overall_summary)
            if is_projection_required and len(overall_order) > top_k:
                overall_order = overall_order[0:top_k]
                per_class_order = per_class_order[:, 0:top_k]
            # sort the per class summary
            per_class_summary = per_class_summary[i, per_class_order]
            # sort the overall summary
            overall_summary = overall_summary[overall_order]
        else:
            overall_summary = np.mean(np.absolute(shap_values), axis=0)
            overall_order = self._order_imp(overall_summary)
            if is_projection_required and len(overall_order) > top_k:
                overall_order = overall_order[0:top_k]
            # sort the overall summary
            overall_summary = overall_summary[overall_order]
        if features is not None:
            overall_imp = _sort_features(features, overall_order).tolist()
            if classification:
                per_class_imp = _sort_features(features, per_class_order).tolist()
        elif isinstance(initialization_examples, pd.DataFrame):
            features = initialization_examples.columns
            overall_imp = _sort_features(features, overall_order).tolist()
            if classification:
                per_class_imp = _sort_features(features, per_class_order).tolist()
        else:
            # return order of importance
            overall_imp = overall_order
            if classification:
                per_class_imp = per_class_order
        if self.run is not None:
            # log the values to run history
            model_type = "classification" if classification else "regression"
            self.run.log('model_type', model_type)
            self.run.log('explainer', 'tabular')
            # pickle the shap values, overall summary and per class summary
            upload_dir = self._create_upload_dir()
            self._upload_artifact(upload_dir, 'shap_values', shap_values)
            if expected_values is not None:
                self._upload_artifact(upload_dir, 'expected_values', expected_values)
            if features is not None:
                self._upload_artifact(upload_dir, 'feature_names', features)
            self._upload_model_summary(upload_dir, 'overall_summary', overall_summary)
            self._upload_model_summary(upload_dir, 'overall_importance_order', overall_order)
            if classification:
                self._upload_model_summary(upload_dir, 'per_class_summary', per_class_summary)
                self._upload_model_summary(upload_dir, 'per_class_importance_order', per_class_order)
                # Only for the classification scenario
                self._upload_artifact(upload_dir, 'classes', np.asarray(classes))
            if classification:
                return self.run, shap_values, expected_values, overall_summary, overall_imp, \
                    per_class_summary, per_class_imp
            else:
                return self.run, shap_values, expected_values, overall_summary, overall_imp
        else:
            if classification:
                return shap_values, expected_values, overall_summary, overall_imp, per_class_summary, per_class_imp
            else:
                return shap_values, expected_values, overall_summary, overall_imp
