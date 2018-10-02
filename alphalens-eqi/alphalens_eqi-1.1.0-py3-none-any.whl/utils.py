#
# Copyright 2018 Quantopian, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pandas as pd
import numpy as np
import re
import warnings

from IPython.display import display
from pandas.tseries.offsets import CustomBusinessDay


class NonMatchingTimezoneError(Exception):
    pass


class MaxLossExceededError(Exception):
    pass


def rethrow(exception, additional_message):
    """
    Re-raise the last exception that was active in the current scope
    without losing the stacktrace but adding an additional message.
    This is hacky because it has to be compatible with both python 2/3
    """
    e = exception
    m = additional_message
    if not e.args:
        e.args = (m,)
    else:
        e.args = (e.args[0] + m,) + e.args[1:]
    raise e


def non_unique_bin_edges_error(func):
    """
    Give user a more informative error in case it is not possible
    to properly calculate quantiles on the input dataframe (factor)
    """
    message = """

    An error occurred while computing bins/quantiles on the input provided.
    This usually happens when the input contains too many identical
    values and they span more than one quantile. The quantiles are choosen
    to have the same number of records each, but the same value cannot span
    multiple quantiles. Possible workarounds are:
    1 - Decrease the number of quantiles
    2 - Specify a custom quantiles range, e.g. [0, .50, .75, 1.] to get unequal
        number of records per quantile
    3 - Use 'bins' option instead of 'quantiles', 'bins' chooses the
        buckets to be evenly spaced according to the values themselves, while
        'quantiles' forces the buckets to have the same number of records.
    4 - for factors with discrete values use the 'bins' option with custom
        ranges and create a range for each discrete value
    Please see utils.get_clean_factor_and_forward_returns documentation for
    full documentation of 'bins' and 'quantiles' options.

"""

    def dec(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            if 'Bin edges must be unique' in str(e):
                rethrow(e, message)
            raise

    return dec


@non_unique_bin_edges_error
def quantize_factor(factor_data,
                    quantiles=5,
                    bins=None,
                    by_group=False,
                    no_raise=False,
                    zero_aware=False):
    """
    Computes period wise factor quantiles.

    Parameters
    ----------
    factor_data : pd.DataFrame - MultiIndex
        A MultiIndex DataFrame indexed by date (level 0) and asset (level 1),
        containing the values for a single alpha factor, forward returns for
        each period, the factor quantile/bin that factor value belongs to, and
        (optionally) the group the asset belongs to.

        - See full explanation in utils.get_clean_factor_and_forward_returns

    quantiles : int or sequence[float]
        Number of equal-sized quantile buckets to use in factor bucketing.
        Alternately sequence of quantiles, allowing non-equal-sized buckets
        e.g. [0, .10, .5, .90, 1.] or [.05, .5, .95]
        Only one of 'quantiles' or 'bins' can be not-None
    bins : int or sequence[float]
        Number of equal-width (valuewise) bins to use in factor bucketing.
        Alternately sequence of bin edges allowing for non-uniform bin width
        e.g. [-4, -2, -0.5, 0, 10]
        Only one of 'quantiles' or 'bins' can be not-None
    by_group : bool, optional
        If True, compute quantile buckets separately for each group.
    no_raise: bool, optional
        If True, no exceptions are thrown and the values for which the
        exception would have been thrown are set to np.NaN
    zero_aware : bool, optional
        If True, compute quantile buckets separately for positive and negative
        signal values. This is useful if your signal is centered and zero is
        the separation between long and short signals, respectively.

    Returns
    -------
    factor_quantile : pd.Series
        Factor quantiles indexed by date and asset.
    """
    if not ((quantiles is not None and bins is None) or
            (quantiles is None and bins is not None)):
        raise ValueError('Either quantiles or bins should be provided')

    if zero_aware and not (isinstance(quantiles, int)
                           or isinstance(bins, int)):
        msg = ("zero_aware should only be True when quantiles or bins is an"
               " integer")
        raise ValueError(msg)

    def quantile_calc(x, _quantiles, _bins, _zero_aware, _no_raise):
        try:
            if _quantiles is not None and _bins is None and not _zero_aware:
                return pd.qcut(x, _quantiles, labels=False) + 1
            elif _quantiles is not None and _bins is None and _zero_aware:
                pos_quantiles = pd.qcut(x[x >= 0], _quantiles // 2,
                                        labels=False) + _quantiles // 2 + 1
                neg_quantiles = pd.qcut(x[x < 0], _quantiles // 2,
                                        labels=False) + 1
                return pd.concat([pos_quantiles, neg_quantiles]).sort_index()
            elif _bins is not None and _quantiles is None and not _zero_aware:
                return pd.cut(x, _bins, labels=False) + 1
            elif _bins is not None and _quantiles is None and _zero_aware:
                pos_bins = pd.cut(x[x >= 0], _bins // 2,
                                  labels=False) + _bins // 2 + 1
                neg_bins = pd.cut(x[x < 0], _bins // 2,
                                  labels=False) + 1
                return pd.concat([pos_bins, neg_bins]).sort_index()
        except Exception as e:
            if _no_raise:
                return pd.Series(index=x.index)
            raise e

    grouper = [factor_data.index.get_level_values('date')]
    if by_group:
        grouper.append('group')

    factor_quantile = factor_data.groupby(grouper)['factor'] \
        .apply(quantile_calc, quantiles, bins, zero_aware, no_raise)
    factor_quantile.name = 'factor_quantile'

    return factor_quantile.dropna()


def infer_trading_calendar(factor_idx, prices_idx):
    """
    Infer the trading calendar from factor and price information.

    Parameters
    ----------
    factor_idx : pd.DatetimeIndex
        The factor datetimes for which we are computing the forward returns
    prices_idx : pd.DatetimeIndex
        The prices datetimes associated withthe factor data

    Returns
    -------
    calendar : pd.DateOffset
    """
    full_idx = factor_idx.union(prices_idx)

    traded_weekdays = []
    holidays = []

    days_of_the_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    for day, day_str in enumerate(days_of_the_week):

        weekday_mask = (full_idx.dayofweek == day)

        # drop days of the week that are not traded at all
        if not weekday_mask.any():
            continue
        traded_weekdays.append(day_str)

        # look for holidays
        used_weekdays = full_idx[weekday_mask].normalize()
        all_weekdays = pd.date_range(full_idx.min(), full_idx.max(),
                                     freq=CustomBusinessDay(weekmask=day_str)
                                     ).normalize()
        _holidays = all_weekdays.difference(used_weekdays)
        _holidays = [timestamp.date() for timestamp in _holidays]
        holidays.extend(_holidays)

    traded_weekdays = ' '.join(traded_weekdays)
    return CustomBusinessDay(weekmask=traded_weekdays, holidays=holidays)


def _to_forward_return(price_df, timedelta, dateset, initial_delta='0D',
                       max_inactive_delta='5D', debug=False):
    """
    Build forward return by:
    - look for next available price date in the price dataframe as start date,
        if the next available price date is more than max_inactivate_days,
        an exception is raised
    - look for the next end price date by adding timedelta to the start date
    - compute percentage change
    Time complexity O(nlogk), n=len(dateset), k=len(df)
    :param price_df: price dataframe
    :param timedelta: period used to compute forward return
    :param dateset: dates to compute forward return for
    :param max_inactive_delta: maximum inactive timedelta used to find the next
                            available price start date
    :return: forward return dataframe
    """
    init_timedelta = pd.Timedelta(initial_delta)
    max_inactive_timedelta = pd.Timedelta(max_inactive_delta)
    if init_timedelta >= max_inactive_timedelta:
        raise ValueError('Initial delta {i_del} cannot be longer than'
                         'maximum inactive time delta {m_del},'
                         'please fix'.format(i_del=init_timedelta,
                                             m_del=max_inactive_timedelta))
    if debug:
        print('timedelta={}, initial_delta={}, max_inactivate_delta={}'.format(
            timedelta,
            init_timedelta,
            max_inactive_timedelta))
    df_t = price_df.T.copy()
    price_df = pd.DataFrame()
    columns = df_t.columns
    for col in sorted(dateset):
        next_start_idx = np.searchsorted(columns, col + init_timedelta,
                                         side='left')
        if next_start_idx >= len(columns):
            price_df[col] = np.nan
            continue
        next_start = columns[next_start_idx]
        if timedelta == pd.Timedelta(0):
            price_df[col] = df_t[next_start]
            continue
        if next_start - col > max_inactive_timedelta:
            raise ValueError(
                'Time different between '
                'factor data (indexed at {f_idx}) and '
                'price data (next available at {p_idx}) '
                'is greater than max inactive days {i_days}.'
                'Please either fix your factor data, '
                'or increase max inactive days parameter'.format(
                    f_idx=col,
                    p_idx=next_start,
                    i_days=max_inactive_delta
                ))
        next_end_idx = np.searchsorted(columns, next_start + timedelta,
                                       side='left')
        if next_end_idx >= len(columns):
            price_df[col] = np.nan
        else:
            next_end = columns[next_end_idx]
            if debug:
                print("Fetched pricing data for {}: "
                      "start={}, end={}".format(col, next_start, next_end))
            price_df[col] = (df_t[next_end] - df_t[next_start]) / df_t[
                next_start]
    return price_df.T


def compute_forward_returns_benchmark(factor,
                                      benchmark_prices,
                                      periods=('1D', '5D', '10D'),
                                      filter_zscore=None,
                                      initial_delta='0D',
                                      max_inactive_delta='32D',
                                      debug=False):
    factor_dateindex = factor.index.get_level_values('date').unique()

    if len(factor_dateindex) == 0:
        raise ValueError("Factor and prices indices don't match: make sure "
                         "they have the same convention in terms of datetimes "
                         "and symbol-names")

    forward_returns = pd.DataFrame(index=pd.MultiIndex.from_product(
        [factor_dateindex, benchmark_prices.columns], names=['date', 'asset']))

    factor_date_set = set(factor_dateindex.unique())

    for period in sorted(periods):
        period_timedelta = pd.Timedelta(period)
        fwdret = (_to_forward_return(benchmark_prices, period_timedelta,
                                     factor_date_set,
                                     initial_delta,
                                     max_inactive_delta,
                                     debug)
                  .reindex(factor_dateindex))
        fwdret = fwdret[fwdret.index.get_level_values(0).isin(factor_date_set)]
        if filter_zscore is not None:
            mask = abs(fwdret - fwdret.mean()) > (filter_zscore * fwdret.std())
            fwdret[mask] = np.nan

        forward_returns[period] = fwdret.stack()

    return forward_returns


def compute_forward_returns(factor,
                            prices,
                            periods=('1D', '5D', '10D'),
                            filter_zscore=None,
                            initial_delta='0D',
                            max_inactive_delta='5D',
                            debug=False):
    """
    Finds the N period forward returns (as percent change) for each asset
    provided.

    Parameters
    ----------
    factor : pd.Series - MultiIndex
        A MultiIndex Series indexed by timestamp (level 0) and asset
        (level 1), containing the values for a single alpha factor.

        - See full explanation in utils.get_clean_factor_and_forward_returns

    prices : pd.DataFrame
        Pricing data to use in forward price calculation.
        Assets as columns, dates as index. Pricing data must
        span the factor analysis time period plus an additional buffer window
        that is greater than the maximum number of expected periods
        in the forward returns calculations.

    periods : sequence[int]
        periods to compute forward returns on.

    filter_zscore : int or float, optional
        Sets forward returns greater than X standard deviations
        from the the mean to nan. Set it to 'None' to avoid filtering.
        Caution: this outlier filtering incorporates lookahead bias.

    initial_delta: Pandas timedelta string, optional
        Timedelta to look for start datetime of return computation

    max_inactive_delta: Pandas timedelta string, optional
        Timedelta that is allowed between the start datetime of
        return computation and factor datetime

    debug: boolean
        Whether to show debug information

    Returns
    -------
    forward_returns : pd.DataFrame - MultiIndex
        A MultiIndex DataFrame indexed by timestamp (level 0) and asset
        (level 1), containing the forward returns for assets.
        Forward returns column names follow the format accepted by
        pd.Timedelta (e.g. '1D', '30m', '3h15m', '1D1h', etc).
        'date' index freq property (forward_returns.index.levels[0].freq)
        will be set to a trading calendar (pandas DateOffset) inferred
        from the input data (see infer_trading_calendar for more details).
    """
    factor_dateindex = factor.index.get_level_values('date').unique()
    if factor_dateindex.tz != prices.index.tz:
        raise NonMatchingTimezoneError("The timezone of 'factor' is not the "
                                       "same as the timezone of 'prices'. See "
                                       "the pandas methods tz_localize and "
                                       "tz_convert.")

    freq = pd.infer_freq(factor_dateindex)

    if len(factor_dateindex) == 0:
        raise ValueError("Factor and prices indices don't match: make sure "
                         "they have the same convention in terms of datetimes "
                         "and symbol-names")

    forward_returns = pd.DataFrame(index=pd.MultiIndex.from_product(
        [factor_dateindex, prices.columns], names=['date', 'asset']))

    forward_returns.index.levels[0].freq = freq

    factor_date_set = set(factor_dateindex.unique())

    for period in sorted(periods):
        period_timedelta = pd.Timedelta(period)
        fwdret = (_to_forward_return(prices, period_timedelta, factor_date_set,
                                     initial_delta,
                                     max_inactive_delta,
                                     debug)
                  .reindex(factor_dateindex))
        fwdret = fwdret[fwdret.index.get_level_values(0).isin(factor_date_set)]
        if filter_zscore is not None:
            mask = abs(fwdret - fwdret.mean()) > (filter_zscore * fwdret.std())
            fwdret[mask] = np.nan

        forward_returns[period] = fwdret.stack()

    original_price = (_to_forward_return(prices, pd.Timedelta(0),
                                         factor_date_set,
                                         initial_delta,
                                         max_inactive_delta,
                                         debug)
                      .reindex(factor_dateindex))
    forward_returns['original'] = original_price.stack()

    forward_returns.index = forward_returns.index.rename(['date', 'asset'])

    return forward_returns


def demean_forward_returns(factor_data, grouper=None):
    """
    Convert forward returns to returns relative to mean
    period wise all-universe or group returns.
    group-wise normalization incorporates the assumption of a
    group neutral portfolio constraint and thus allows allows the
    factor to be evaluated across groups.

    For example, if AAPL 5 period return is 0.1% and mean 5 period
    return for the Technology stocks in our universe was 0.5% in the
    same period, the group adjusted 5 period return for AAPL in this
    period is -0.4%.

    Parameters
    ----------
    factor_data : pd.DataFrame - MultiIndex
        Forward returns indexed by date and asset.
        Separate column for each forward return window.
    grouper : list
        If True, demean according to group.

    Returns
    -------
    adjusted_forward_returns : pd.DataFrame - MultiIndex
        DataFrame of the same format as the input, but with each
        security's returns normalized by group.
    """

    factor_data = factor_data.copy()

    if not grouper:
        grouper = factor_data.index.get_level_values('date')

    cols = get_forward_returns_columns(factor_data.columns)
    factor_data[cols] = factor_data.groupby(grouper)[cols] \
        .transform(lambda x: x - x.mean())

    return factor_data


def print_table(table, name=None, fmt=None):
    """
    Pretty print a pandas DataFrame.

    Uses HTML output if running inside Jupyter Notebook, otherwise
    formatted text output.

    Parameters
    ----------
    table : pd.Series or pd.DataFrame
        Table to pretty-print.
    name : str, optional
        Table name to display in upper left corner.
    fmt : str, optional
        Formatter to use for displaying table elements.
        E.g. '{0:.2f}%' for displaying 100 as '100.00%'.
        Restores original setting after displaying.
    """
    if isinstance(table, pd.Series):
        table = pd.DataFrame(table)

    if isinstance(table, pd.DataFrame):
        table.columns.name = name

    prev_option = pd.get_option('display.float_format')
    if fmt is not None:
        pd.set_option('display.float_format', lambda x: fmt.format(x))

    display(table)

    if fmt is not None:
        pd.set_option('display.float_format', prev_option)


def get_clean_factor(factor,
                     forward_returns,
                     groupby=None,
                     binning_by_group=False,
                     quantiles=5,
                     bins=None,
                     groupby_labels=None,
                     max_loss=0.35,
                     zero_aware=False,
                     clean_binning=True):
    """
    Formats the factor data, forward return data, and group mappings into a
    DataFrame that contains aligned MultiIndex indices of timestamp and asset.
    The returned data will be formatted to be suitable for Alphalens functions.

    It is safe to skip a call to this function and still make use of Alphalens
    functionalities as long as the factor data conforms to the format returned
    from get_clean_factor_and_forward_returns and documented here

    Parameters
    ----------
    factor : pd.Series - MultiIndex
        A MultiIndex Series indexed by timestamp (level 0) and asset
        (level 1), containing the values for a single alpha factor.
        ::
            -----------------------------------
                date    |    asset   |
            -----------------------------------
                        |   AAPL     |   0.5
                        -----------------------
                        |   BA       |  -1.1
                        -----------------------
            2014-01-01  |   CMG      |   1.7
                        -----------------------
                        |   DAL      |  -0.1
                        -----------------------
                        |   LULU     |   2.7
                        -----------------------

    forward_returns : pd.DataFrame - MultiIndex
        A MultiIndex DataFrame indexed by timestamp (level 0) and asset
        (level 1), containing the forward returns for assets.
        Forward returns column names must follow the format accepted by
        pd.Timedelta (e.g. '1D', '30m', '3h15m', '1D1h', etc).
        'date' index freq property must be set to a trading calendar
        (pandas DateOffset), see infer_trading_calendar for more details.
        This information is currently used only in cumulative returns
        computation
        ::
            ---------------------------------------
                       |       | 1D  | 5D  | 10D
            ---------------------------------------
                date   | asset |     |     |
            ---------------------------------------
                       | AAPL  | 0.09|-0.01|-0.079
                       ----------------------------
                       | BA    | 0.02| 0.06| 0.020
                       ----------------------------
            2014-01-01 | CMG   | 0.03| 0.09| 0.036
                       ----------------------------
                       | DAL   |-0.02|-0.06|-0.029
                       ----------------------------
                       | LULU  |-0.03| 0.05|-0.009
                       ----------------------------

    groupby : pd.Series - MultiIndex or dict
        Either A MultiIndex Series indexed by date and asset,
        containing the period wise group codes for each asset, or
        a dict of asset to group mappings. If a dict is passed,
        it is assumed that group mappings are unchanged for the
        entire time period of the passed factor data.
    binning_by_group : bool
        If True, compute quantile buckets separately for each group.
        This is useful when the factor values range vary considerably
        across gorups so that it is wise to make the binning group relative.
        You should probably enable this if the factor is intended
        to be analyzed for a group neutral portfolio
    quantiles : int or sequence[float]
        Number of equal-sized quantile buckets to use in factor bucketing.
        Alternately sequence of quantiles, allowing non-equal-sized buckets
        e.g. [0, .10, .5, .90, 1.] or [.05, .5, .95]
        Only one of 'quantiles' or 'bins' can be not-None
    bins : int or sequence[float]
        Number of equal-width (valuewise) bins to use in factor bucketing.
        Alternately sequence of bin edges allowing for non-uniform bin width
        e.g. [-4, -2, -0.5, 0, 10]
        Chooses the buckets to be evenly spaced according to the values
        themselves. Useful when the factor contains discrete values.
        Only one of 'quantiles' or 'bins' can be not-None
    groupby_labels : dict
        A dictionary keyed by group code with values corresponding
        to the display name for each group.
    max_loss : float, optional
        Maximum percentage (0.00 to 1.00) of factor data dropping allowed,
        computed comparing the number of items in the input factor index and
        the number of items in the output DataFrame index.
        Factor data can be partially dropped due to being flawed itself
        (e.g. NaNs), not having provided enough price data to compute
        forward returns for all factor values, or because it is not possible
        to perform binning.
        Set max_loss=0 to avoid Exceptions suppression.
    zero_aware : bool, optional
        If True, compute quantile buckets separately for positive and negative
        signal values. This is useful if your signal is centered and zero is
        the separation between long and short signals, respectively.
        'quantiles' is None.
    clean_binning: bool, optional
        If True, cleaning factor data that is not properly binned



    Returns
    -------
    merged_data : pd.DataFrame - MultiIndex
        A MultiIndex Series indexed by date (level 0) and asset (level 1),
        containing the values for a single alpha factor, forward returns for
        each period, the factor quantile/bin that factor value belongs to, and
        (optionally) the group the asset belongs to.

        - forward returns column names follow the format accepted by
          pd.Timedelta (e.g. '1D', '30m', '3h15m', '1D1h', etc)

        - 'date' index freq property (merged_data.index.levels[0].freq) is the
          same as that of the input forward returns data. This is currently
          used only in cumulative returns computation
        ::
           -------------------------------------------------------------------
                      |       | 1D  | 5D  | 10D  |factor|group|factor_quantile
           -------------------------------------------------------------------
               date   | asset |     |     |      |      |     |
           -------------------------------------------------------------------
                      | AAPL  | 0.09|-0.01|-0.079|  0.5 |  G1 |      3
                      --------------------------------------------------------
                      | BA    | 0.02| 0.06| 0.020| -1.1 |  G2 |      5
                      --------------------------------------------------------
           2014-01-01 | CMG   | 0.03| 0.09| 0.036|  1.7 |  G2 |      1
                      --------------------------------------------------------
                      | DAL   |-0.02|-0.06|-0.029| -0.1 |  G3 |      5
                      --------------------------------------------------------
                      | LULU  |-0.03| 0.05|-0.009|  2.7 |  G1 |      2
                      --------------------------------------------------------
    """

    initial_amount = float(len(factor.index))

    factor = factor.copy()
    factor.index = factor.index.rename(['date', 'asset'])

    merged_data = forward_returns.copy()
    merged_data['factor'] = factor

    if groupby is not None:
        if isinstance(groupby, dict):
            diff = set(factor.index.get_level_values(
                'asset')) - set(groupby.keys())
            if len(diff) > 0:
                raise KeyError(
                    "Assets {} not in group mapping".format(
                        list(diff)))

            ss = pd.Series(groupby)
            groupby = pd.Series(index=factor.index,
                                data=ss[factor.index.get_level_values(
                                    'asset')].values)

        if groupby_labels is not None:
            diff = set(groupby.values) - set(groupby_labels.keys())
            if len(diff) > 0:
                raise KeyError(
                    "groups {} not in passed group names".format(
                        list(diff)))

            sn = pd.Series(groupby_labels)
            groupby = pd.Series(index=groupby.index,
                                data=sn[groupby.values].values)

        merged_data['group'] = groupby.astype('category')

    merged_data = merged_data.dropna()

    fwdret_amount = float(len(merged_data.index))

    if clean_binning:
        no_raise = False if max_loss == 0 else True
        merged_data['factor_quantile'] = quantize_factor(merged_data,
                                                         quantiles,
                                                         bins,
                                                         binning_by_group,
                                                         no_raise,
                                                         zero_aware)

        merged_data = merged_data.dropna()

    binning_amount = float(len(merged_data.index))

    tot_loss = (initial_amount - binning_amount) / initial_amount
    fwdret_loss = (initial_amount - fwdret_amount) / initial_amount
    bin_loss = tot_loss - fwdret_loss

    print("Dropped %.1f%% entries from factor data: %.1f%% in forward "
          "returns computation and %.1f%% in binning phase "
          "(set max_loss=0 to see potentially suppressed Exceptions)." %
          (tot_loss * 100, fwdret_loss * 100, bin_loss * 100))

    if tot_loss > max_loss:
        message = ("max_loss (%.1f%%) exceeded %.1f%%, consider increasing it."
                   % (max_loss * 100, tot_loss * 100))
        raise MaxLossExceededError(message)
    else:
        print("max_loss is %.1f%%, not exceeded: OK!" % (max_loss * 100))

    return merged_data


def get_clean_factor_and_forward_returns(factor,
                                         prices,
                                         groupby=None,
                                         binning_by_group=False,
                                         quantiles=5,
                                         bins=None,
                                         periods=('1D', '5D', '10D'),
                                         filter_zscore=20,
                                         groupby_labels=None,
                                         max_loss=0.35,
                                         zero_aware=False,
                                         clean_binning=True,
                                         initial_delta='0D',
                                         max_inactive_delta='5D',
                                         debug=False):
    """
    Formats the factor data, pricing data, and group mappings into a DataFrame
    that contains aligned MultiIndex indices of timestamp and asset. The
    returned data will be formatted to be suitable for Alphalens functions.

    It is safe to skip a call to this function and still make use of Alphalens
    functionalities as long as the factor data conforms to the format returned
    from get_clean_factor_and_forward_returns and documented here

    Parameters
    ----------
    factor : pd.Series - MultiIndex
        A MultiIndex Series indexed by timestamp (level 0) and asset
        (level 1), containing the values for a single alpha factor.
        ::
            -----------------------------------
                date    |    asset   |
            -----------------------------------
                        |   AAPL     |   0.5
                        -----------------------
                        |   BA       |  -1.1
                        -----------------------
            2014-01-01  |   CMG      |   1.7
                        -----------------------
                        |   DAL      |  -0.1
                        -----------------------
                        |   LULU     |   2.7
                        -----------------------

    prices : pd.DataFrame
        A wide form Pandas DataFrame indexed by timestamp with assets
        in the columns.
        Pricing data must span the factor analysis time period plus an
        additional buffer window that is greater than the maximum number
        of expected periods in the forward returns calculations.
        It is important to pass the correct pricing data in depending on
        what time of period your signal was generated so to avoid lookahead
        bias, or  delayed calculations.
        'Prices' must contain at least an entry for each timestamp/asset
        combination in 'factor'. This entry should reflect the buy price
        for the assets and usually it is the next available price after the
        factor is computed but it can also be a later price if the factor is
        meant to be traded later (e.g. if the factor is computed at market
        open but traded 1 hour after market open the price information should
        be 1 hour after market open).
        'Prices' must also contain entries for timestamps following each
        timestamp/asset combination in 'factor', as many more timestamps
        as the maximum value in 'periods'. The asset price after 'period'
        timestamps will be considered the sell price for that asset when
        computing 'period' forward returns.
        ::
            ----------------------------------------------------
                        | AAPL |  BA  |  CMG  |  DAL  |  LULU  |
            ----------------------------------------------------
               Date     |      |      |       |       |        |
            ----------------------------------------------------
            2014-01-01  |605.12| 24.58|  11.72| 54.43 |  37.14 |
            ----------------------------------------------------
            2014-01-02  |604.35| 22.23|  12.21| 52.78 |  33.63 |
            ----------------------------------------------------
            2014-01-03  |607.94| 21.68|  14.36| 53.94 |  29.37 |
            ----------------------------------------------------

    groupby : pd.Series - MultiIndex or dict
        Either A MultiIndex Series indexed by date and asset,
        containing the period wise group codes for each asset, or
        a dict of asset to group mappings. If a dict is passed,
        it is assumed that group mappings are unchanged for the
        entire time period of the passed factor data.
    binning_by_group : bool
        If True, compute quantile buckets separately for each group.
        This is useful when the factor values range vary considerably
        across gorups so that it is wise to make the binning group relative.
        You should probably enable this if the factor is intended
        to be analyzed for a group neutral portfolio
    quantiles : int or sequence[float]
        Number of equal-sized quantile buckets to use in factor bucketing.
        Alternately sequence of quantiles, allowing non-equal-sized buckets
        e.g. [0, .10, .5, .90, 1.] or [.05, .5, .95]
        Only one of 'quantiles' or 'bins' can be not-None
    bins : int or sequence[float]
        Number of equal-width (valuewise) bins to use in factor bucketing.
        Alternately sequence of bin edges allowing for non-uniform bin width
        e.g. [-4, -2, -0.5, 0, 10]
        Chooses the buckets to be evenly spaced according to the values
        themselves. Useful when the factor contains discrete values.
        Only one of 'quantiles' or 'bins' can be not-None
    periods : sequence[int]
        periods to compute forward returns on.
    filter_zscore : int or float, optional
        Sets forward returns greater than X standard deviations
        from the the mean to nan. Set it to 'None' to avoid filtering.
        Caution: this outlier filtering incorporates lookahead bias.
    groupby_labels : dict
        A dictionary keyed by group code with values corresponding
        to the display name for each group.
    max_loss : float, optional
        Maximum percentage (0.00 to 1.00) of factor data dropping allowed,
        computed comparing the number of items in the input factor index and
        the number of items in the output DataFrame index.
        Factor data can be partially dropped due to being flawed itself
        (e.g. NaNs), not having provided enough price data to compute
        forward returns for all factor values, or because it is not possible
        to perform binning.
        Set max_loss=0 to avoid Exceptions suppression.
    zero_aware : bool, optional
        If True, compute quantile buckets separately for positive and negative
        signal values. This is useful if your signal is centered and zero is
        the separation between long and short signals, respectively.

    clean_binning:
        If True, cleaning factor data that is not properly binned

    initial_delta: Pandas timedelta string, optional
        Timedelta to look for start datetime of return computation

    max_inactive_delta: Pandas timedelta string, optional
        Timedelta that is allowed between the start datetime of
        return computation and factor datetime

    debug: boolean
        Whether to show debug information

    Returns
    -------
    merged_data : pd.DataFrame - MultiIndex
        A MultiIndex Series indexed by date (level 0) and asset (level 1),
        containing the values for a single alpha factor, forward returns for
        each period, the factor quantile/bin that factor value belongs to, and
        (optionally) the group the asset belongs to.
        - forward returns column names follow  the format accepted by
          pd.Timedelta (e.g. '1D', '30m', '3h15m', '1D1h', etc)
        - 'date' index freq property (merged_data.index.levels[0].freq) will be
          set to a trading calendar (pandas DateOffset) inferred from the input
          data (see infer_trading_calendar for more details). This is currently
          used only in cumulative returns computation
        ::
           -------------------------------------------------------------------
                      |       | 1D  | 5D  | 10D  |factor|group|factor_quantile
           -------------------------------------------------------------------
               date   | asset |     |     |      |      |     |
           -------------------------------------------------------------------
                      | AAPL  | 0.09|-0.01|-0.079|  0.5 |  G1 |      3
                      --------------------------------------------------------
                      | BA    | 0.02| 0.06| 0.020| -1.1 |  G2 |      5
                      --------------------------------------------------------
           2014-01-01 | CMG   | 0.03| 0.09| 0.036|  1.7 |  G2 |      1
                      --------------------------------------------------------
                      | DAL   |-0.02|-0.06|-0.029| -0.1 |  G3 |      5
                      --------------------------------------------------------
                      | LULU  |-0.03| 0.05|-0.009|  2.7 |  G1 |      2
                      --------------------------------------------------------
    """

    forward_returns = \
        compute_forward_returns(factor, prices, periods,
                                filter_zscore,
                                initial_delta=initial_delta,
                                max_inactive_delta=max_inactive_delta,
                                debug=debug)

    factor_data = get_clean_factor(factor, forward_returns, groupby=groupby,
                                   groupby_labels=groupby_labels,
                                   quantiles=quantiles, bins=bins,
                                   binning_by_group=binning_by_group,
                                   max_loss=max_loss, zero_aware=zero_aware,
                                   clean_binning=clean_binning)

    return factor_data


def rate_of_return(period_ret, base_period):
    """
    Convert returns to 'one_period_len' rate of returns: that is the value the
    returns would have every 'one_period_len' if they had grown at a steady
    rate

    Parameters
    ----------
    period_ret: pd.DataFrame
        DataFrame containing returns values with column headings representing
        the return period.
    base_period: string
        The base period length used in the conversion
        It must follow pandas.Timedelta constructor format (e.g. '1 days',
        '1D', '30m', '3h', '1D1h', etc)

    Returns
    -------
    pd.DataFrame
        DataFrame in same format as input but with 'one_period_len' rate of
        returns values.
    """
    period_len = period_ret.name
    conversion_factor = (pd.Timedelta(base_period) /
                         pd.Timedelta(period_len))
    return period_ret.add(1).pow(conversion_factor).sub(1)


def std_conversion(period_std, base_period):
    """
    one_period_len standard deviation (or standard error) approximation

    Parameters
    ----------
    period_std: pd.DataFrame
        DataFrame containing standard deviation or standard error values
        with column headings representing the return period.
    base_period: string
        The base period length used in the conversion
        It must follow pandas.Timedelta constructor format (e.g. '1 days',
        '1D', '30m', '3h', '1D1h', etc)

    Returns
    -------
    pd.DataFrame
        DataFrame in same format as input but with one-period
        standard deviation/error values.
    """
    period_len = period_std.name
    conversion_factor = (pd.Timedelta(period_len) /
                         pd.Timedelta(base_period))
    return period_std / np.sqrt(conversion_factor)


def get_forward_returns_columns(columns):
    """
    Utility that detects and returns the columns that are forward returns
    """
    pattern = re.compile(r"^(\d+([Dhms]|ms|us|ns))+$", re.IGNORECASE)
    valid_columns = [(pattern.match(col) is not None) for col in columns]
    return columns[valid_columns]


def timedelta_to_string(timedelta):
    """
    Utility that converts a pandas.Timedelta to a string representation
    compatible with pandas.Timedelta constructor format

    Parameters
    ----------
    timedelta: pd.Timedelta

    Returns
    -------
    string
        string representation of 'timedelta'
    """
    c = timedelta.components
    timedelta_format = ''
    if c.days != 0:
        timedelta_format += '%dD' % c.days
    if c.hours > 0:
        timedelta_format += '%dh' % c.hours
    if c.minutes > 0:
        timedelta_format += '%dm' % c.minutes
    if c.seconds > 0:
        timedelta_format += '%ds' % c.seconds
    if c.milliseconds > 0:
        timedelta_format += '%dms' % c.milliseconds
    if c.microseconds > 0:
        timedelta_format += '%dus' % c.microseconds
    if c.nanoseconds > 0:
        timedelta_format += '%dns' % c.nanoseconds
    return timedelta_format


def _freq_unit_to_timedelta(freq_unit):
    if freq_unit in {'B', 'C', 'D'}:
        return 'D'
    elif freq_unit in {'M', 'MS', 'BM', 'CBM', 'CBMS', 'BMS'}:
        return 'M'
    else:
        warnings.warn("Frequency {} is not recognized "
                      "by converter".format(freq_unit))
        return freq_unit


def _freq_to_timedelta(freq):
    if not isinstance(freq, str):
        freqstr = freq.freqstr
    else:
        freqstr = freq
    if hasattr(freq, 'n'):
        freq_n = freq.n
    else:
        freq_n = 1
    freq_unit = re.match('\d*(\w+)', freqstr).group(1)
    timedelta_unit = _freq_unit_to_timedelta(freq_unit)
    return pd.Timedelta(freq_n, unit=timedelta_unit)


def add_custom_calendar_timedelta(input_date, timedelta, freq):
    """
    Add timedelta to 'input' taking into consideration custom frequency, which
    is used to deal with custom calendars, such as a trading calendar

    Parameters
    ----------
    input_date : pd.DatetimeIndex or pd.Timestamp
    timedelta : pd.Timedelta
    freq : DateOffset, optional

    Returns
    -------
    pd.DatetimeIndex or pd.Timestamp
        input + timedelta
    """

    return input_date + timedelta


def diff_custom_calendar_timedeltas(start, end, input_idx):
    """
    Compute the difference between two pd.Timedelta taking into consideration
    custom frequency, which is used to deal with custom calendars, such as a
    trading calendar

    Parameters
    ----------
    start : pd.Timestamp
    end : pd.Timestamp

    Returns
    -------
    pd.Timedelta
        end - start
    """
    s_idx, e_idx = np.searchsorted(input_idx, pd.to_datetime([start, end]))
    return e_idx - s_idx


def _get_date_values(df):
    if isinstance(df.index, pd.MultiIndex):
        return df.index.get_level_values('date')
    else:
        return df.index


def _min(df):
    return _get_date_values(df).min()


def _max(df):
    return _get_date_values(df).max()


def _next_idx(df, val):
    dates = _get_date_values(df)
    idx = np.searchsorted(dates, val)
    return dates[idx] if idx < len(dates) else val


def _truncate(df, start_date, end_date):
    if isinstance(df.index, pd.MultiIndex):
        return df.to_eqi().e_between('date', start_date,
                                     end_date).to_pandas()
    else:
        return df[(df.index >= start_date) & (df.index <= end_date)]


def overlap_date(*dfs):
    start_date = max([_min(df) for df in dfs])
    end_date = min([_max(df) for df in dfs])
    return (_truncate(df, start_date, end_date) for df in dfs)


def match_date(*dfs):
    df_to_match = dfs[0]
    start_date = _min(df_to_match)
    end_date = _max(df_to_match)
    return (_truncate(df, start_date, _next_idx(df, end_date)) for df in
            dfs[1:])


def _append_index(df, timedelta):
    index = df.index.get_level_values('date')
    index.append(pd.Index([index.max() + timedelta]))
    return index
