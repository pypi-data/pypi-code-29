import pandas as pd


def append_times(df, st, et):
    df.insert(0, 'START_TIME', st)
    df.insert(1, 'STOP_TIME', et)
    df = df.set_index(['START_TIME', 'STOP_TIME'])
    return df


def offset(df, offset_in_secs):
    df_copy = df.copy(deep=True)
    df_copy.index = df_copy.index + pd.DateOffset(seconds=offset_in_secs)
    return df_copy


def segment(df, start_time=None, stop_time=None, start_time_col=0,
            stop_time_col=None):
    if stop_time_col is None:
        stop_time_col = start_time_col
    if start_time is None:
        start_time = df.iloc[0, start_time_col]
    if stop_time is None:
        stop_time = df.iloc[-1, stop_time_col]

    if start_time_col == stop_time_col:
        mask = (df.iloc[:, start_time_col] >= start_time) & (
            df.iloc[:, stop_time_col] < stop_time)
        return df[mask].copy(deep=True)
    else:
        mask = (df.iloc[:, start_time_col] < stop_time) & (
            df.iloc[:, stop_time_col] > start_time)
        subset_df = df[mask].copy(deep=True)
        subset_df[subset_df.iloc[:, start_time_col] <
                  start_time].iloc[:, start_time_col] = start_time
        subset_df[subset_df.iloc[:, stop_time_col] >
                  stop_time].iloc[:, stop_time_col] = stop_time
        return subset_df


def segment_sensor(df, start_time=None, stop_time=None):
    return segment(df, start_time=start_time, stop_time=stop_time)


def segment_annotation(df, start_time=None, stop_time=None):
    return segment(df, start_time=start_time, stop_time=stop_time,
                   start_time_col=1, stop_time_col=2)


def start_time(df, start_time_col=0):
    return df.iloc[0, start_time_col]


def end_time(df, stop_time_col=0):
    return df.iloc[-1, stop_time_col]


def append_edges(df, before_df=None, after_df=None, duration=120,
                 start_time_col=0, stop_time_col=0):
    lbound_time = df.iloc[0, start_time_col]
    rbound_time = df.iloc[-1, stop_time_col]

    if before_df is not None:
        ledge_df = segment(before_df,
                           start_time=lbound_time -
                           pd.Timedelta(duration, unit='s'),
                           stop_time=lbound_time,
                           start_time_col=start_time_col,
                           stop_time_col=stop_time_col)
    else:
        ledge_df = pd.DataFrame()

    if after_df is not None:
        redge_df = segment(after_df,
                           start_time=rbound_time,
                           stop_time=rbound_time +
                           pd.Timedelta(duration, unit='s'),
                           start_time_col=start_time_col,
                           stop_time_col=stop_time_col)
    else:
        redge_df = pd.DataFrame()

    return pd.concat((ledge_df, df, redge_df))
