import calendar

import numpy as np
from IPython.core.display import display
from ipywidgets import interactive

from alphalens import plotting
import matplotlib.pyplot as plt
import inspect


def _drop_date(df):
    df.index = df.index.droplevel('date')
    return df


def _reindex_perf(perf, idx):
    return perf[perf.index >= idx].divide(perf.loc[idx])


def create_composition_explorer(result_tables,
                                alphalens_factor,
                                benchmark_name,
                                period):
    top_quantile = result_tables['top_quantile']
    bottom_quantile = result_tables['bottom_quantile']
    combined_dfs = result_tables['perf_dfs']
    weighted_returns = result_tables['weighted_returns']
    dates = combined_dfs[period].index.values

    def composition_explorer_func(factor_date):
        combined_df = combined_dfs[period]
        target_index_idx = np.searchsorted(combined_df.index.values,
                                           factor_date)
        target_index = combined_df.index.values[target_index_idx]
        prev_target_index = combined_df.index.values[
            target_index_idx - 1] if target_index_idx != 0 else None
        is_initial_view = prev_target_index is None
        if is_initial_view:
            return
        fig, axes = plt.subplots(4, 1, figsize=(20, 7 * 4))
        ax_itr = iter(axes)
        ax = next(ax_itr)
        plotting.plot_performance_comparison(combined_df,
                                             benchmark_name,
                                             period,
                                             ax=ax)
        perfs = combined_df.loc[target_index]
        info = """Top={:6.2f}\nBottom={:6.2f}\nBenchmark={:6.2f}""".format(
            perfs['factor_top_quantile'],
            perfs['factor_bottom_quantile'],
            perfs['benchmark'])
        ax.axvline(x=target_index, color='red', linestyle='-.', alpha=0.5)
        ax.text(0.05, 0.95, info, transform=ax.transAxes, fontsize=14,
                verticalalignment='top',
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.5))

        ax = next(ax_itr)
        plotting.plot_performance_comparison(
            _reindex_perf(combined_df, factor_date),
            benchmark_name,
            period,
            ax=ax,
            title_suffix="starting at {}".format(factor_date))

        for quantile in (top_quantile, bottom_quantile):
            plot_contribution_chart(alphalens_factor,
                                    weighted_returns,
                                    prev_target_index,
                                    quantile, period, ax_itr)

    p = interactive(composition_explorer_func,
                    factor_date=dates)
    display(p)


def get_month_start_end(year, month):
    return calendar.monthrange(year, month)


def plot_contribution_chart(alphalens_factor,
                            weighted_returns,
                            factor_date,
                            quantile, period,
                            ax_itr):
    factor_sum = (
            alphalens_factor.to_eqi()
            .e_is('date', factor_date)
            .e_select('factor')
            .sum()
            .to_pandas().iloc[0, 0]
    )

    quantile_sum = (
            alphalens_factor.to_eqi()
            .e_is('date', factor_date)
            .e_is('factor_quantile', quantile)
            .e_select('factor')
            .sum()
            .to_pandas().iloc[0, 0]
    )

    weighted_return = (weighted_returns.to_eqi()
                       .e_is('date', factor_date)
                       .e_is('factor_quantile', quantile)
                       .e_select(period)
                       .multiply(1 * factor_sum / quantile_sum)
                       .to_pandas()
                       )

    total_inst = len(weighted_return)
    expected_return = weighted_return.sum()[period]
    template = """# Equities = {}
                Expected return = {:2.2f}"""

    info = template.format(total_inst, expected_return)
    info = inspect.cleandoc(info)

    contribution_df = weighted_return.sort_values(by=[period], ascending=False)
    contribution_df.index = contribution_df.index.droplevel('date')
    num = 10
    contribution_top = contribution_df[:min(num, total_inst)]
    contribution_bottom = contribution_df[max(-num, -total_inst):]

    ax = next(ax_itr)
    ax.barh(contribution_top.index.values, contribution_top[period].tolist(),
            label='Top growth contributors '
                  'quantile {}'.format(quantile), color='green')
    ax.barh(contribution_bottom.index.values,
            contribution_bottom[period].tolist(),
            label='Bottom growth contributors '
                  'quantile {}'.format(quantile), color='red')
    ax.set_title('Growth contributors for quantile {}'.format(quantile))
    ax.text(0.05, 0.95, info, transform=ax.transAxes, fontsize=14,
            verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.5))

    ax.legend()
    ax.grid(True)
