from eqi_utils.data import view


def to_return_index(dataframe, ticker_col='RIC_CD', date_col='MARKETDATE'):
    """
    Transform TRQA Return Index into EQI Factor format.
    :param dataframe: TRQA Return Index dataframe
    :param ticker_col: ticker column name
    :param date_col: date column name
    :return: TRQA Return Index in EQI Factor format
    """
    return (dataframe.to_eqi()
            .e_rename({ticker_col: 'asset', date_col: 'Date'})
            .e_select('Date', 'asset', 'RI')
            .e_set_index('Date', 'asset')
            .e_groupby('asset')
            .e_apply(
        lambda df: df.to_eqi().e_groupby('Date').sum().to_pandas())
            .unstack(0)
            .e_drop_level(0)
            .resample('d')
            .bfill()
            .sort_index()
            .to_pandas())


# TODO: Ticker matching and mapping utilities
_SUPPORTED_CODE_MAPPING = {}


def _map_code(from_code, to_code):
    if from_code not in _SUPPORTED_CODE_MAPPING or \
            _SUPPORTED_CODE_MAPPING[from_code] != to_code:
        raise AttributeError(
            "{} to {} mapping is not supported".format(from_code, to_code))


def to_index_weight(index_name='msci_us'):
    """
    Transfrom POP index holdings weight into EQI Factor format.
    :param index_name: index name
    :return:POP index holdings weight in EQI Factor format
    """
    holdings = view.load_to_df('{}_holding'.format(index_name), user='default',
                               remote=True)
    return (holdings.to_eqi()
            .e_notnull('PORTFOLIO_WEIGHT')
            .e_astype({'INSTRUMENT_ID': str})
            .e_set_index('AS_OF_DATE', 'INSTRUMENT_ID')
            .e_select('PORTFOLIO_WEIGHT')
            .e_rename({'AS_OF_DATE': 'date', 'INSTRUMENT_ID': 'asset'})
            .to_pandas())
