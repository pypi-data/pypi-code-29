import pandas as pd


def is_freq_day(df):
    freq = df.index.get_level_values('date').freq
    return freq is not None and freq.freqstr in {'B', 'C', 'D'}


def to_daily(df):
    if not is_freq_day(df):
        df = df.groupby(level=[1]).apply(
            lambda df_: df_.to_eqi().e_drop_level('asset').resample(
                'D').bfill().to_pandas()).swaplevel(0, 1).sort_index()
    return df


def recompute_quantile(df, quantile=5, by_group=False):
    def _to_quantile(df_, quantile_):
        return pd.qcut(df_.rank(method='first'),
                       quantile_,
                       labels=False) + 1

    grouper = [df.index.get_level_values('date')]
    if by_group:
        grouper.append('group')

    factor_quantile = df.groupby(grouper)['factor'] \
        .apply(_to_quantile, quantile)
    df['factor_quantile'] = factor_quantile
    return df


def overlap_date(df1, df2):
    def _min(df):
        return df.index.get_level_values('date').min()

    def _max(df):
        return df.index.get_level_values('date').max()

    def _truncate(df):
        return df.to_eqi().e_between('date', start_date, end_date).to_pandas()

    start_date = max(_min(df1), _min(df2))
    end_date = min(_max(df1), _max(df2))
    return _truncate(df1), _truncate(df2)


def bi_split(alphalens_factor):
    return alphalens_factor.groupby(['date']).apply(
        lambda df: recompute_quantile(df, quantile=2)).dropna()


def get_total_quantiles(alphalens_factor):
    return len(alphalens_factor['factor_quantile'].unique())
