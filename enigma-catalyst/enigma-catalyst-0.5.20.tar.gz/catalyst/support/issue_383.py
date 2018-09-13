from catalyst import run_algorithm
from catalyst.api import order_target, record, symbol, order, order_target_percent, set_commission
import pandas as pd


def initialize(context):
    context.asset = symbol('xrp_btc')
    context.i = 0


def handle_data(context, data):
    if not context.blotter.open_orders:
        if context.portfolio.positions and context.portfolio.positions[context.asset].amount >= 2 :
            order(context.asset, -2, limit_price=(data.current(context.asset, 'price')))
        else:
            order(context.asset, 3, limit_price=(data.current(context.asset, 'price')+0.00000001))

    record(btc=data.current(context.asset, 'price'))


if __name__ == '__main__':
    live = True
    if live:
        run_algorithm(
            capital_base=0.02,
            data_frequency='daily',
            initialize=initialize,
            handle_data=handle_data,
            exchange_name='poloniex',
            algo_namespace='buy_btc_simple',
            quote_currency='btc',
            live=True,
            simulate_orders=False,
        )
    else:
        run_algorithm(
                capital_base=100000,
                data_frequency='daily',
                initialize=initialize,
                handle_data=handle_data,
                exchange_name='poloniex',
                algo_namespace='buy_btc_simple',
                quote_currency='usdt',
                start=pd.to_datetime('2016-01-01', utc=True),
                end=pd.to_datetime('2016-01-03', utc=True),
            )
