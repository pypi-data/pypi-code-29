import numpy as np
import pandas as pd

from eqi_utils.data import view
import eqi_analysis.core.plot
from eqi_analysis.core.db.analysis import plot_coverage_graph
from .analysis import Benchmark, Factor, Portfolio


def analyze_alphalens(factor_df,
                      name,
                      benchmark=Benchmark.MSCI_US,
                      perf_map=None,
                      quantile=5,
                      clean_binning=False,
                      periods=('28D', '84D'),
                      show_performance=True,
                      long_short=False,
                      batch_mode=True,
                      price_name='close_month_start_by_RIC',
                      **kwargs):
    """
    Analyze a single factor with alphalens
    :param factor_df: factor Dataframe
    :param name: name of the factor
    :param benchmark: benchmark to use for performance comparison
    :param perf_map: map to store the computed performance
    :param quantile: number of quantiles to use for analysis
    :param clean_binning: whether to clean binning during analysis
    :param periods: look ahead periods to use
    :param show_performance: whether to show cumulative performance chart
    :param long_short: whether to build a long short portfolio
    :param batch_mode: whether to run the full performance analysis
    :return: Portfolio with performance analyzed by alphalens
    """
    factor = Factor(factor_df, 'RIC', name)

    factor.limit_by_index(benchmark)

    portfolio = Portfolio(factor, periods=periods)

    portfolio.join_price(price_name)

    portfolio.use_benchmark(benchmark)

    portfolio.to_alphalens_factor(quantile=quantile,
                                  clean_binning=clean_binning)

    portfolio.analyze_by_alphalens(long_short=long_short,
                                   show_performance=show_performance,
                                   batch_mode=batch_mode,
                                   **kwargs)
    if not batch_mode:
        plot_coverage_graph(portfolio.alphalens_factor,
                            portfolio._benchmark_name,
                            portfolio._factor)
    perf_df = portfolio._result_tables['perf_dfs']

    if batch_mode and perf_map is not None:
        for k, v in perf_df.items():
            v.columns = [name + '_' + str(col) if col != 'benchmark' else col
                         for col in v.columns]
            if k not in perf_map:
                perf_map[k] = [v]
            else:
                perf_map[k].append(v)

    return portfolio


def analyze_db(factor_df,
               name,
               benchmark=Benchmark.MSCI_US,
               quantile=5,
               clean_binning=False,
               price_name='close_month_start_by_RIC',
               periods=('28D', '84D'), **kwargs):
    factor = Factor(factor_df, 'RIC', name)

    factor.limit_by_index(benchmark)

    portfolio = Portfolio(factor, periods=periods)

    portfolio.join_price(price_name)

    portfolio.use_benchmark(benchmark)

    portfolio.to_alphalens_factor(quantile=quantile,
                                  clean_binning=clean_binning)

    portfolio.analyze_by_db(**kwargs)

    return portfolio


def multi_analyze_alphalens(factor_map,
                            benchmark=Benchmark.MSCI_US,
                            quantile=5,
                            clean_binning=False,
                            periods=('28D', '84D'),
                            show_performance=True,
                            long_short=False,
                            batch_mode=True):
    """
    Analyze multiple factors with alphalens
    :param factor_map: factor_name -> factor_dataframe map
    :param benchmark: benchmark to use for performance comparison
    :param quantile: number of quantiles to use for analysis
    :param clean_binning: whether to clean binning during analysis
    :param periods: look ahead periods to use
    :param show_performance: whether to show cumulative performance chart
    :param long_short: whether to build a long short portfolio
    :param batch_mode: whether to run the full performance analysis
    :return: Map of factor performances
    """
    perf_map = {}
    for name, factor in factor_map.items():
        analyze_alphalens(factor, name, benchmark=benchmark, perf_map=perf_map,
                          quantile=quantile, clean_binning=clean_binning,
                          periods=periods,
                          show_performance=show_performance,
                          long_short=long_short,
                          batch_mode=batch_mode)
    return perf_map


def plot_performance_chart(period, perf_map, benchmark_name=None, top_n=5,
                           asc=True):
    """
    Plot performance chart of multiple factors
    :param period: look ahead period to use
    :param perf_map: factor performance map
    :param benchmark_name: benchmark to use for performance comparison
    :param top_n: number of top factors to show
    :param asc: show best performing factors if True, False otherwise
    :return:
    """
    eqi_analysis.core.plot.set_plt_size()
    all_perf = pd.concat(
        [p_df.drop('benchmark', axis=1) for p_df in perf_map[period]], axis=1)
    all_perf['benchmark'] = perf_map[period][1]['benchmark']
    last_10_mean = [all_perf[col][-50:].mean() for col in all_perf.columns]
    if asc:
        top_5_cols = all_perf.columns[
            np.array(last_10_mean).argsort()[-top_n:][::-1]]
    else:
        top_5_cols = all_perf.columns[
            np.array(last_10_mean).argsort()[0:top_n + 1][::-1]]
    if 'benchmark' not in top_5_cols:
        top_5_cols = top_5_cols.insert(0, 'benchmark')
    title = 'Top {} Factors Performance Comparison' \
            ' against {}'.format(top_n, benchmark_name)
    all_perf[top_5_cols].plot(figsize=(25, 15), title=title, fontsize=20)

def refresh_datafile(name, user='default'):
    view.load_to_df(name, user=user, remote=True, force=True)