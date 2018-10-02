from datetime import datetime
from eqi_utils.data import bundle, view
from eqi_utils.data import utils
from .entity import access
from .entity import entity
import pandas as pd


def list_available_prices():
    bundle.list_datafile_desc('price')


def fetch_price(tickers,
                start_date=None,
                end_date=None,
                price_name='close_month_start_by_RIC',
                left_buf=pd.Timedelta(0),
                right_buf=pd.Timedelta(365, unit='d')):
    """
    Return price dataframe
    :param tickers: tickers to fetch price for
    :param start_date: start date condition, optional
    :param end_date: end date limit, optional
    :param price_name: name of price to use.
    :param left_buf: timedelta before start to fetch price for
    :param right_buf: timedelta after end to fetch price for
    :return: price dataframe
    """

    def strftime(t):
        return t.strftime('%d-%b-%Y') if t is not pd.NaT else None

    if price_name in bundle.get_datafiles('price'):
        # For officially supported price data
        price_df = bundle.load_to_df('price', price_name, columns=tickers)
    else:
        # For user customized price data
        price_df = view.load_to_df(price_name, columns=tickers)

    if start_date is not None or end_date is not None:
        effective_start = strftime(start_date - left_buf)
        effective_end = strftime(end_date + right_buf)
        return price_df.to_eqi().e_between('Date',
                                           effective_start,
                                           effective_end).to_pandas()
    else:
        return price_df


def fetch_index_holdings(name):
    return view.load_to_df('index_holding_{}_by_rics'.format(name),
                           user='default', remote='True')


def load_to_df(name, tickers=None, start_date=None, end_date=None):
    """
    Return EQI refdata into a Pandas dataframe
    :param name: EQIRefData name
    :param tickers: tickers to fetch the refdata for, optional
    :param start_date: start date condition, optional
    :param end_date: end date condition, optional
    :return: dataframe of EQI refdata
    """
    return access.load_to_df(name, source_type=entity.REFDATA_TYPE,
                             tickers=tickers, start_date=start_date,
                             end_date=end_date)


def list_refdata():
    """
    Print all the refdata available
    :return:
    """
    access.list_refdata()


def save_refdata_s3(df, name, desc, ticker_type, as_admin=False):
    """
    Upload refdata to s3, and register in registry
    :param df: refdata dataframe
    :param name: refdata name
    :param desc: refdata description
    :param ticker_type: refdata ticker type
    :param as_admin: whether to save as admin
    :return:
    """
    if as_admin:
        utils.authenticate_admin()
        view.save_view_as_admin(df, name, desc, remote=True)
    else:
        view.save_view(df, name, desc, remote=True)
    user = 'default' if as_admin else view.DEFAULT_USER
    eqirefdata = entity.EQIRefData(name=name, path=name,
                                   location='S3',
                                   ticker_type=ticker_type,
                                   owner=user,
                                   description=desc,
                                   creation_ts=datetime.now(),
                                   last_modified_ts=datetime.now())
    access.save_refdata(eqirefdata)


def save_refdata_oracle(name, desc, ticker_type, query, ticker_col_name=None,
                        date_col_name=None, as_admin=False):
    """
    Register refdata in the registry with SQL query
    :param name: refdata name
    :param desc: refdata description
    :param ticker_type: refdata ticker type
    :param query: query to use for fetching the refdata
    :param ticker_col_name: ticker attribute name, optional
    :param date_col_name: date attribute name, optional
    :param as_admin: whether to save as admin
    :return:
    """
    if as_admin:
        utils.authenticate_admin()
    user = 'default' if as_admin else view.DEFAULT_USER
    eqirefdata = entity.EQIRefData(name=name, path=query,
                                   location='ORACLE',
                                   ticker_type=ticker_type,
                                   owner=user,
                                   description=desc,
                                   creation_ts=datetime.now(),
                                   last_modified_ts=datetime.now(),
                                   ticker_col_name=ticker_col_name,
                                   date_col_name=date_col_name)
    access.save_refdata(eqirefdata)


def save_refdata(refdata):
    """
    Register refdata in the registry
    :param refdata: refdata to register
    :return:
    """
    access.save_refdata(refdata)


def delete_refdata(name):
    """
    Delete refdata from registry
    :param name: refdata name
    :return:
    """
    refdata = get_refdata(name)
    access.delete_refdata(refdata)


def get_refdata(name):
    """
    Get refdata by name
    :param name: refdata name
    :return: refdata with given name
    """
    return access.get_refdata(name)


def find_refdata(**kwargs):
    """
    Find EQIRefData by criteria
    :param kwargs: criteria, e.g. name='my_refdata'
    :return: a list of refdata found
    """
    return access.find_refdata(**kwargs)
