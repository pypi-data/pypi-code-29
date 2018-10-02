import json
from datetime import datetime

import pandas as pd
from alphalens import utils, interactive, tears
from eqi_utils.data import view

from eqi_analysis.core.utils import recompute_quantile, overlap_date
from . import entity
from . import refdata
from . import plot
from . import utils as analysis_utils
from .entity import access
from .db import analysis as db_analysis


class Benchmark:
    MSCI_US = 'MSCI_US'
    MSCI_WORLD = 'MSCI_WORLD'
    MSCI_ACWI = 'MSCI_ACWI'
    SPX = 'SPX'
    RUSSELL_3000 = 'RUSSELL_3000'


class Factor:
    """Timeseries factor indexed by asset and date."""

    def __init__(self, df, ticker_type, name):
        """
        Construct a new Factor
        :param df: factor DataFrame, which must meet the requirements: \
                - index exactly as ['date', 'asset']
                - no duplicated index
                - exactly one factor column, with any string name
        :param ticker_type: the ticker type of the asset, e.g. 'RIC' \
                            this will be used for various later stage refdata
                            fetching, e.g. price
        :param name: name of the factor
        """
        self.raw_df = df
        self.name = name
        self.ticker_type = ticker_type
        self._check_factor_index()
        self._check_dup_index()
        self._check_column_name()
        self.meta = self._get_meta()

    @staticmethod
    def from_registry(name):
        """
        Load an existing factor from database matching a given name
        :param name: factor name
        :return: existing Factor
        """
        factor = entity.access.get_factor(name)
        df = entity.access.load_to_df(name)
        return Factor(df, factor.ticker_type, factor.name)

    @staticmethod
    def list_registry():
        """
        List all factors from registry
        """
        entity.access.list_factors()

    @staticmethod
    def delete_from_registry(name):
        """
        Delete factor with a specific name from registry
        :param name:
        :return:
        """
        factor = entity.access.find_factors(name=name)
        if len(factor) == 1:
            factor = factor[0]
            entity.access.delete_factor(factor)
            view.delete_view(factor.name, remote=True)
        elif len(factor) == 0:
            raise ValueError("No factor found by name {}".format(name))
        else:
            raise ValueError("Too many results found by name {}".format(name))

    @staticmethod
    def search_registry(**kwargs):
        """
        Search for factors in the registry matching a criteria
        :param kwargs: field=value, e.g. name='my_factor'
        :return: a list of factors found
        """
        entity.access.list_factors(entity.access.find_factors(**kwargs))

    def upload_to_registry(self, desc):
        """
        Upload this factor to registry
        :param desc: factory description
        """
        view.save_view(self.raw_df, self.name, desc=desc, remote=True)
        eqifactor = entity.entity.EQIFactor(name=self.name, path=self.name,
                                            location='S3',
                                            ticker_type=self.ticker_type,
                                            owner=view.DEFAULT_USER,
                                            description=desc,
                                            creation_ts=datetime.now(),
                                            last_modified_ts=datetime.now())
        access.save_factor(eqifactor)

    def to_pop(self):
        pass

    def _get_meta(self):
        return {
            'min_date': self.raw_df.index.get_level_values(
                'date').min(),
            'max_date': self.raw_df.index.get_level_values(
                'date').max(),
            'tickers': self.raw_df.index.get_level_values(
                'asset').unique().values.tolist()
        }

    def _check_factor_index(self):
        names = self.raw_df.to_eqi().e_index_names()
        if names != ['date', 'asset']:
            raise AttributeError(
                "Expect factor raw DataFrame to have"
                "exact indexes like ['date, 'asset'], not {}, {}".format(
                    names[0], names[1]))

    def _check_dup_index(self):
        if self.raw_df.to_eqi().e_has_dup_index():
            raise AttributeError(
                "Factor raw DataFrame has duplicate index, "
                "please remove")

    def _check_column_name(self):
        if len(self.raw_df.columns) != 1:
            raise AttributeError(
                "Factor needs to contain exactly one value column, "
                "please adjust")
        self.raw_df = self.raw_df.rename(columns=lambda c: str(c))

    @staticmethod
    def _filter_by_index(df, index_holdings):
        df = df.copy()
        cur_date = df.to_eqi().e_unique('date').to_pandas()[0]
        ticker_set = index_holdings['ticker_set'].loc[cur_date]
        return (df.to_eqi()
                .e_drop_level('date')
                .e_in('asset', ticker_set)
                .to_pandas())

    def limit_by_index(self, index_name):
        index_holding = view.load_to_df(
            'index_holding_{}_by_rics'.format(index_name),
            remote=True,
            user='default')
        self.raw_df, index_holding = overlap_date(self.raw_df, index_holding)
        index_holding['ticker_set'] = index_holding['tickers'].apply(
            lambda s: set(json.loads(s)))
        self.raw_df = self.raw_df.groupby('date').apply(
            Factor._filter_by_index, index_holding)
        self.meta = self._get_meta()


class CategorizedFactor(Factor):
    """Factor with category information."""

    def __init__(self, categorized_df, ticker_type, name,
                 category_map=None):
        """
        Construct a new CategorizedFactor
        :param categorized_df: input DataFrame, which must meet requirements: \
                            - index exactly as ['date', 'asset', 'category']
                            - no duplicate index
                            - exactly one factor column, with string name
        :param ticker_type: the ticker type of the asset, e.g. 'RIC' \
                            this will be used for various later stage refdata
                            fetching, e.g. price
        :param name: factor name
        :param category_map: category id -> name map, optional
        """
        self.categorized_factor = categorized_df.to_eqi()
        self._check_category_df()
        combined_factor = categorized_df.groupby(level=['date', 'asset']).sum()
        super(CategorizedFactor, self).__init__(combined_factor, ticker_type,
                                                name)
        self.meta['categories'] = self.categorized_factor.e_to_set('category')
        self.meta['category_map'] = category_map

    def _check_category_df(self):
        names = self.categorized_factor.e_index_names()
        if names != ['date', 'asset', 'category']:
            raise AttributeError("Expect factor raw DataFrame to have exact "
                                 "indexes as ['date, 'asset', 'category']")

    @staticmethod
    def from_registry(name):
        factor = entity.access.get_factor(name)
        df = entity.access.load_to_df(name)
        return CategorizedFactor(df, factor.category_col_name,
                                 factor.ticker_type,
                                 factor.name)

    def iteritems(self):
        return ((x, self.categorized_factor.to_eqi().e_is('category',
                                                          x).e_drop_level(
            'category').to_pandas())
                for x in self.meta['categories'])


class Portfolio:
    """Timeseries asset holdings"""

    def __init__(self, factor, periods=('28D', '84D', '168D')):
        """
        Construct a Portfolio
        :param factor: Factor used as asset weighting
        :param periods: Forward period to compute return for analysis
        """
        self._factor = factor
        self._periods = periods
        self._period_timedelta = [pd.Timedelta(p) for p in periods]
        self._benchmark_name = None
        self._benchmark_return = None
        self._benchmark_price = None
        self._result_tables = None
        self._quantile = None
        self.price = None
        self.alphalens_factor = None
        self.alphalens_factors = None

    def publish_result(self):
        pass

    def join_price(self, price_type='return_index'):
        """
        Fetch the price data for portfolio holdings
        :param price_type: type of price, e.g. 'return_index'
        """
        self.price = refdata.fetch_price(self._factor.meta['tickers'],
                                         self._factor.meta['min_date'],
                                         self._factor.meta['max_date'],
                                         price_type,
                                         right_buf=max(self._period_timedelta)
                                         )

    @staticmethod
    def _to_factor_with_return(df, price, resample_period='',
                               quantile=3,
                               forward_periods=('28D', '84D', '168D'),
                               max_loss=1,
                               clean_binning=True,
                               **kwargs):
        clean_binning = False if resample_period else clean_binning
        alphalens_factor = \
            utils.get_clean_factor_and_forward_returns(
                df,
                price, quantiles=quantile, max_loss=max_loss,
                periods=forward_periods, clean_binning=clean_binning, **kwargs)
        if resample_period != '':
            alphalens_factor = Portfolio.resample(alphalens_factor,
                                                  resample_period)
        if not clean_binning:
            alphalens_factor = recompute_quantile(alphalens_factor,
                                                  quantile=quantile)
        return alphalens_factor.sort_index()

    def to_alphalens_factor(self, resample_period='', quantile=3, max_loss=1,
                            **kwargs):
        """
        Convert Factor into AlphaLens format (joined with forward return and \
        quantile)
        :param resample_period: {'month_start', 'month_end', ''}
        :param quantile: quantile to bin factor data
        :param max_loss: max data loss allowed during computation
        :param kwargs: additional AlphaLens kwargs
        """
        if self.price is None:
            raise AttributeError(
                "Price data has to be fetched first, "
                "please call portfolio.join_price()")
        self._quantile = quantile
        self.alphalens_factor = Portfolio._to_factor_with_return(
            self._factor.raw_df,
            self.price, resample_period=resample_period, quantile=quantile,
            max_loss=max_loss,
            forward_periods=self._periods, **kwargs
        )

        if isinstance(self._factor, CategorizedFactor):
            alphalens_factors = {}
            for category, factor_by_category in self._factor.iteritems():
                alphalens_factors[
                    category] = Portfolio._to_factor_with_return(
                    factor_by_category,
                    self.price, resample_period=resample_period,
                    quantile=quantile, max_loss=max_loss,
                    forward_periods=self._periods, **kwargs
                )
            self.alphalens_factors = alphalens_factors

    def analyze_by_alphalens(self, *args, **kwargs):
        """
        Analyze the Portfolio performance with AlphaLens
        :param args: additional AlphaLens positional args
        :param kwargs: additional AlphaLens kwargs
        """
        if self.alphalens_factor is None:
            raise AttributeError(
                "Alphalens factor needs to be computed first,"
                " please call portfolio.to_alphalens_factor()")
        is_by_group = 'group_by' in kwargs
        if isinstance(self._factor, CategorizedFactor):
            tears.create_full_tear_sheet_by_categories(
                self.alphalens_factor,
                self.alphalens_factors,
                by_group=is_by_group,
                category_map=self._factor.meta['category_map'], *args,
                **kwargs)
        else:
            self._result_tables = tears.create_full_tear_sheet(
                self.alphalens_factor,
                by_group=is_by_group,
                benchmark_return=self._benchmark_return,
                benchmark_name=self._benchmark_name,
                benchmark_price=self._benchmark_price,
                factor_name=self._factor.name,
                *args,
                **kwargs)

    def analyze_by_db(self, split_line_x=None):
        """
        Analyze the Portfolio performance in DB format
        :return:
        """
        if self.alphalens_factor is None:
            raise AttributeError(
                "Alphalens factor needs to be computed first,"
                " please call portfolio.to_alphalens_factor()")
        plot.set_plt_size()
        db_analysis.SPLIT_LINE_X = split_line_x
        db_analysis.plot_coverage_graph(self.alphalens_factor,
                                        self._benchmark_name,
                                        self._factor)
        raw_factor_quantiled = analysis_utils.recompute_quantile(
            self._factor.raw_df, self._quantile)
        db_analysis.plot_quantiles_boundary(raw_factor_quantiled, "Raw Factor")
        db_analysis.plot_quantiles_boundary(self.alphalens_factor,
                                            "Factor after Price Join")
        bi_splited = analysis_utils.bi_split(self.alphalens_factor)
        total_quantiles = analysis_utils.get_total_quantiles(
            self.alphalens_factor)
        q2_label = 'Quantile=2'
        qtotal_label = 'Quantile={}'.format(total_quantiles)
        for period in self._periods:
            db_analysis.plot_return_spread(self.alphalens_factor, period,
                                           desc=qtotal_label)
            db_analysis.plot_return_spread(bi_splited, period, desc=q2_label)
            db_analysis.plot_quantile_ann_return(self.alphalens_factor, period)
            db_analysis.plot_performance(self.alphalens_factor, period,
                                         desc=qtotal_label)
            db_analysis.plot_performance(bi_splited, period, desc=q2_label)
            db_analysis.plot_turnover(self.alphalens_factor, period,
                                      desc=qtotal_label)
            db_analysis.plot_turnover(bi_splited, period, desc=q2_label)

    def explore_quantile(self, period):
        interactive.create_composition_explorer(self._result_tables,
                                                self.alphalens_factor,
                                                self._benchmark_name, period)

    @staticmethod
    def to_month_end(df):
        return df.unstack(1).resample(
            'BM').last().stack(1)

    @staticmethod
    def to_month_start(df):
        return df.unstack(1).resample(
            'BMS').first().stack(1)

    @staticmethod
    def resample(df, period='month_end'):
        if period == 'month_end':
            return Portfolio.to_month_end(df)
        elif period == 'month_start':
            return Portfolio.to_month_start(df)
        else:
            raise AttributeError(
                'Period {} cannot be recognized'.format(period))

    def _to_benchmark_return(self):
        bench_return = utils.compute_forward_returns_benchmark(
            self._factor.raw_df,
            self._benchmark_price,
            periods=self._periods)
        bench_return.index = bench_return.index.droplevel('asset')
        return bench_return

    @staticmethod
    def _to_benchmark_price(name):
        return view.load_to_df("price_{}".format(name), remote=True,
                               user='default')

    def use_benchmark(self, name):
        if not name:
            self._benchmark_name = None
            self._benchmark_price = None
            self._benchmark_return = None
            return
        self._benchmark_name = name
        self._benchmark_price = Portfolio._to_benchmark_price(name)
        self._benchmark_return = self._to_benchmark_return()
