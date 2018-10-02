import functools

from eqi_utils.data import dbview
from eqi_utils.data import utils
from eqi_utils.data import view
from . import connection
from . import entity


def session_aware(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        session = connection.DB_CONNECTION.get_session()
        try:
            return func(session, *args, **kwargs)
        finally:
            session.close()

    return wrapper


@session_aware
def find_factors(session, **kwargs):
    """
    Find factors based on criteria
    :param session: DB session to use
    :param kwargs: criteria, e.g. name='my_factor'
    :return: a list of factors found
    """
    return session.query(entity.EQIFactor).filter_by(**kwargs).all()


@session_aware
def get_all_factors(session):
    """
    Return a list of all the existing factors from the DB
    :param session: DB session to use
    :return: a list of existing factors
    """
    return session.query(entity.EQIFactor).all()


@session_aware
def get_factor(session, name):
    """
    Get one single factor by name
    :param session: DB session to use
    :param name: factor name
    :return: factor found
    """
    return session.query(entity.EQIFactor).filter_by(name=name).first()


def _pprint_factors(factors):
    rows = []
    for factor in factors:
        rows.append(factor.to_list())


@session_aware
def get_all_refdata(session):
    """
    Return all the existing refdata from the DB
    :param session: DB session to use
    :return: a list of all existing refdata
    """
    return session.query(entity.EQIRefData).all()


@utils.print_as_df(
    columns=['ID', 'Name', 'Description', 'Location', 'Owner', 'Last Modified',
             'Ticker Type'])
def list_factors(factors=None):
    """
    Print factors in a table
    :param factors: factors to print
    """
    # Make sure get_all_factors are not called at module load time
    if factors is None:
        factors = get_all_factors()
    return {factor.id: factor.to_list() for factor in factors}


@utils.print_as_df(
    columns=['ID', 'Name', 'Description', 'Location', 'Owner', 'Last Modified',
             'Ticker Type'])
def list_refdata(refdatas=None):
    """
    Print refdata in a table
    :param refdatas: refdata to print
    """
    # Make sure get_all_refdata are not called at module load time
    if refdatas is None:
        refdatas = get_all_refdata()
    return {refdata.id: refdata.to_list() for refdata in refdatas}


@session_aware
def save_factor(session, factor):
    """
    Save a factor to DB
    :param session: DB session to use
    :param factor: factor to save
    """
    session.add(factor)
    session.commit()


@session_aware
def delete_factor(session, factor):
    """
    Delete a factor from DB
    :param session: DB session to use
    :param factor: factor to delete
    """
    if factor.owner == view.DEFAULT_USER:
        session.delete(factor)
        session.commit()
    else:
        raise UserWarning(
            "You are not allowed to delete factors from other people")

@session_aware
def delete_refdata(session, refdata):
    """
    Delete refdata from DB
    :param session: DB session to use
    :param refdata: refdata to delete
    """
    if refdata.owner == view.DEFAULT_USER:
        session.delete(refdata)
        session.commit()
    else:
        raise UserWarning(
            "You are not allowed to delete refdata from other people")

@session_aware
def find_refdata(session, **kwargs):
    """
    Find refdata from DB by criteria
    :param session: DB session to use
    :param kwargs: criteria, e.g. name='return_index'
    """
    return session.query(entity.EQIRefData).filter_by(**kwargs).all()


@session_aware
def get_refdata(session, name):
    """
    Get refdata from DB by name
    :param session: DB session to use
    :param name: name of the refdata
    :return: refdata with name
    """
    return session.query(entity.EQIRefData).filter_by(name=name).first()


@session_aware
def save_refdata(session, refdata):
    """
    Save refdata to the DB
    :param session: DB session to use
    :param refdata: refdata to save
    """
    session.add(refdata)
    session.commit()


def _parse_s3_path(path):
    parts = path.split(r':')
    if len(parts) < 2:
        raise AttributeError(
            "Path {} is not a valid S3 path, abort".format(path))
    return parts[0], parts[1]


def _quote(string):
    return "'{}'".format(string)


def _to_date(string):
    return "to_date('{}')".format(string)


def _to_sql_conditions(eqidata, tickers, start_date, end_date):
    conditions = []
    if tickers is not None:
        conditions.append('{} in ({})'.format(_ticker_col(eqidata),
                                              ','.join([_quote(t) for t in
                                                        tickers])))
    if start_date:
        conditions.append(
            '{} >= {}'.format(eqidata.date_col_name, _to_date(start_date)))
    if end_date:
        conditions.append(
            '{} <= {}'.format(eqidata.date_col_name, _to_date(end_date)))
    return ' and '.join(conditions)


def _load_sql_to_df(eqidata, tickers, start_date, end_date):
    batch_size = 1000
    if tickers is not None and len(tickers) > batch_size:
        tickers_len = len(tickers)
        dataframe = None
        idx = 0
        while idx < len(tickers):
            tickers_to_fetch = tickers[idx: min(idx + batch_size, tickers_len)]
            cond = _to_sql_conditions(eqidata, tickers_to_fetch, start_date,
                                      end_date)
            sql_statement = "{} where {}".format(eqidata.path, cond)
            df = dbview.load_to_df(sql_statement)
            if not dataframe:
                dataframe = df
            else:
                dataframe.append(df)
            idx += batch_size
        return dataframe
    else:
        sql_statement = "{} where {}".format(eqidata.path,
                                             _to_sql_conditions(eqidata,
                                                                tickers,
                                                                start_date,
                                                                end_date))
        return dbview.load_to_df(sql_statement)

def _ticker_col(eqidata):
    return eqidata.ticker_col_name if eqidata.ticker_col_name else 'asset'

def _date_col(eqidata):
    return eqidata.date_col_name if eqidata.date_col_name else 'date'

def _filter_df(df, eqidata, tickers, start_date, end_date):
    eqidf = df.to_eqi()
    if tickers is not None:
        eqidf.e_in(_ticker_col(eqidata), tickers)
    if start_date:
        eqidf.e_greater_than(_date_col(eqidata), start_date)
    if end_date:
        eqidf.e_less_than(_date_col(eqidata), end_date)
    return eqidf.to_pandas()


def load_to_df(name, source_type=entity.FACTOR_TYPE, tickers=None,
               start_date=None, end_date=None):
    """
    Load either a EQIFactor or EQIRefData into a dataframe.
    :param name: name of the EQIFactor or EQIRefData
    :param source_type: {FACTOR_TYPE, FACTOR_TYPE}
    :param tickers: tickers used to filter the result
    :param start_date: start date used to filter the result
    :param end_date: end date used to filter the result
    :return: dataframe loaded from either a EQIFactor or EQIRefData
    """
    def _has_query():
        return (tickers is not None or
                start_date is not None or
                end_date is not None)

    if source_type == entity.FACTOR_TYPE:
        data = get_factor(name)
    elif source_type == entity.REFDATA_TYPE:
        data = get_refdata(name)
    else:
        raise AttributeError("Type {} is unknown".format(source_type))
    if data.is_s3():
        username = data.owner if data.owner else 'default'
        df = view.load_to_df(data.path, user=username, remote=True)
        if _has_query():
            df = _filter_df(df, data, tickers, start_date, end_date)
        return df
    elif data.is_oracle():
        if not _has_query():
            return dbview.load_to_df(data.path)
        else:
            return _load_sql_to_df(data, tickers, start_date, end_date)
    else:
        raise AttributeError("Location {} is unknown".format(data.location))
