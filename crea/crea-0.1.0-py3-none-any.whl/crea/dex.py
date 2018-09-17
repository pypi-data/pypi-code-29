import random

from creabase import transactions, operations
from creabase.storage import configStorage as config

from .amount import Amount
from .instance import shared_cread_instance


class Dex(object):
    """ This class allows to access calls specific for the internal
        exchange of CREA.

        :param Cread cread_instance: Cread() instance to use when
        accessing a RPC

    """
    assets = ["CREA", "CBD"]

    def __init__(self, cread_instance=None):
        self.cread = cread_instance or shared_cread_instance()

    def _get_asset(self, symbol):
        """ Return the properties of the assets tradeable on the
            network.

            :param str symbol: Symbol to get the data for (i.e. CREA, CBD,
            VESTS)

        """
        if symbol == "CREA":
            return {"symbol": "CREA", "precision": 3}
        elif symbol == "CBD":
            return {"symbol": "CBD", "precision": 3}
        elif symbol == "VESTS":
            return {"symbol": "VESTS", "precision": 6}
        else:
            return None

    def _get_assets(self, quote):
        """ Given the `quote` asset, return base. If quote is CBD, then
            base is CREA and vice versa.
        """
        assets = self.assets.copy()
        assets.remove(quote)
        base = assets[0]
        return self._get_asset(quote), self._get_asset(base)

    def get_ticker(self):
        """ Returns the ticker for all markets.

            Output Parameters:

            * ``latest``: Price of the order last filled
            * ``lowest_ask``: Price of the lowest ask
            * ``highest_bid``: Price of the highest bid
            * ``cbd_volume``: Volume of CBD
            * ``crea_volume``: Volume of CREA
            * ``percent_change``: 24h change percentage (in %)

            .. note::

                Market is CREA:CBD and prices are CBD per CREA!

            Sample Output:

            .. code-block:: js

                 {'highest_bid': 0.30100226633322913,
                  'latest': 0.0,
                  'lowest_ask': 0.3249636958897082,
                  'percent_change': 0.0,
                  'cbd_volume': 108329611.0,
                  'crea_volume': 355094043.0}


        """
        t = self.cread.get_ticker()
        return {
            'highest_bid': float(t['highest_bid']),
            'latest': float(t["latest"]),
            'lowest_ask': float(t["lowest_ask"]),
            'percent_change': float(t["percent_change"]),
            'cbd_volume': Amount(t["cbd_volume"]),
            'crea_volume': Amount(t["crea_volume"])
        }

    def trade_history(self, time=1 * 60 * 60, limit=100):
        """ Returns the trade history for the internal market

            :param int time: Show the last x seconds of trades (default 1h)
            :param int limit: amount of trades to show (<100) (default: 100)
        """
        assert limit <= 100, "'limit' has to be smaller than 100"
        return self.cread.get_trade_history(
            transactions.fmt_time_from_now(-time),
            transactions.fmt_time_from_now(),
            limit,
        )

    def market_history_buckets(self):
        return self.cread.get_market_history_buckets()

    def market_history(
            self,
            bucket_seconds=60 * 5,
            start_age=1 * 60 * 60,
            end_age=0,
    ):
        """ Return the market history (filled orders).

            :param int bucket_seconds: Bucket size in seconds (see
            `returnMarketHistoryBuckets()`)

            :param int start_age: Age (in seconds) of the start of the
            window (default: 1h/3600)

            :param int end_age: Age (in seconds) of the end of the window
            (default: now/0)

            Example:

            .. code-block:: js

                 {'close_cbd': 2493387,
                  'close_crea': 7743431,
                  'high_cbd': 1943872,
                  'high_crea': 5999610,
                  'id': '7.1.5252',
                  'low_cbd': 534928,
                  'low_crea': 1661266,
                  'open': '2016-07-08T11:25:00',
                  'open_cbd': 534928,
                  'open_crea': 1661266,
                  'cbd_volume': 9714435,
                  'seconds': 300,
                  'crea_volume': 30088443},
        """
        return self.cread.get_market_history(
            bucket_seconds,
            transactions.fmt_time_from_now(-start_age - end_age),
            transactions.fmt_time_from_now(-end_age),
        )

    def buy(self,
            amount,
            quote_symbol,
            rate,
            expiration=7 * 24 * 60 * 60,
            killfill=False,
            account=None,
            order_id=None):
        """ Places a buy order in a given market (buy ``quote``, sell
            ``base`` in market ``quote_base``). If successful, the
            method will return the order creating (signed) transaction.

            :param number amount: Amount of ``quote`` to buy

            :param str quote_symbol: CREA, or CBD

            :param float price: price denoted in ``base``/``quote``

            :param number expiration: (optional) expiration time of the
            order in seconds (defaults to 7 days)

            :param bool killfill: flag that indicates if the order shall be
            killed if it is not filled (defaults to False)

            :param str account: (optional) the source account for the
            transfer if not ``default_account``

            :param int order_id: (optional) a 32bit orderid for tracking of
            the created order (random by default)

            Prices/Rates are denoted in 'base', i.e. the CREA:CBD market
            is priced in CBD per CREA.
        """
        if not account:
            if "default_account" in config:
                account = config["default_account"]
        if not account:
            raise ValueError("You need to provide an account")

        # We buy quote and pay with base
        quote, base = self._get_assets(quote=quote_symbol)
        op = operations.LimitOrderCreate(
            **{
                "owner":
                    account,
                "orderid":
                    order_id or random.getrandbits(32),
                "amount_to_sell":
                    '{:.{prec}f} {asset}'.format(
                        amount * rate,
                        prec=base["precision"],
                        asset=base["symbol"]),
                "min_to_receive":
                    '{:.{prec}f} {asset}'.format(
                        amount, prec=quote["precision"], asset=quote["symbol"]),
                "fill_or_kill":
                    killfill,
                "expiration":
                    transactions.fmt_time_from_now(expiration)
            })
        return self.cread.commit.finalizeOp(op, account, "active")

    def sell(self,
             amount,
             quote_symbol,
             rate,
             expiration=7 * 24 * 60 * 60,
             killfill=False,
             account=None,
             orderid=None):
        """ Places a sell order in a given market (sell ``quote``, buy
            ``base`` in market ``quote_base``). If successful, the
            method will return the order creating (signed) transaction.

            :param number amount: Amount of ``quote`` to sell

            :param str quote_symbol: CREA, or CBD

            :param float price: price denoted in ``base``/``quote``

            :param number expiration: (optional) expiration time of the
            order in seconds (defaults to 7 days)

            :param bool killfill: flag that indicates if the order shall be
            killed if it is not filled (defaults to False)

            :param str account: (optional) the source account for the
            transfer if not ``default_account``

            :param int orderid: (optional) a 32bit orderid for tracking of
            the created order (random by default)

            Prices/Rates are denoted in 'base', i.e. the CREA:CBD market
            is priced in CBD per CREA.
        """
        if not account:
            if "default_account" in config:
                account = config["default_account"]
        if not account:
            raise ValueError("You need to provide an account")
        # We buy quote and pay with base
        quote, base = self._get_assets(quote=quote_symbol)
        op = operations.LimitOrderCreate(
            **{
                "owner":
                    account,
                "orderid":
                    orderid or random.getrandbits(32),
                "amount_to_sell":
                    '{:.{prec}f} {asset}'.format(
                        amount, prec=quote["precision"], asset=quote["symbol"]),
                "min_to_receive":
                    '{:.{prec}f} {asset}'.format(
                        amount * rate,
                        prec=base["precision"],
                        asset=base["symbol"]),
                "fill_or_kill":
                    killfill,
                "expiration":
                    transactions.fmt_time_from_now(expiration)
            })
        return self.cread.commit.finalizeOp(op, account, "active")

    def cancel(self, orderid, account=None):
        """ Cancels an order you have placed in a given market.

            :param int orderid: the 32bit orderid

            :param str account: (optional) the source account for the
            transfer if not ``default_account``

        """
        if not account:
            if "default_account" in config:
                account = config["default_account"]
        if not account:
            raise ValueError("You need to provide an account")

        op = operations.LimitOrderCancel(**{
            "owner": account,
            "orderid": orderid,
        })
        return self.cread.commit.finalizeOp(op, account, "active")
