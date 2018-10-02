import functools
import random
import re

import pandas as pd

from eqi_utils.data import utils

pd.DataFrame.to_eqi = lambda self: EQIDF(self)

_NOT_IMPLEMENTED_MSG = 'Opps, ' \
                       'not implemented yet. Stay tuned for future releases'

_SEED = random.randrange(50)


class EQIDF:
    """
        EQI DataFrame, an extended Pandas DataFrame.

        - Pandas Compatible:
            - You can use Pandas DataFrame methods on EQIDF
        - Reduce LOC with convention over configuration:
            - index and columns should have distinct names of string type
        - Easy-to-use extension methods (e_*() methods):
            - No more axis, nor distinction between column or index. \
            Simply use the unique name instead
            - Warning: not 1000% Pythonic! But sorry, we are not religious.
        - Streamlined DataFrame transformation pipline in builder pattern:
            - No explicit intermediate variable assignments
        - Draft mode:
            - Save time when drafting your transformation pipeline by \
            taking a small percentage of the whole data
        - Sensible debug utilities (show_*() methods)
            - Everybody makes mistakes, these methods help you finish your
                transformation pipeline faster.

        TODO: Integrate with Spark DF and Dask DF
    """

    def __init__(self, delegate, copy=True):
        """
        PLEASE DO NOT USE THE CONSTRUCTORS DIRECTLY
        USE THE STATIC from_*(df) CONSTRUCTORS INSTEAD.
        :param delegate:
        :param copy:
        """
        if copy:
            self.dlg = delegate.copy()
        else:
            self.dlg = delegate

    @staticmethod
    def from_pandas(df):
        """
        Create a EQIDF from Pandas DataFrame
        :param df:
        :return:
        """
        return EQIDF(df)

    @staticmethod
    def from_spark(df):
        raise NotImplementedError(_NOT_IMPLEMENTED_MSG)

    @staticmethod
    def from_dask(df):
        raise NotImplementedError(_NOT_IMPLEMENTED_MSG)

    def __getattribute__(self, attr):
        try:
            # If this is an EQIDF attribute, return it directly
            attr_ret = object.__getattribute__(self, attr)
        except AttributeError:
            # Not an EQIDF attribute, get from the delegate
            attr_ret = getattr(self.dlg, attr)
            if hasattr(attr_ret, "__call__"):
                # If it is a callable, wrap it up to return proper values
                return _MethodWrapper(self, attr_ret)
        return attr_ret

    def _delegate_func_by(self, func_name):
        return getattr(self.dlg, func_name)

    def is_name_index(self, name):
        return name in self.dlg.index.names

    def _has_default_index(self):
        return isinstance(self.dlg.index,
                          pd.Int64Index) and self.dlg.index.names == [None]

    def e_reset_index(self, keep_default_index=False):
        """
        Reset dataframe indexes
        :param keep_default_index: whether to keep the default int64 index
        :return: the same caller EQIDF instance
        """
        if self._has_default_index():
            if keep_default_index:
                self.dlg.reset_index(inplace=True)
            else:
                self.dlg.reset_index(drop=True, inplace=True)
        else:
            self.dlg.reset_index(inplace=True)
        return self

    def e_set_index(self, *names, keep_default_index=False, **kwargs):
        """
        Set dataframe index, names with 'date' or 'timestamp' as suffix will be
        automatically turned into DatetimeIndex.
        :param names: Column or existing index names
        :param keep_default_index: whether to keep the default int64 index
        :param kwargs: Additional kwargs for DatetimeIndex if any
        :return: the same caller EQIDF instance
        """
        if not names:
            self.e_reset_index(keep_default_index)
            return self
        col_names, index_names = self._into_col_index(names)
        if index_names:
            self.e_reset_index(keep_default_index)
        index = [
            pd.DatetimeIndex(self._get_value(c), **kwargs) if _is_date_column(
                c) else c
            for
            c in names]
        date_cols = [c for c in names if _is_date_column(c)]
        if date_cols:
            self.e_drop(*date_cols)
        self.dlg.set_index(index, inplace=True)
        return self

    def _get_column(self, column):
        return self.dlg[column]

    def _get_index(self, index):
        return self.dlg.index.get_level_values(index)

    def _get_value(self, name):
        if self.is_name_index(name):
            return self._get_index(name)
        else:
            return self._get_column(name)

    def e_notnull(self, *names):
        """
        Select rows that has non-null values on names (either column or index)
        :param names: Column or index names
        :return: the same caller EQIDF instance
        """
        if not names:
            return self
        condition = None
        for name in names:
            if condition is None:
                condition = self._get_value(name).notnull()
            else:
                condition &= self._get_value(name).notnull()
        self.dlg = self.dlg.loc[condition]
        return self

    def e_show(self):
        """
        Print dataframe
        :return: the same caller EQIDF instance
        """
        utils.full_print(self.dlg)
        return self

    def e_showstop(self):
        """
        Print dataframe and terminate program execution by raising an exception
        :return: the same caller EQIDF instance
        """
        utils.full_print(self.dlg)
        raise KeyboardInterrupt

    def e_in(self, name, value_set):
        """
        Select rows with value of name (either column or index) in a value set
        :param name: column or index name
        :param value_set: iterable, Series, DataFrame or dictionary
        :return: the same caller EQIDF instance
        """
        self.dlg = self.dlg.loc[self._get_value(name).isin(value_set)]
        return self

    def e_is(self, name, value):
        """
        Select rows with value of name (either column or index) equals to\
        a given target value
        :param name: column or index name
        :param value: target value to check equality against
        :return: the same caller EQIDF instance
        """
        self.dlg = self.dlg.loc[self._get_value(name) == value]
        return self

    def e_between(self, name, start=None, end=None):
        """
        Select rows with value of name (either column or index) is between \
            a range (inclusive)
        :param name: column or index name
        :param start: start value, can be None
        :param end: end value, can be None
        :return: the same caller EQIDF instance
        """
        start_cond = self._get_value(name) >= start if start else None
        end_cond = self._get_value(name) <= end if end else None
        if start and end:
            self.dlg = self.dlg.loc[start_cond & end_cond]
        elif start:
            self.dlg = self.dlg.loc[start_cond]
        elif end:
            self.dlg = self.dlg.loc[end_cond]
        return self

    def e_greater_than(self, name, value):
        """
        Select rows with value of name (either column or index) greater than \
            a target value
        :param name: column or index name
        :param value: target value
        :return: the same caller EQIDF instance
        """
        gt_cond = self._get_value(name) > value
        self.dlg = self.dlg.loc[gt_cond]
        return self

    def e_less_than(self, name, value):
        """
        Select rows with value of name (either column or index) smaller than \
            a target value
        :param name: column or index name
        :param value: target value
        :return: the same caller EQIDF instance
        """
        lt_cond = self._get_value(name) < value
        self.dlg = self.dlg.loc[lt_cond]
        return self

    def e_select(self, *columns):
        """
        Select columns
        :param columns: column names
        :return: the same caller EQIDF instance
        """
        self.dlg = self.dlg[list(columns)]
        return self

    def e_groupby(self, *names):
        """
        Group by names (either column or index names)
        :param names: column or index names
        :return: the same caller EQIDF instance
        """
        col_names, index_names = self._into_col_index(names)
        if col_names:
            self.e_set_index(*names)
        self.dlg = self.dlg.groupby(level=names)
        return self

    def e_apply(self, func):
        """
        Apply func
        :param func: function to apply
        :return: the same caller EQIDF instance
        """
        self.dlg = self.dlg.apply(func)
        return self

    def to_pandas(self):
        """
        To Pandas DataFrame
        :return: Pandas DataFrame
        """
        return self.dlg

    def e_rename(self, rename_map):
        """
        Rename columns or indexes
        :param rename_map: name (column or index) to new name map
        :return: the same caller EQIDF instance
        """
        new_index = self.dlg.index.names
        column_rename = {}
        for k, v in rename_map.items():
            if self.is_name_index(k):
                new_index = [v if k == x else x for x in new_index]
            else:
                column_rename[k] = v
        self.dlg.index.names = new_index
        self.dlg = self.dlg.rename(columns=column_rename)
        return self

    def e_skip(self, skiprows):
        """
        Skip rows
        :param skiprows: number of rows to skip from the beginning
        :return: the same caller EQIDF instance
        """
        self.dlg = self.dlg[skiprows:]
        return self

    def e_index_names(self):
        """
        Return the index names list
        :return: index names list
        """
        return self.dlg.index.names

    def __str__(self):
        return str(self.to_pandas())

    def e_limit(self, num):
        """
        Return the first total number of rows
        :param num: total numbers of rows to return from the beginning
        :return: the same caller EQIDF instance
        """
        self.dlg = self.dlg[:num]
        return self

    def e_call(self, func_name, *args, **kwargs):
        return self._delegate_func_by(func_name)(self.to_pandas(), *args,
                                                 **kwargs)

    def e_normalize_by(self, other):
        """
        Normalize by another DataFrame, assuming:
        1. the two dataframes share the same index
        2. each of the two dataframes only has one column
        :param other: Another dataframe
        :return: the same caller EQIDF instance
        """
        merged_df = self.dlg.merge(other, how='left', left_index=True,
                                   right_index=True)
        self.dlg = pd.DataFrame(
            merged_df.iloc[:, 0].divide(merged_df.iloc[:, 1]))
        return self

    def e_show_len(self):
        """
        Print the length of this EQIDF, mostly for debug purpose
        :return: the same caller EQIDF instance
        """
        print(len(self.dlg))
        return self

    def e_show_describe(self):
        """
        Print the description of this EQIDF, mostly for debug purpose
        :return: the same caller EQIDF instance
        """
        utils.full_print(self.dlg.describe())
        return self

    def e_show_info(self):
        """
        Print the info of this EQIDF, mostly for debug purpose
        :return: the same caller EQIDF instance
        """
        print(self.dlg.info())
        return self

    def e_show_type(self):
        """
        Print the type of this EQIDF, mostly for debug purpose
        :return: the same caller EQIDF instance
        """
        print(type(self.dlg))
        return self

    def e_print_dup_index(self, first_only=True):
        """
        Print the duplicate index values
        :param first_only: print only the first duplicated index
        :return: the same caller EQIDF instance
        """
        dup_arr = self.dlg.index.duplicated()
        for i, v in enumerate(dup_arr):
            if v:
                print(self.dlg.index[i])
                if first_only:
                    return self
        return self

    def e_has_dup_index(self):
        """
        Returns if the EQIDF has duplicated index
        :return: boolean, if the EQIDF has duplicated index
        """
        return self.dlg.index.duplicated().any()

    def e_set(self, from_name, to_name, func):
        """
        Add a new column from an existing column by applying func
        :param from_name: from column name
        :param to_name: to column name
        :param func: transformation func
        :return: the same caller EQIDF instance
        """
        self.dlg[to_name] = self.dlg[from_name].apply(func)
        return self

    def e_select_series(self, column):
        """
        Select column as a series
        :param column: column name
        :return: series with the input column name
        """
        return self.dlg[column]

    def e_drop_dup_index(self):
        """
        Drop duplicated index, keep the first row for rows sharing a same
        duplicated index value
        :return: the same caller EQIDF instance
        """
        self.dlg = self.dlg[~self.dlg.index.duplicated(keep='first')]
        return self

    def e_drop_level(self, *names):
        """
        Drop levels, only for Multiindex dataframes, for single index ones \
        use e_drop instead
        :param names: column or index names
        :return: the same caller EQIDF instance
        """
        if not names:
            return self
        col_names, index_names = self._into_col_index(names)
        if col_names:
            self.dlg.columns = self.dlg.columns.droplevel(col_names)
        if index_names:
            self.dlg.index = self.dlg.index.droplevel(index_names)
        return self

    def _into_col_index(self, names):
        col_names = [name for name in names if not self.is_name_index(name)]
        index_names = [name for name in names if self.is_name_index(name)]
        return col_names, index_names

    @staticmethod
    def e_pass():
        """
        Returns an identity function, t -> t
        :return: identity function
        """
        return lambda df: df

    def e_drop(self, *names):
        """
        Drops columns or indexes
        :param names: Column or index names
        :return: the same caller EQIDF instance
        """
        col_names, index_names = self._into_col_index(names)
        if col_names:
            self.dlg.drop(col_names, axis=1, inplace=True)
        if index_names:
            index = self.dlg.index
            if isinstance(index, pd.MultiIndex):
                self.dlg.index = self.dlg.index.droplevel(index_names)
            else:
                self.e_reset_index()
                self.dlg.drop(index_names, axis=1, inplace=True)
        return self

    def e_copy(self):
        """
        Make a new copy of the wrapped dataframe
        :return: the same caller EQIDF instance
        """
        self.dlg = self.dlg.copy()
        return self

    def e_unique(self, name):
        """
        Returns unique values of a column or index
        :param name: column or index name
        :return: the same caller EQIDF instance
        """
        self.dlg = pd.unique(self._get_value(name))
        return self

    def e_count(self):
        """
        Returns the length of the underlying dataframe
        :return: the length of the underlying dataframe
        """
        return len(self.dlg)

    def e_where(self, name, func):
        """
        Select rows with func(value_of_name) == True
        :param name: column or index name
        :param func: condition function which returns boolean
        :return: the same caller EQIDF instance
        """
        self.dlg = self.dlg[self._get_value(name).apply(func)]
        return self

    def e_first_col(self):
        """
        Select the first column
        :return: the same caller EQIDF instance
        """
        self.dlg = self.dlg.iloc[:, 0]
        return self

    def _is_multiindex(self):
        return isinstance(self.dlg.index, pd.MultiIndex)

    def e_astype(self, type_map):
        """
        Change columns or indexes to have specific types
        :param type_map: a map of name -> type, name can be column or\
            index names
        :return: the same caller EQIDF instance
        """
        col_names, index_names = self._into_col_index(list(type_map.keys()))
        if col_names:
            for c in col_names:
                self.dlg[c] = self.dlg[c].astype(type_map[c])
        if index_names:
            if self._is_multiindex():
                for i in index_names:
                    self.dlg.index.set_levels(
                        self.dlg.index.get_level_values(i).astype(
                            type_map[i]), level=i, inplace=True)
            else:
                for i in index_names:
                    self.dlg.index = self.dlg.index.get_level_values(i).astype(
                        type_map[i])
        return self

    def e_fillna(self, na_map):
        """
        Fill na value for one or more columns
        :param na_map: a map of column name -> value to replace na
        :return: the same caller EQIDF instance
        """
        for k, v in na_map.items():
            self.dlg[k] = self.dlg[k].fillna(v)
        return self

    def e_dropna(self, *columns):
        """
        Drop na values for one or more columns
        :param columns: column names
        :return: the same caller EQIDF instance
        """
        self.dlg.dropna(subset=columns, inplace=True)
        return self

    def e_to_factor(self, asset_column, date_column, value_column):
        """
        Transform into an EQI Factor format, i.e. a dataframe \
            with Multiindex ['date', 'asset'] and one single value column
        :param asset_column: asset column name
        :param date_column: date column name
        :param value_column: value column name
        :return: Pandas dataframe in EQI factor format
        """
        return (self.dlg.to_eqi()
                .e_select(asset_column, date_column, value_column)
                .e_rename({asset_column: 'asset', date_column: 'date'})
                .e_notnull(value_column)
                .e_set_index('date', 'asset')
                .sort_index()
                .to_pandas()
                )

    def e_to_set(self, name):
        """
        Return values of a column or index as a set
        :param name: column or index name
        :return: value set
        """
        return set(pd.unique(self._get_value(name)))

    def e_to_dict(self, name=None):
        """
        Return index -> values of a column as a dict
        :param name: column name
        :return: index -> values dict
        """
        if not name:
            return self.dlg.iloc[:, 0].to_dict()
        else:
            return self.dlg[name].to_dict()

    def e_draft(self, force=False):
        """
        Turn into draft mode by processing only a partial randomly sampled data
        :return: the same caller EQIDF instance
        """
        if len(self.dlg) < 5000 and not force:
            return self
        else:
            self.dlg = self.dlg.sample(frac=0.1, random_state=_SEED)
            return self


class _MethodWrapper:
    """
    Wrapper for Pandas Methods to make them accessible by EQIDF
    """

    def __init__(self, parent, callable_):
        self.parent = parent
        self.callable_ = callable_
        self.__name__ = 'wrapper({})'.format(callable_.__name__)

    def __call__(self, *args, **kwargs):
        ret = self.callable_(*args, **kwargs)
        if isinstance(ret, pd.DataFrame):
            self.parent.dlg = ret
            return self.parent
        elif isinstance(ret, pd.Series):
            self.parent.dlg = pd.DataFrame(ret)
            return self.parent
        elif hasattr(ret, '__module__') and "pandas." in ret.__module__:
            self.parent.dlg = ret
            return self.parent
        else:
            return ret


def wrap(func):
    @functools.wraps(func)
    def wrapped_func(df, *args, **kwargs):
        return func(EQIDF(df), *args, **kwargs)

    return wrapped_func


def _is_date_column(name):
    return re.match(".*(date|timestamp)$", name.lower())
