# coding=utf-8
from __future__ import unicode_literals, print_function, absolute_import

from nf.constant import CSDK_OPERATE_SUCCESS, ERR_INVALID_PARAMETER

from nf.api.basic import _error_call_back, _check_frequency

from nf.csdk.c_sdk import (py_nfi_place_order, py_nfi_get_unfinished_orders,
                           py_nfi_get_orders, py_nfi_cancel_all_orders,
                           py_nfi_get_execution_reports_intraday, py_nfi_get_orders_intraday,
                           py_nfi_get_unfinished_orders_intraday,
                           py_nfi_cancel_order,
                           py_nfi_get_execution_reports, py_nfi_get_positions,
                           py_nfi_get_instruments,
                           py_nfi_get_symbols_by_fc, py_nfi_get_symbols_by_front,
                           py_nfi_get_symbol_of_coins, py_nfi_get_symbol,
                           py_nfi_get_all_symbols_of_coin,
                           py_nfi_history_ticks, py_nfi_history_bars,
                           py_nfi_history_ticks_n, py_nfi_history_bars_n,
                           py_nfi_get_exchange_rate, py_nfi_get_market_depth,
                           nfi_now)

from nf.enum import OrderType_Limit, OrderType_Market, OrderQualifier_Unknown, OrderDuration_Unknown, \
    MODE_BACKTEST, OrderStyle_Volume, OrderStyle_Value, OrderStyle_Percent, \
    OrderStyle_TargetVolume, OrderStyle_TargetValue, OrderStyle_TargetPercent
from nf.model.storage import Context
from nf.pb.core.api.account_pb2 import Order, Orders, ExecRpts, Positions, ExchangeRateList
from nf.pb.trade.api.trade.service_pb2 import (GetUnfinishedOrdersReq,
                                               GetOrdersReq, GetExecrptsReq, PlaceOrderReq, GetPositionsReq,
                                               SearchCoinPairsRsp, CancelOrderReq)

from nf.pb.data.api.data_pb2 import Ticks, Bars, DethpRateLists

from nf.pb_to_dict import protobuf_to_dict, dict_to_protobuf
from nf.utils import load_to_list, dict_fields_filter, takePriceFromDepth, load_to_datetime_str

from nf.pb.data.api.data_pb2 import InstrumentInfos
from nf.pb.core.api.common_pb2 import CommSymbolInfo
import pandas as pd

context = Context()


def _place_order(**kwargs):
    order = Order()

    for key in kwargs:
        setattr(order, key, kwargs[key])
        if context.mode == MODE_BACKTEST:
            order.created_at.seconds = nfi_now()    #get timestamp from csdk

    place_order_req = PlaceOrderReq()

    place_order_req.orders.extend([order])
    req = place_order_req.SerializeToString()
    status, result = py_nfi_place_order(req)

    if not status == CSDK_OPERATE_SUCCESS:
        _error_call_back(status)
        return []

    if not result:
        return []

    res = Orders()
    res.ParseFromString(result)

    return [protobuf_to_dict(res_order, including_default_value_fields=True) for
            res_order in res.data]


def order_volume(symbol, volume, side, order_type, position_effect=0,
                 order_duration=0, order_qualifier=0,
                 account = '', price=0):
    """
    按指定量委托
    """
    if not symbol or not volume or not side or not order_type or len(symbol) <= 0:
        raise TypeError('order_volume() : argument missing or incorrect argument type.')

    if order_type == OrderType_Limit and price <= 0:
        raise TypeError('order_volume() : argument error, whit price <= 0 for order type \'OrderType_Limit\'.')

    account_id = ''
    account_name = ''

    order_src = 2  # sdk
    return _place_order(symbol=symbol, volume=volume, value=-1,     #when place an order by volume, 'value' should be set to a negtive number
                        side=side, account_id=account_id,
                        account_name=account_name, price=price,
                        order_type=order_type, order_src=order_src)


def order_value(symbol, value, side, order_type, position_effect=0,
                 order_duration=0, order_qualifier=0,
                 account='', price=0):
    """
    按指定价委托
    """
    if not symbol or not value or not side or not order_type or len(symbol) <= 0:
        raise TypeError('order_value() : argument missing or incorrect argument type.')

    if order_type == OrderType_Limit and price <= 0:
        raise TypeError('order_value() : argument error, whit price <= 0 for order type \'OrderType_Limit\'.')

    account_id = ''
    account_name = ''

    order_src = 2  # sdk
    return _place_order(symbol=symbol, value=value, volume=-1,  #when place an order by volume, 'value' should be set to a negtive number
                        side=side, account_id=account_id,
                        account_name=account_name, price=price,
                        order_type=order_type, order_src=order_src)


def order_batch(orders, combine=False, account=''):
    orders = load_to_list(orders)

    place_order_req = PlaceOrderReq()
    try:
        for order in orders:
            pb_order = Order()
            if 'created_at' in order.keys():
                order.pop('created_at')
            if 'updated_at' in order.keys():
                order.pop('updated_at')
            order["order_src"] = 2  # 对于自己组的orders，order_src 必须设置上
            pb_order = dict_to_protobuf(pb_klass_or_instance=pb_order, values=order, ignore_none=True)
            place_order_req.orders.extend([pb_order])
    except TypeError:
        raise TypeError('order_batch() : argument missing or incorrect argument type.')
        return []

    req = place_order_req.SerializeToString()
    status, result = py_nfi_place_order(req)

    if not status == CSDK_OPERATE_SUCCESS:
        _error_call_back(status)
        return []

    if not result:
        return []

    res = Orders()
    res.ParseFromString(result)

    return [protobuf_to_dict(res_order, including_default_value_fields=True) for
            res_order in res.data]


def get_unfinished_orders(exchange=None):
    """
    查询所有未结委托
    """
    req = GetUnfinishedOrdersReq()
    if exchange:
        exchange = exchange.upper()
        req.exchange = exchange

    req = req.SerializeToString()
    status, result = py_nfi_get_unfinished_orders(req)
    if not status == CSDK_OPERATE_SUCCESS:
        _error_call_back(status)
        return []

    res = Orders()
    res.ParseFromString(result)

    orders = [protobuf_to_dict(res_order, including_default_value_fields=True) for res_order in res.data]

    if not exchange:
        return orders
    else:
        orders = [order for order in orders if exchange in order['symbol']]
        return orders


def get_orders(exchange=None, symbols=None, cl_ord_ids=None):
    """
    查询日内全部委托
    """
    req = GetOrdersReq()
    if exchange:
        exchange = exchange.upper()
        req.exchange = exchange

    if symbols:
        symbols = load_to_list(symbols)
        for symbol in symbols:
            req.symbols.append(symbol)

    if cl_ord_ids:
        cl_ord_ids = load_to_list(cl_ord_ids)
        for cl_ord_id in cl_ord_ids:
            req.cl_ord_ids.append(cl_ord_id)

    req = req.SerializeToString()
    status, result = py_nfi_get_orders(req)

    if not status == CSDK_OPERATE_SUCCESS:
        _error_call_back(status)
        return []

    if not result:
        return []

    res = Orders()
    res.ParseFromString(result)

    orders = [protobuf_to_dict(res_order, including_default_value_fields=True) for res_order in res.data]

    if not exchange:
        return orders
    else:
        orders = [order for order in orders if exchange in order['symbol']]
        return orders


def order_cancel(wait_cancel_orders):
    """
    撤销委托
    """
    wait_cancel_orders = load_to_list(wait_cancel_orders)

    orders = Orders()
    cancel_order_req = CancelOrderReq()

    try:
        cl_ord_ids = [order['cl_ord_id'] for order in wait_cancel_orders]
    except Exception as e:
        #传入的参数不是Order 类
        raise TypeError('order_cancel() : argument missing or incorrect argument type.')
    else:
        for cl_ord_id in cl_ord_ids:
            order = orders.data.add()
            order.cl_ord_id = cl_ord_id
        cancel_order_req.orders.extend([order])
        req = cancel_order_req.SerializeToString()

        status = py_nfi_cancel_order(req)
        if not status == CSDK_OPERATE_SUCCESS:
            _error_call_back(status)


# req = GetExecrptsReq, res = core.api.ExecRpts
def get_execution_reports(exchange=None):
    req = GetExecrptsReq()
    if exchange:
        exchange = exchange.upper()
        req.exchange = exchange

    req = req.SerializeToString()
    status, result = py_nfi_get_execution_reports(req)
    if not status == CSDK_OPERATE_SUCCESS:
        _error_call_back(status)
        return []

    res = ExecRpts()
    res.ParseFromString(result)
    reports = [protobuf_to_dict(Execrpt, including_default_value_fields=True) for
            Execrpt in res.data]

    if not exchange:
        return reports
    else:
        reports = [order for order in reports if exchange in order['symbol']]
        return reports


def get_positions(exchange=None, currency=None):
    # 持仓信息
    req = GetPositionsReq()
    if not currency:
        currency = ''

    if not exchange:
        exchange = ''

    exchange = exchange.upper()

    req.exchange = exchange
    req.currency = currency

    req = req.SerializeToString()
    status, result = py_nfi_get_positions(req)

    # 如果调用rpc返回的状态不正确
    if not status == CSDK_OPERATE_SUCCESS:
        _error_call_back(status)
        return []

    positions = Positions()
    positions.ParseFromString(result)

    positions = [protobuf_to_dict(position, including_default_value_fields=True)
                 for position in positions.data]

    res = []
    for position in positions:
        t_crc = position["currency"]
        if "." not in t_crc:
            continue
        t_crc_list = t_crc.split(".")
        if len(t_crc_list) != 2:
            continue
        t_exchange = t_crc_list[0]
        t_currency = t_crc_list[1]
        if exchange.strip() and exchange.upper() != t_exchange.upper():
            continue
        if currency.strip() and currency.upper() != t_currency.upper():
            continue
        '''原position中的currency格式为 交易所代码.币代码，如OKEX.btc，将此字段拆成两个独立的key，即在原posiiton中增加exchange'''
        position['currency'] = t_currency
        position['exchange'] = t_exchange

        res.append(position)
    return res


def get_symbols_by_front(market, currency, df=False):
    if not market or not  currency:
        raise TypeError('get_symbols_by_front() : argument missing or incorrect argument type.')

    market = market.upper()

    status, result = py_nfi_get_symbols_by_front(market, currency)

    if not status == CSDK_OPERATE_SUCCESS:
        _error_call_back(status)
        return []

    symbols = InstrumentInfos()
    symbols.ParseFromString(result)

    symbols = [protobuf_to_dict(symbol, including_default_value_fields=True) for symbol in symbols.data]

    instrument_infos = [
        '{}'.format(instrumentinfo['symbol']) for instrumentinfo in symbols]

    if not df:
        return instrument_infos

    data = pd.DataFrame(instrument_infos)

    return data


def get_symbols_by_fc(market, from_currency, df=False):
    if not market or not  from_currency:
        raise TypeError('get_symbols_by_fc() : argument missing or incorrect argument type.')

    market = market.upper()

    status, result = py_nfi_get_symbols_by_fc(market, from_currency)

    if not status == CSDK_OPERATE_SUCCESS:
        _error_call_back(status)
        return []

    symbols = InstrumentInfos()
    symbols.ParseFromString(result)

    symbols = [protobuf_to_dict(symbol, including_default_value_fields=True)
               for symbol in symbols.data]

    instrument_infos = [
        '{}'.format(symbol['symbol']) for
        symbol in symbols]

    if not df:
        return instrument_infos

    data = pd.DataFrame(instrument_infos)

    return data


def get_symbol_of_coins(market, currency_a, currency_b, df=False):
    if not market or not currency_a or not currency_b:
        raise TypeError('get_symbol_of_coins() : argument missing or incorrect argument type.')

    market = market.upper()

    status, result = py_nfi_get_symbol_of_coins(market, currency_a, currency_b)

    if not status == CSDK_OPERATE_SUCCESS:
        _error_call_back(status)
        return

    common_symbol_info = CommSymbolInfo()
    common_symbol_info.ParseFromString(result)

    # coins_info = {
    #   '{}'.format(common_symbol_info.data['symbol'])}

    if not df:
        return [common_symbol_info.data.symbole]

    data = pd.DataFrame([common_symbol_info.data.symbole])

    return data


def get_symbol(market, front, rear, df=False):
    if not market or not front or not rear:
        raise TypeError('get_symbol() : argument missing or incorrect argument type.')

    market = market.upper()

    status, result = py_nfi_get_symbol(market, front, rear)
    if not status == CSDK_OPERATE_SUCCESS:
        _error_call_back(status)
        return None

    common_symbol_info = CommSymbolInfo()
    common_symbol_info.ParseFromString(result)
    '''
    common_symbol_info = [protobuf_to_dict(symbol_info, including_default_value_fields=True)
                          for symbol_info in common_symbol_info.data]
    symbol = {
        '{}'.format(symbol_info['symbol']): symbol_info for
        symbol_info in common_symbol_info}
    '''

    if not df:
        return common_symbol_info.data.symbole

    data = pd.DataFrame([{'symbol': common_symbol_info.data.symbole}])

    return data


def get_execution_reports_intraday(exchange=None):
    if not exchange:
        exchange = ''

    exchange = exchange.upper()

    status, result = py_nfi_get_execution_reports_intraday(exchange)

    if not status == CSDK_OPERATE_SUCCESS:
        _error_call_back(status)
        return []

    res = ExecRpts()
    res.ParseFromString(result)

    reports = [protobuf_to_dict(Execrpt, including_default_value_fields=True) for
               Execrpt in res.data]

    if not exchange:
        return reports
    else:
        reports = [order for order in reports if exchange in order['symbol']]
        return reports


def get_orders_intraday(exchange=None):
    if not exchange:
        exchange = ''

    exchange = exchange.upper()

    status, result = py_nfi_get_orders_intraday(exchange)

    if not status == CSDK_OPERATE_SUCCESS:
        _error_call_back(status)
        return []

    res = Orders()
    res.ParseFromString(result)

    orders = [protobuf_to_dict(res_order, including_default_value_fields=True) for res_order in res.data]

    if not exchange:
        return orders
    else:
        orders = [order for order in orders if exchange in order['symbol']]
        return orders


def get_all_symbols_of_coin(market, from_currency, df=False):
    if not market or not from_currency:
        raise TypeError('get_all_symbols_of_coin() : argument missing or incorrect argument type.')

    market = market.upper()

    status, result = py_nfi_get_all_symbols_of_coin(market, from_currency)

    if not status == CSDK_OPERATE_SUCCESS:
        _error_call_back(status)
        return []

    instruments = InstrumentInfos()
    instruments.ParseFromString(result)

    instruments = [protobuf_to_dict(instrument, including_default_value_fields=True)
                   for instrument in instruments.data]

    coins_info = ['{}'.format(instrument['symbol']) for instrument in instruments]

    if not df:
        return coins_info

    data = pd.DataFrame(coins_info)

    return data


def history(symbol, frequency, start_time, end_time, fields='', skip_suspended=True, fill_missing='', df=False):
    if not symbol or not frequency or not start_time or not end_time:
        raise TypeError('history() : argument missing or incorrect argument type.')

    if len(symbol) <= 0:
        return []

    start_time = load_to_datetime_str(start_time)
    end_time = load_to_datetime_str(end_time)

    if frequency == 'tick':

        status, result = py_nfi_history_ticks(symbol, start_time, end_time, fields, skip_suspended,
                                              fill_missing, 1)

        if not status == CSDK_OPERATE_SUCCESS:
            _error_call_back(status)
            return []

        ticks = Ticks()
        ticks.ParseFromString(result)
        ticks = [protobuf_to_dict(tick) for tick in ticks.data]

        if not df:
            if not fields or fields == '':
                return ticks
            else:
                fields = load_to_list(fields)
                new_ticks = []
                for tick in ticks:
                    new_tick = {key: value for key, value in tick.items() if key in fields}
                    new_ticks.append(new_tick)
                return new_ticks


        if not ticks:
            return pd.DataFrame(columns=[fields])

        data = pd.DataFrame(ticks)
        if not fields or fields == '':
            return data
        else:
            fields = load_to_list(fields)
            return data[fields]

    else:

        frequency = _check_frequency(frequency)
        if not frequency:
            _error_call_back(ERR_INVALID_PARAMETER)
            return

        status, result = py_nfi_history_bars(symbol, frequency, start_time, end_time, fields, skip_suspended,
                                             fill_missing, 1)

        if not status == CSDK_OPERATE_SUCCESS:
            _error_call_back(status)
            return []

        bars = Bars()
        bars.ParseFromString(result)
        bars = [protobuf_to_dict(bars) for bars in bars.data]

        if not df:
            if not fields or fields == '':
                return bars
            else:
                fields = load_to_list(fields)
                new_bars = []
                for bar in bars:
                    new_bar = {key: value for key, value in bar.items() if key in fields}
                    new_bars.append(new_bar)
                return new_bars


        if not bars:
            return pd.DataFrame(columns=[fields])

        data = pd.DataFrame(bars)
        if not fields or fields == '':
            return data
        else:
            fields = load_to_list(fields)
            return data[fields]


def history_n(symbol, frequency, count, end_time, fields='', skip_suspended=True, fill_missing='', df=False):
    if not symbol or not frequency or not count or not end_time:
        raise TypeError('history_n() : argument missing or incorrect argument type.')

    if len(symbol) <= 0:
        return []

    end_time = load_to_datetime_str(end_time)

    if frequency == 'tick':

        status, result = py_nfi_history_ticks_n(symbol, count, end_time, fields, skip_suspended,
                                                fill_missing, 1)

        if not status == CSDK_OPERATE_SUCCESS:
            _error_call_back(status)
            return []

        ticks = Ticks()
        ticks.ParseFromString(result)
        ticks = [protobuf_to_dict(tick) for tick in ticks.data]

        if not df:
            if not fields or fields == '':
                return ticks
            else:
                fields = load_to_list(fields)
                new_ticks = []
                for tick in ticks:
                    new_tick = {key: value for key, value in tick.items() if key in fields}
                    new_ticks.append(new_tick)
                return new_ticks


        if not ticks:
            return pd.DataFrame(columns=[fields])

        data = pd.DataFrame(ticks)
        if not fields or fields == '':
            return data
        else:
            fields = load_to_list(fields)
            return data[fields]

    else:
        frequency = _check_frequency(frequency)
        if not frequency:
            _error_call_back(ERR_INVALID_PARAMETER)
            return

        status, result = py_nfi_history_bars_n(symbol, frequency, count, end_time, fields, skip_suspended,
                                               fill_missing, 1)

        if not status == CSDK_OPERATE_SUCCESS:
            _error_call_back(status)
            return []

        bars = Bars()
        bars.ParseFromString(result)
        bars = [protobuf_to_dict(bars) for bars in bars.data]

        if not df:
            if not fields or fields == '':
                return bars
            else:
                fields = load_to_list(fields)
                new_bars = []
                for bar in bars:
                    new_bar = {key: value for key, value in bar.items() if key in fields}
                    new_bars.append(new_bar)
                return new_bars


        if not bars:
            return pd.DataFrame(columns=[fields])

        data = pd.DataFrame(bars)
        if not fields or fields == '':
            return data
        else:
            fields = load_to_list(fields)
            return data[fields]


def get_unfinished_orders_intraday(exchange=None):
    if not exchange:
        exchange = ''

    exchange = exchange.upper()

    status, result = py_nfi_get_unfinished_orders_intraday(exchange)

    if not status == CSDK_OPERATE_SUCCESS:
        _error_call_back(status)
        return []

    res = Orders()
    res.ParseFromString(result)

    orders = [protobuf_to_dict(res_order, including_default_value_fields=True) for res_order in res.data]

    if not exchange:
        return orders
    else:
        orders = [order for order in orders if exchange in order['symbol']]
        return orders


def get_instruments(symbol):
    if not symbol or len(symbol) <= 0:
        raise TypeError('get_instruments() : argument missing or incorrect argument type.')

    status, result = py_nfi_get_instruments(symbol)

    if not status == CSDK_OPERATE_SUCCESS:
        _error_call_back(status)
        return

    res = SearchCoinPairsRsp()
    res.ParseFromString(result)

    return res


def order_cancel_all(exchange=""):
    exchange = exchange.upper()

    status = py_nfi_cancel_all_orders(exchange)

    return _error_call_back(status)


def get_exchange_rate(currencies, from_currency=None, start_time=None, end_time=None):
    """
    查询公允汇率，返回python list[dictionary]
    :param currencies:
    :param from_currency:
    :param start_time:
    :param end_time:
    :return:
    """
    if not currencies:
        raise TypeError('get_exchange_rate() : argument missing or incorrect argument type.')

    currencies_list = load_to_list(currencies)
    currencies = ','.join(currencies_list)

    if not from_currency:
        from_currency = 'USD'

    if not start_time:
        start_time = ''
    if not end_time:
        end_time = ''

    status, result = py_nfi_get_exchange_rate(currencies, from_currency, start_time, end_time)

    if not status == CSDK_OPERATE_SUCCESS:
        _error_call_back(status)
        return []

    # 反序列化。ExchangeRates是一个list类型，每个健对应的值是一个字典
    rates = ExchangeRateList()
    rates.ParseFromString(result)

    # 把返回的字典中的值取出来，放到一个字典列表中返回给用户
    rates = [protobuf_to_dict(currency, including_default_value_fields=True) for currency in rates.data]

    return rates


def get_depth(symbol, points=50):
    '''
    :param symbol:  trade symbol, like:BITFINEX.btcusd
    :param points:  levels of depth
    :return:    {'bids':[], 'asks':[]}
    :info: 用于获取交易深度
    '''
    if not symbol or len(symbol) <= 0:
        return

    if points > 50:
        points = 50

    status, result = py_nfi_get_market_depth(symbol)

    if not status == CSDK_OPERATE_SUCCESS:
        print('status: ', status)
        _error_call_back(status)
        return {}

    depth = DethpRateLists()
    depth.ParseFromString(result)

    depth = protobuf_to_dict(depth)

    bids = depth.data[0].bids
    asks = depth.data[0].asks

    if points < len(bids):
        bids = bids[0: points]
        asks = asks[0: points]

    bids = [dict_fields_filter(bid, ['price', 'volume']) for bid in bids]
    asks = [dict_fields_filter(ask, ['price', 'volume']) for ask in asks]

    bids.sort(key=takePriceFromDepth, reverse=True)     #买盘，降序
    asks.sort(key=takePriceFromDepth, reverse=False)    #卖盘，升序

    acc_vol = 0
    for dpt in asks:
        acc_vol += dpt['volume']
        dpt['accumulate'] = acc_vol

    acc_vol = 0
    for dpt in bids:
        acc_vol += dpt['volume']
        dpt['accumulate'] = acc_vol

    depth = {'points': len(bids), 'bids': bids, 'asks': asks}

    return depth

