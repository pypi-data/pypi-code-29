from catalyst import run_algorithm
from catalyst.api import order_target, record, symbol, get_order, cancel_order
import pandas as pd


def initialize(context):
    # context.asset = symbol('btc_usdt')
    context.asset = symbol('etc_btc')
    context.i = 0

def handle_data(context, data):
    if not context.blotter.open_orders:
        if context.portfolio.positions and context.portfolio.positions[context.asset].amount > 0.5:
            id = order_target(context.asset, 0, limit_price=(data.current(context.asset, 'price')+0.10013))
        else:
            id = order_target(context.asset, 1, limit_price=(data.current(context.asset, 'price')-0.00103))


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
            algo_namespace='issue_367',
            quote_currency='btc',
            live=True,
            simulate_orders=False,
            # start=pd.to_datetime('2018-05-01 17:18', utc=True),
            # end=pd.to_datetime('2018-05-14 08:28', utc=True),
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
