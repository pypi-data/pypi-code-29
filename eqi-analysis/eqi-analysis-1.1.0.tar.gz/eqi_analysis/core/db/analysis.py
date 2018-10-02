import numpy as np
import pandas as pd
from alphalens import utils
from matplotlib import pyplot as plt

from eqi_analysis.core import plot, refdata
from eqi_analysis.core.utils import get_total_quantiles

FIG_SIZE = (20, 7)
SPLIT_LINE_X = None


def _to_split_x_idx(idx_values, value):
    return np.searchsorted(idx_values, value)


def _plot_split_line(ax, x):
    ax.axvline(x=x, color='red', linestyle='-.', alpha=0.5)


def plot_split_line(ax):
    if SPLIT_LINE_X is not None:
        _plot_split_line(ax, SPLIT_LINE_X)


def plot_split_idx_line(ax, idx_values):
    if SPLIT_LINE_X is not None:
        split_x = _to_split_x_idx(idx_values, SPLIT_LINE_X)
        _plot_split_line(ax, split_x)


def _to_mean_return(alphalens_factor, period):
    total_quantiles = get_total_quantiles(alphalens_factor)
    mean_return = alphalens_factor.groupby(['factor_quantile', 'date'])[
        period].mean().unstack(0)
    mean_return['spread'] = mean_return[total_quantiles] - mean_return[1]
    return mean_return


def get_performance(alphalens_factor, period):
    mean_return = _to_mean_return(alphalens_factor, period)
    mean_return = mean_return['spread'].shift(1) + 1
    mean_return.iloc[0] = 1
    return mean_return.cumprod()


def plot_performance(alphalens_factor, period, desc=''):
    performance = get_performance(alphalens_factor, period)
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    ax.plot(performance)
    ax.grid(True)
    ax.set_title(
        'Long-Short Portfolio Performance, Period={} {}'.format(period, desc))
    ax.set_ylabel('Performance')
    plot_split_line(ax)


def get_turnover(alphalens_factor, period, window=12):
    def turn_over(df, q):
        return (df[q] - df[q].shift(1)).apply(
            lambda s: len(s) if pd.notnull(s) else 0) / df[q].shift(1).apply(
            lambda s: len(s) if pd.notnull(s) else 1)

    total_quantiles = get_total_quantiles(alphalens_factor)
    assets = alphalens_factor.groupby(['factor_quantile', 'date'])[
        period].apply(
        lambda df: set(df.dropna().index.get_level_values('asset'))).unstack(0)
    two_way_turnover = turn_over(assets, 1) + turn_over(assets,
                                                        total_quantiles)
    two_way_turnover_mean = two_way_turnover.rolling(window).mean()
    turnover_df = pd.concat([two_way_turnover, two_way_turnover_mean],
                            axis=1)
    turnover_df.columns = ['Two way turnover', 'Moving average window=12']
    return turnover_df


def plot_turnover(alphalens_factor, period, desc=''):
    turnover_df = get_turnover(alphalens_factor, period)
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    plot.bar_line(turnover_df, ax, bar_columns=['Two way turnover'],
                  line_columns=['Moving average window=12'], width=0.5,
                  title='Two-Way L/S Turnover, Period={} {}'.format(period,
                                                                    desc))
    plot_split_idx_line(ax, pd.to_datetime(turnover_df.index.values))


def get_ann_return(alphalens_factor, period):
    total_quantiles = get_total_quantiles(alphalens_factor)
    quantile_ann_returns = [annualized_return(
        alphalens_factor[alphalens_factor.factor_quantile == i][
            period])
        for i in range(1, total_quantiles + 1)]
    mean_return = _to_mean_return(alphalens_factor, period)
    spread_ann = annualized_return(mean_return['spread'])
    return quantile_ann_returns + [spread_ann]


def plot_quantile_ann_return(alphalens_factor, period, desc=''):
    total_quantiles = get_total_quantiles(alphalens_factor)
    ann_returns = get_ann_return(alphalens_factor, period)
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    xticks = list(range(1, total_quantiles + 2))
    ax.bar(xticks, ann_returns)
    ax.grid(True)
    ax.set_title(
        'Quantile Portfolio Annualized Returns, Period={} {}'.format(period,
                                                                     desc))
    plt.xticks(xticks, list(range(1, total_quantiles + 1)) + ['L/S'])


def get_return_spread(alphalens_factor, period):
    mean_return = _to_mean_return(alphalens_factor, period)
    mean_return['rolling_spread_window_12'] = mean_return[
        'spread'].rolling(12).mean()
    return mean_return


def plot_return_spread(alphalens_factor, period, desc=''):
    mean_return = get_return_spread(alphalens_factor, period)
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    plot.bar_line(mean_return, ax, bar_columns=['spread'],
                  line_columns=['rolling_spread_window_12'], width=0.5,
                  title='Spread, Period={} {}'.format(period, desc))
    basic_stat = str(mean_return['spread'].describe())
    basic_stat = '\n'.join(basic_stat.splitlines()[0:-1])
    ax.text(0.05, 0.95, basic_stat, transform=ax.transAxes, fontsize=14,
            verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.5))
    plot_split_idx_line(ax, pd.to_datetime(mean_return.index.values))


def plot_quantiles_boundary(alphalens_factor, name):
    quantile_mean = \
        alphalens_factor.groupby(['factor_quantile', 'date'])[
            'factor'].max()
    quantile_index = quantile_mean.index.get_level_values(0)
    total_quantiles = len(quantile_index.unique())
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    idx_values = None
    for q in range(1, total_quantiles):
        data_in_quantile = quantile_mean[quantile_index == q]
        data_in_quantile.index = data_in_quantile.index.droplevel(0)
        idx_values = pd.to_datetime(data_in_quantile.index.values)
        idx_idx = np.arange(len(idx_values))
        ax.plot(idx_idx, data_in_quantile,
                label="{0:.0%}".format(q / total_quantiles))
        plt.xticks(idx_idx,
                   ['{}.{}'.format(idx.year,
                                   idx.month) if idx.month == 1 else '' for
                    idx in idx_values], rotation=90)
    ax.set_title('Factor Quantile Boundary for {}'.format(name))
    ax.legend()
    ax.grid(True)
    plot_split_idx_line(ax, idx_values)


def plot_coverage_graph(alphalens_factor, _benchmark_name, _factor):
    if alphalens_factor is None:
        raise AttributeError(
            "Alphalens factor needs to be computed first,"
            " please call portfolio.to_alphalens_factor()")
    if _benchmark_name is None:
        raise AttributeError(
            "Coverage graph is against a benchmark, try"
            " portfolio.use_benchmark(benchmark)")

    benchmark = _benchmark_name
    factor_df = _factor.raw_df
    holding_count = refdata.fetch_index_holdings(_benchmark_name)[
        'tickers'].apply(
        lambda v: len(v.split(',')))

    factor_filtered_count = factor_df.groupby('date').count()

    final_count = alphalens_factor.groupby('date')[
        'factor'].count()

    holding_count, factor_filtered_count = utils.overlap_date(
        holding_count, factor_filtered_count)

    def rolling_mean(df, window=12):
        return df.rolling(window).mean()

    factor_filtered_count, final_count, holding_count = utils.overlap_date(
        factor_filtered_count, final_count, holding_count)
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    names = ['# Stocks in Factor Universe', '# Stocks in Index',
             '# Stocks after Price Join',
             'Mean # Stocks in Factor Universe (window=12)',
             'Mean # Stocks after Price Join (window=12)']
    coverage_df = pd.concat(
        [factor_filtered_count, holding_count, final_count], names=names,
        axis=1, join='inner')
    factor_rmean = rolling_mean(factor_filtered_count)
    final_rmean = rolling_mean(final_count)
    coverage_df = pd.concat([coverage_df, factor_rmean, final_rmean],
                            axis=1)
    coverage_df.columns = names

    title = 'Coverage against {}'.format(benchmark)
    plot.bar_line(coverage_df, ax, bar_columns=names[0:3],
                  line_columns=names[3:5], width=0.5, title=title)
    plot_split_idx_line(ax, pd.to_datetime(coverage_df.index.values))


def annualized_return(return_df):
    min_date = return_df.index.get_level_values('date').min()
    max_date = return_df.index.get_level_values('date').max()
    days_delta = (max_date - min_date).days
    return pow((return_df.groupby('date').mean() + 1).cumprod()[-1],
               252 / days_delta) - 1
