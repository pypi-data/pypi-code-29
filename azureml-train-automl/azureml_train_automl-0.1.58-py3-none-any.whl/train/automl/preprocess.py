# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""Global methods used during an AutoML fit method for pre-processing raw data into meaningful features."""
import math
import re

import dateutil
import numpy as np
import pandas as pd
from scipy import sparse
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import LabelEncoder
from sklearn.utils import murmurhash3_32
from sklearn_pandas import DataFrameMapper

from .constants import Tasks
from .utilities import (_get_column_data_type_as_str,
                        _check_if_column_data_type_is_numerical,
                        _check_if_column_data_type_is_int
                        )


class BinTransformer(BaseEstimator, TransformerMixin):
    """
    Wrapper over pandas.cut for binning the train data into intervals and then applying them to test data.

    :param num_bins: Number of bins for binning the values into discrete intervals.
    :type num_bins: int
    """
    def __init__(self, num_bins=5):
        """
        Constructor for BinTransformer.

        :param num_bins: Number of bins for binning the values into discrete intervals.
        :type num_bins: int
        """

        self._num_bins = num_bins
        self._bins = None

    def fit(self, x, y=None):
        """
        Identify the distribution of values with repect to the number of specified bins.

        :param x: The data to transform.
        :type x: numpy.ndarray or pandas.series
        :param y: Target values.
        :type y: numpy.ndarray
        :return: The transformed data.
        """
        _, self._bins = pd.cut(x, self._num_bins, retbins=True)
        return self

    def transform(self, x):
        """
        Return the bins identified for the input values.

        :param x: The data to transform.
        :type x: numpy.ndarray or pandas.series
        :return: The transformed data.
        """
        if self._bins is None:
            raise ValueError("BinTransformer not fit")
        return pd.cut(x, bins=self._bins, labels=False)


class NaiveBayes(BaseEstimator, TransformerMixin):
    """
    Wrapper for sklearn Multinomial Naive Bayes.
    """

    def __init__(self):
        """
        Constructor for Naive Bayes transformer.
        """
        self.model = MultinomialNB()

    def fit(self, x, y=None):
        """
        Fit function for Naive Bayes transform to learn conditional probablities for textual data.

        :param x: The data to transform.
        :type x: numpy.ndarray or pandas.series
        :param y: Target values.
        :type y: numpy.ndarray
        :return: Naive Bayes class object.
        """
        self.model.fit(x, y)
        return self

    def transform(self, x):
        """
        Transforms data x

        :param x: The data to transform.
        :type x: numpy.ndarray or pandas.series
        :return: Prediction probability values from Naive Bayes model.
        """
        return self.model.predict_proba(x)


class ImputationMarker(BaseEstimator, TransformerMixin):
    """
    Add boolean imputation marker for values that are imputed.
    """

    def fit(self, x, y=None):
        """
        Fit function for imputation marker transform.

        :param x: Input array of integers or strings.
        :type x: numpy.ndarray or pandas.series
        :param y: Target values.
        :type y: numpy.ndarray
        :return: Class object itself.
        """
        return self

    def transform(self, x):
        """
        Transform function for imputation marker.

        :param x: Input array of integers or strings.
        :type x: numpy.ndarray or pandas.series
        :return: Boolean array having True where the value is not present.
        """
        return pd.isna(x).values


class CatImputer(BaseEstimator, TransformerMixin):
    """
    Impute missing values for categorical data by the most frequent category.

    :param copy: Create copy of the categorical column.
    :type copy: boolean
    """

    def __init__(self, copy=True):
        """
        Constructor for CatImputer.

        :param copy: Create copy of the categorical column.
        :type copy: boolean
        :return:
        """
        self._missing_vals = [np.nan]
        self._copy = copy

    def _get_mask(self, x):
        """
        Get missing values mask.

        :param x: Input array.
        :return: Mask with missing values.
        """
        mask = np.zeros(x.shape, dtype=bool)
        x_object = None
        for val in self._missing_vals:
            if val is None or (isinstance(val, float) and np.isnan(val)):
                mask = mask | pd.isnull(x)
            else:
                x_object = x.astype(
                    np.object) if x_object is None else x_object
                mask = mask | (x_object == val)

        return mask

    def fit(self, x, y=None):
        """
        Transforms the data to mark the missing values and identify the most frequent category.

        :param x: The data to transform.
        :type x: numpy.ndarray or pandas.series
        :param y: Target values.
        :type y: numpy.ndarray
        :return: The transformed data.
        """
        non_na = x.dropna()
        if non_na.empty:
            raise ValueError("All elements are missing values")

        series_name = x.name if x.name is not None else 0

        mode = non_na.to_frame().groupby(series_name)[
            series_name].agg("count").idxmax()
        self._fill = mode

        return self

    def transform(self, x):
        """
        Transforms data x by adding the missing values with the most frequent categories.

        Must call fit() before calling transform()

        :param x: The data to transform.
        :type x: numpy.ndarray or pandas.series
        :return: The transformed data.
        """
        if self._fill is None:
            raise ValueError("CatImputer fit not called")

        mask = self._get_mask(x)
        if self._copy:
            x = x.copy()
        x[mask] = self._fill

        return x.values


class DateTimeFeaturesTransformer(BaseEstimator, TransformerMixin):
    """
    Expands datetime features from input into sub features like year, month, day,\
    day of the week, day of the year, quarter, week of the month, hour, minute and second.
    """

    def fit(self, x, y=None):
        """
        Fit function for date time transform.

        :param x: Input array.
        :type x: numpy.ndarray or pandas.series
        :param y: Target values.
        :type y: numpy.ndarray
        :return: Class object itself.
        """
        return self

    def transform(self, x):
        """
        Transforms data x.

        :param x: The data to transform.
        :type x: numpy.ndarray or pandas.series
        :return: The transformed data.
        """
        return self._datetime_feats(x)

    def _datetime_feats(self, x):
        """
        Gets the features for a datetime column.
        Expand the date time features from array of dates.

        :param x: Series that represents column.
        :type x: numpy.ndarray or pandas.series
        :return: Features for datetime column.
        """
        x = pd.to_datetime(pd.Series(x), infer_datetime_format=True,
                           box=False, errors="coerce").fillna(pd.Timestamp.min)
        return pd.concat([
            x.dt.year,
            x.dt.month,
            x.dt.day,
            x.dt.dayofweek,
            x.dt.dayofyear,
            x.dt.quarter,
            x.apply(lambda dt: (dt.day - 1) // 7 + 1),
            x.dt.hour,
            x.dt.minute,
            x.dt.second,
        ], axis=1).values


class HashOneHotVectorizerTransformer(BaseEstimator, TransformerMixin):
    """
    Convert input to hash and encode to one hot encoded vector.

    The input and output type is same for this transformer.

    :param hashing_seed_val: Seed value for hashing transform.
    :type hashing_seed_val: int
    :param num_cols: Number of columns to be generated.
    :type num_cols: int
    """

    def __init__(self, hashing_seed_val, num_cols=8096):
        """
        Initialize for hashing one hot encoder transform with a seed value and maximum number of expanded columns.

        :param hashing_seed_val: Seed value for hashing transform.
        :type hashing_seed_val: int
        :param num_cols: Number of columns to be generated.
        :type num_cols: int
        :return:
        """
        self._num_cols = num_cols
        self._seed = hashing_seed_val

    def fit(self, x, y=None):
        """
        Fit function for hashing one hot encoder transform.

        :param x: Input array.
        :type x: numpy.ndarray or pandas.series
        :param y: Target values.
        :type y: numpy.ndarray
        :return: Class object itself.
        """
        return self

    def _hash_cat_feats(self, x):
        """
        Hash transform and one-hot encode the input series or dataframe.

        :param x: Series that represents column.
        :type x: numpy.ndarray or pandas.series
        :return: Hash vector features for column.
        """
        row = []
        col = []
        data = []
        row_no = 0
        for val in x:
            hash_val = murmurhash3_32(val, self._seed) % self._num_cols
            row.append(row_no)
            row_no = row_no + 1
            col.append(hash_val)
            data.append(True)

        X = sparse.csr_matrix((data, (row, col)),
                              shape=(x.shape[0], self._num_cols),
                              dtype=np.bool_)
        X.sort_indices()
        return X

    def transform(self, x):
        """
        Transform function for hashing one hot encoder transform.

        :param x: Input array.
        :type x: numpy.ndarray or pandas.series
        :return: Result of hashing one hot encoder transform.
        """
        return self._hash_cat_feats(x)


class StringCastTransformer(BaseEstimator, TransformerMixin):
    """
    Cast input to string. The input and output type is same for this transformer.
    """

    def fit(self, x, y=None):
        """
        Fit function for string cast transform.

        :param x: Input array.
        :type x: numpy.ndarray
        :param y: Target values.
        :type y: numpy.ndarray
        :return: Class object itself.
        """
        return self

    def transform(self, x):
        """
        Transforms data x into array of strings.

        :param x: The data to transform.
        :type x: numpy.ndarray
        :return: The transformed data which is an array of strings.
        """
        return x.astype(str)


class LambdaTransformer(BaseEstimator, TransformerMixin):
    """
    Transforms column through a lambda function.

    :param func: The lambda function to use in the transformation.
    :type func: function
    """

    def __init__(self, func):
        """
        Constructor for LambdaTransformer

        :param func: The lambda function to use in the transformation.
        :type func: function
        :return:
        """
        self.func = func

    def fit(self, x, y=None):
        """
        Fit function for lambda transform.

        :param x: Input array.
        :type x: numpy.ndarray
        :param y: Target values.
        :type y: numpy.ndarray
        :return: Class object itself.
        """
        return self

    def transform(self, x):
        """
        Transform function for lambda transform which calls the lambda function over the input.

        :param x: Input array.
        :type x: numpy.ndarray
        :return: Result of lambda transform.
        """
        return self.func(x)


class LabelEncoderTransformer(BaseEstimator, TransformerMixin):
    """
    Transforms column through a label encoder to encode categories into numbers.

    :param hashing_seed_val: Seed value used for hashing if needed.
    :type hashing_seed_val: int
    """

    def __init__(self, hashing_seed_val):
        """
        Initialize for label encoding transform.

        :param hashing_seed_val: Seed value used for hashing if needed.
        :type hashing_seed_val: int
        :return:
        """
        self._label_encoder = LabelEncoder()
        self._hashing_seed_val = hashing_seed_val

    def fit(self, x, y=None):
        """
        Fit function for label encoding transform which learns the labels.

        :param x: Input array of integers or strings.
        :type x: numpy.ndarray
        :param y: Target values.
        :type y: numpy.ndarray
        :return: Class object itself.
        """
        # Keep track of the labels
        self._label_encoder.fit(x)
        return self

    def transform(self, x):
        """
        Transform function for label encoding transform to convert categorical data into integers.

        :param x: Input array of integers or strings.
        :type x: numpy.ndarray
        :return: Label encoded array of ints.
        """
        # Find the new classes in 'x'
        new_classes = np.unique(x)

        # Check if new classes are being label encoded
        if len(np.intersect1d(new_classes, self._label_encoder.classes_)) < len(new_classes):

            # Create a set of new classes that are detected
            new_classes = np.setdiff1d(new_classes, self._label_encoder.classes_)

            # Walk each entry in x and map the new classes to existing classes
            x_new_with_known_classes = []
            for entry in x:
                if entry in new_classes:
                    # Compute the hash for the entry and then map it to some
                    # existing class
                    entry = self._label_encoder.classes_[
                        (murmurhash3_32(entry, seed=self._hashing_seed_val)) % len(self._label_encoder.classes_)]

                x_new_with_known_classes.append(entry)

            # It is safe to run label encoder on all the existing classes
            return self._label_encoder.transform(x_new_with_known_classes)

        # Label encode x column
        return self._label_encoder.transform(x)


class FeatureTypeRecognizer:
    """
    Class for storing the feature types that the pre-processor recognizes.
    """

    Numeric = 'Numeric'
    DateTime = 'DateTime'
    Categorical = 'Categorical'
    CategoricalHash = 'CategoricalHash'
    Text = 'Text'
    Hashes = 'hashes'
    Ignore = 'Ignore'

    FULL_SET = {Numeric, DateTime, Categorical, Text, Hashes, Ignore}


class RawFeatureStats:
    """
    Class for computing feature stats from raw features.

    :param raw_column: Column having raw data.
    :type raw_column: numpy.ndarray
    """

    def __init__(self, raw_column):
        """
        Calculate stats for the input column.

        These stats are needed for deciding the data type of the column.

        :param raw_column: Column having raw data.
        :type raw_column: numpy.ndarray
        """
        # Number of unique values in the column
        self.num_unique_vals = raw_column.unique().shape[0]
        # Total number of values in the column
        self.total_number_vals = raw_column.shape[0]
        # Create a series having lengths of the entries in the column
        self.lengths = raw_column.apply(str).apply(len)
        # Calculate the number of lengths of the entries in the column
        self.num_unique_lens = self.lengths.unique().shape[0]
        # Get the column type
        self.column_type = _get_column_data_type_as_str(raw_column.values)
        # Average lengths of an entry in the column
        self.average_entry_length = 0
        # Average number of spaces in an entry in the column
        self.average_number_spaces = 0
        # Number of missing values in the column
        self.num_na = raw_column.isna().sum()

        for column_entry in raw_column:
            # if not np.isnan(column_entry):
            self.average_entry_length += len(str(column_entry))
            self.average_number_spaces += str(column_entry).count(' ')

        self.average_entry_length /= 1.0 * self.total_number_vals
        self.average_number_spaces /= 1.0 * self.total_number_vals

        self.cardinality_ratio = (1.0 * self.num_unique_vals) / self.total_number_vals


class DataTransformer(BaseEstimator, TransformerMixin):
    """
    Preprocessing class that can be added in pipeline for input.

    This class does the following:
    1. Numerical inputs treated as it is.
    2. For dates: year, month, day and hour are features
    3. For text, tfidf features
    4. Small number of unique values for a column that is not float become
        categoricals

    :param task: 'classification' or 'regression' depending on what kind of ML problem to solve.
    :type task: str or azureml.train.automl.constants.Tasks
    """

    def __init__(self, task=Tasks.CLASSIFICATION):
        """
        Initialize for data transformer for pre-processing raw user data.

        :param task: 'classification' or 'regression' depending on what kind of ML problem to solve.
        :type task: str or azureml.train.automl.constants.Tasks
        """
        if task != Tasks.CLASSIFICATION and task != Tasks.REGRESSION:
            raise ValueError("Unknown task")

        self._task_type = task
        self.mapper = None

        self.date_regex1 = re.compile(r'(\d+/\d+/\d+)')
        self.date_regex2 = re.compile(r'(\d+-\d+-\d+)')

        # ratio of unique values to total values to be considered categoricals
        self._min_ratio_uniq_cats = 0.05
        # max number of unique values to be considered cats
        self._max_num_cats = 200
        # max number of unique values to be considered categorical hash
        self._max_num_cat_hash = 10000
        # max number of unique values to be considered cats for integer
        self._max_num_cats_int = 50
        # ratio of unique values to total values to be considered hashes
        self._min_ratio_hashes = 0.9
        # number of maxrows allowed for tfidf computation since tfidf
        # vectorizer is expensive
        self._maxrows_for_tfidf = 1e5
        # max number of unique lengths in a column to be considered hash
        self._max_uniqhashlens = 3
        # min number of rows for hashes to be present
        self._min_num_hashrows = 200
        # max size in characters for ngram
        self._max_ngram = 3
        # Hashing seed value for murmurhash
        self._hashing_seed_value = 314489979
        # External logger if None, then no logs
        self.logger = None

    def fit_transform_with_logger(self, X, y=None, logger=None, **fit_params):
        """
        Wrapper function around the fit_transform function for the Data transformer class.

        :param X: Dataframe representing text, numerical or categorical input.
        :type X:numpy.ndarray or pandas.DataFrame
        :param y: To match fit signature.
        :type y: numpy.ndarray or pandas.DataFrame
        :param fit_params: Additional parameters for fit_transform().
        :param logger: External logger handler.
        :type logger: logging.Logger
        :return: Transformed data.
        """
        # Init the logger
        self._init_logger(logger)
        # Call the fit and transform function
        X_new = self.fit_transform(X, y, **fit_params)
        # Release the logger
        self._release_logger()
        return X_new

    def fit(self, df, y=None):
        """
        Perform the raw data validation and identify the transformations to apply.

        :param df: Dataframe representing text, numerical or categorical input.
        :type df: numpy.ndarray or pandas.DataFrame
        :param y: To match fit signature.
        :type y: numpy.ndarray or pandas.DataFrame
        :return: DataTransform object.
        :raises: Value Error for non-dataframe and empty dataframes.
        """
        self._check_input(df)
        if isinstance(df, np.ndarray):
            df = pd.DataFrame(df)
        self.mapper = DataFrameMapper(
            self._get_transforms(df), input_df=True, sparse=True)
        self.mapper.fit(df, y)

        return self

    def transform(self, df):
        """
        Transform the input raw data with the transformations idetified in fit stage.

        :param df: Dataframe representing text, numerical or categorical input.
        :type df: numpy.ndarray or pandas.DataFrame
        :return: Numpy array.
        """
        if not self.mapper:
            raise Exception("fit not called")

        self._check_input(df)

        if isinstance(df, np.ndarray):
            df = pd.DataFrame(df)

        return self.mapper.transform(df)

    def _get_transforms(self, df):
        """
        Identify the transformations for all the columns in the dataframe.

        :param df: Input dataframe.
        :type df: numpy.ndarray or pandas.DataFrame
        :return: Transformations that go into datamapper.
        """
        transforms = []

        # drop columns that have only missing data
        df = df.dropna(axis=1, how="all")

        self._logger_wrapper('info', "Start getting transformers.")
        for dtype, column in zip(df.dtypes, df.columns):

            raw_stats, feature_type_detected = self._detect_feature_type(
                column,
                df)

            self._logger_wrapper(
                'info',
                "Preprocess transformer for col {}, datatype: {}, detected datatype {}".format(
                    df.columns.get_loc(column),
                    str(dtype),
                    str(feature_type_detected)
                )
            )

            if feature_type_detected == FeatureTypeRecognizer.Numeric:

                # floats or ints go as they are, we only fix NaN
                transforms.append(
                    ([column], [Imputer()], {"alias": str(column)}))
                # if there are lot of imputed values, add an imputation marker
                if raw_stats.num_na > 0.01 * raw_stats.total_number_vals:
                    transforms.append(
                        ([column], [ImputationMarker()], {"alias": "{}_imputemarker".format(str(column))}))

            elif feature_type_detected == FeatureTypeRecognizer.DateTime:
                transforms.append(
                    (column, [CatImputer(), StringCastTransformer(),
                              DateTimeFeaturesTransformer()], {"alias": str(column)}))
            elif feature_type_detected == FeatureTypeRecognizer.CategoricalHash:
                bits = pow(2, int(math.log(raw_stats.num_unique_vals, 2)) + 1)
                transforms.append((column,
                                   [
                                       StringCastTransformer(),
                                       HashOneHotVectorizerTransformer(hashing_seed_val=self._hashing_seed_value,
                                                                       num_cols=int(bits))
                                   ],
                                   {"alias": str(column)}))
            elif feature_type_detected == FeatureTypeRecognizer.Categorical:
                # use categorical
                if raw_stats.num_unique_vals <= 2:
                    # Use label encoder
                    transforms.append((column,
                                       [
                                           CatImputer(),
                                           StringCastTransformer(),
                                           LabelEncoderTransformer(hashing_seed_val=self._hashing_seed_value)
                                       ],
                                       {"alias": str(column)}))
                else:
                    # use CountVectorizer for both Hash and CategoricalHash for now
                    transforms.append((column,
                                       [
                                           StringCastTransformer(),
                                           CountVectorizer(
                                               tokenizer=self._wrap_in_lst,
                                               binary=True)
                                       ],
                                       {"alias": str(column)}))
            elif feature_type_detected == FeatureTypeRecognizer.Text:
                transforms.extend(
                    self._get_string_transforms(
                        column, self._get_ngram_len(raw_stats.lengths)))
            else:
                # skip if hashes or ignore case
                self._logger_wrapper(
                    'info',
                    "Hashes or single value column detected. No transforms needed")
                continue

        if not transforms:
            # can happen when we get all hashes
            self._logger_wrapper('warning', "No features could be identified or generated")
            raise ValueError("No features could be identified or generated")

        # Log the transformations done for raw data into the logs
        self._logger_wrapper('info', self._get_transformations_str(df, transforms))

        self._logger_wrapper('info', "End getting transformers.")

        return transforms

    def _detect_feature_type(self, column, df):
        """
        Calculate the stats on the raw column and decide the data type of the input column.

        :param column: Column name in the data frame.
        :param df: Input dataframe.
        :return: Raw column stats, Type of feature.
        """
        raw_stats = RawFeatureStats(df[column])

        if raw_stats.num_unique_vals == 1:
            # If there is only one unique value, then we don't need to include
            # this column for transformations
            feature_type_detected = FeatureTypeRecognizer.Ignore
        elif raw_stats.num_unique_vals >= min(
                self._max_num_cats, self._min_ratio_uniq_cats * raw_stats.total_number_vals):
            # If number of unique values is higher than a ratio of input data
            if _check_if_column_data_type_is_numerical(
                    raw_stats.column_type):
                feature_type_detected = FeatureTypeRecognizer.Numeric
            else:
                non_na = df[column].dropna()
                num_dates = np.sum(non_na.apply(str).apply(self._is_date))
                # Detect DateTime features
                if num_dates == non_na.shape[0] and non_na.shape[0] > 0:
                    feature_type_detected = FeatureTypeRecognizer.DateTime
                elif raw_stats.cardinality_ratio > 0.85 and \
                        raw_stats.average_number_spaces > 1.0:
                    feature_type_detected = FeatureTypeRecognizer.Text
                elif raw_stats.cardinality_ratio < 0.7 and \
                        raw_stats.num_unique_vals < self._max_num_cat_hash:
                    feature_type_detected = FeatureTypeRecognizer.CategoricalHash
                elif raw_stats.average_number_spaces > 1.0:
                    feature_type_detected = FeatureTypeRecognizer.Text
                elif raw_stats.cardinality_ratio > 0.9:
                    feature_type_detected = FeatureTypeRecognizer.Hashes
                else:
                    feature_type_detected = FeatureTypeRecognizer.Ignore
        else:
            if _check_if_column_data_type_is_int(
                    raw_stats.column_type):
                if raw_stats.num_unique_vals <= min(
                        self._max_num_cats_int, self._min_ratio_uniq_cats * raw_stats.total_number_vals):
                    feature_type_detected = FeatureTypeRecognizer.Categorical
                else:
                    feature_type_detected = FeatureTypeRecognizer.Numeric
            elif _check_if_column_data_type_is_numerical(
                    raw_stats.column_type):
                feature_type_detected = FeatureTypeRecognizer.Numeric
            else:
                feature_type_detected = FeatureTypeRecognizer.Categorical
        return raw_stats, feature_type_detected

    def _get_ngram_len(self, lens_series):
        """
        Get N-grams length required for text transforms.

        :param lens_series: Series of lengths for a string.
        :return: The ngram to use.
        """
        lens_series = lens_series.apply(lambda x: min(x, self._max_ngram))
        return lens_series.mode()[0]

    def _is_date(self, input):
        """
        Check if a given string is a date.

        Needs regex to make sure the dateutil doesn't allow integers
        interpreted as epochs.

        :param input: String.
        :return: True/False.
        """
        if (self.date_regex1.search(input) is None and
                self.date_regex2.search(input) is None):
            return False

        try:
            dateutil.parser.parse(input)
            return True
        except ValueError:
            return False

    def _check_input(self, df):
        """
        Check inputs for transformations.

        :param df: Input dataframe.
        :return:
        """
        # Raise an exception if the input is not a data frame or array
        if not isinstance(df, pd.DataFrame) and not isinstance(df, np.ndarray):
            raise ValueError("df should be a pandas dataframe or numpy array")

    def _get_string_transforms(self, column, ngram_len):
        """
        Create a list of transforms for text data.

        :param column: Column name.
        :param ngram_len: Continous length of characters or number of words.
        :return: String transformations to use in a list.
        """
        ngram_len = min(self._max_ngram, ngram_len)
        tr = [(column,
               [
                   StringCastTransformer(),
                   TfidfVectorizer(use_idf=False, norm='l2', max_df=0.95,
                                   analyzer="char", ngram_range=(1, ngram_len))
               ],
               {
                   "alias": "{}_chartrigram".format(column)
               }
               ),
              (column,
               [
                   StringCastTransformer(),
                   TfidfVectorizer(use_idf=False, norm='l2',
                                   analyzer="word", ngram_range=(1, 2))
               ],
               {
                   "alias": "{}_wordbigram".format(column)
               }
               )]

        if self._task_type == Tasks.CLASSIFICATION:
            tr.append((column,
                       [
                           CatImputer(),
                           StringCastTransformer(),
                           CountVectorizer(analyzer="word",
                                           ngram_range=(1, 1)),
                           NaiveBayes()
                       ],
                       {
                           "alias": "{}_wordbigram_nb".format(column)
                       }))

        return tr

    def _wrap_in_lst(self, x):
        """
        Wrap an element in list.

        :param x: Element like string or integer.
        """
        return [x]

    def _init_logger(self, logger):
        """
        Init the logger and also enable external logs.

        :param logger: Logger handle to log messages into the log file
        :type logger: logging.Logger
        :return:
        """
        self.logger = logger

    def _release_logger(self):
        """
        Release the logger(set to None) object so that pickle can serialize the data transformer.

        :return:
        """
        self.logger = None

    def _logger_wrapper(self, level, message):
        """
        Log a message with a given debug level in a log file.

        :param logger: the logger handle
        :type logger: logging.Logger
        :param level: log level (info or debug)
        :param message: log message
        :type message: str
        """
        # Check if the logger object is valid. If so, log the message otherwise pass
        if self.logger:
            if level == 'info':
                self.logger.info(message)
            elif level == 'warning':
                self.logger.warning(message)

    def _get_transformations_str(self, df, transforms):
        """
        Get the data transformations recorded for raw columns as strings.

        :param df: Input dataframe.
        :type df:numpy.ndarray or pandas.DataFrame or sparse matrix
        :param transforms: List of applied transformations for various raw columns as a string.
        :type transforms: List
        """
        transformation_str = "Transforms:\n"
        list_of_transforms_as_list = []

        # Walk all columns in the input dataframe
        for column in df.columns:

            # Get all the indexes of transformations for the current column
            column_matches_transforms = \
                [i for i in range(0, len(transforms)) if transforms[i][0] == column]

            # If no matches for column name is found, then look for list having
            # this column name
            if len(column_matches_transforms) == 0:
                column_matches_transforms = \
                    [i for i in range(0, len(transforms)) if transforms[i][0] == [column]]

            # Walk all the transformations found for the current column and add
            # to a string
            for transform_index in column_matches_transforms:
                some_str = 'col {}, transformers: {}'.format(
                    df.columns.get_loc(column),
                    '\t'.join([tf.__class__.__name__ for tf in transforms[transform_index][1]]))
                list_of_transforms_as_list.append(some_str)

        transformation_str += '\n'.join(list_of_transforms_as_list)

        # Return the string representation of all the transformations
        return transformation_str


class LaggingTransformer(BaseEstimator, TransformerMixin):
    """
    Transforms the input data by appending previous rows.

    :param lag_length: Lagging length.
    :type lag_length: int
    """

    def __init__(self, lag_length):
        """
        Initialize for lagging transform with lagging length.

        :param lag_length: Lagging length.
        :type lag_length: int
        :return:
        """
        self._lag_length = lag_length
        self._missing_fill = 0

    def fit(self, x, y=None):
        """
        Fit function for lagging transform.

        :param x: Input dataframe or sparse matrix.
        :type x: numpy.ndarray or pandas.DataFrame or sparse matrix
        :param y: Target values.
        :type y: numpy.ndarray or pandas.DataFrame
        :return: Class object itself.
        """
        return self

    def transform(self, x):
        """
        Transform function for lagging transform. The function appends columns with previous seen rows \
        to the input dataframe or sparse matrix depending on the specified lagging length.

        :param x: Input dataframe or sparse matrix.
        :type x: numpy.ndarray or pandas.DataFrame or sparse matrix
        :return: Result of lagging transform.
        """
        x_is_sparse = sparse.issparse(x)

        if not isinstance(x, pd.DataFrame) and not isinstance(x, np.ndarray) and not x_is_sparse:
            raise ValueError(
                "x should be dataframe or numpy array or scipy sparse matrix")

        if x.shape[0] < self._lag_length:
            raise ValueError(
                "Input needs to have at least {0} rows".format(self._lag_length))

        if isinstance(x, np.ndarray):
            df = pd.DataFrame(x)
        elif x_is_sparse:
            # SparseDataFrame throws error with to_coo if dtype is int
            df = pd.SparseDataFrame(x.astype(float))
        else:
            df = x

        df_lag = df
        for i in range(1, self._lag_length + 1):
            df_lag = pd.concat([df_lag, df.shift(i)], axis=1)

        df_lag.columns = range(len(df_lag.columns))
        return df_lag.to_coo().tocsr() if x_is_sparse else df_lag.fillna(self._missing_fill).values
