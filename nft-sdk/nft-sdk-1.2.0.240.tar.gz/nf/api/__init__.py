# coding=utf-8
from __future__ import print_function, absolute_import, unicode_literals

# 基本api
import getopt
import sys

from nf.model.storage import context

from nf import __version__
from nf.enum import *

from nf.csdk.c_sdk import py_nfi_set_version
from .basic import (
    set_token, get_version, subscribe, unsubscribe,
    current, get_strerror, schedule, run, log, set_serv_addr, stop, now)

# 交易api
from .trade import (
    order_volume, order_value, order_batch, order_cancel, order_cancel_all, get_positions,
    get_orders, get_unfinished_orders, get_execution_reports,
    get_symbols_by_front, get_symbols_by_fc, get_symbol_of_coins,
    get_all_symbols_of_coin, get_symbol, get_execution_reports_intraday,
    get_orders_intraday, get_instruments,
    history, history_n, get_unfinished_orders_intraday,
    get_exchange_rate,
    get_depth
)

# 数据查询api
from .query import (get_trades)


__all__ = [
    'context',
    'set_token', 'get_version', 'subscribe', 'unsubscribe',
    'current', 'get_strerror', 'schedule', 'run', 'get_instruments',
    'log', 'stop', 'now', 'set_serv_addr',

    'order_volume', 'order_value', 'order_batch', 'order_cancel', 'order_cancel_all',
    'get_positions', 'get_orders', 'get_unfinished_orders', 'get_execution_reports',
    'get_execution_reports_intraday', 'get_orders_intraday',
    'get_unfinished_orders_intraday',

    'get_symbols_by_front', 'get_symbols_by_fc', 'get_symbol_of_coins',
    'get_all_symbols_of_coin', 'get_symbol',

    'history', 'history_n',

    'get_exchange_rate',
    'get_depth',

    'get_trades',

    'ExecType_Unknown',
    'ExecType_New',
    'ExecType_DoneForDay',
    'ExecType_Canceled',
    'ExecType_PendingCancel',
    'ExecType_Stopped',
    'ExecType_Rejected',
    'ExecType_Suspended',
    'ExecType_PendingNew',
    'ExecType_Calculated',
    'ExecType_Expired',
    'ExecType_Restated',
    'ExecType_PendingReplace',
    'ExecType_Trade',
    'ExecType_TradeCorrect',
    'ExecType_TradeCancel',
    'ExecType_OrderStatus',
    'ExecType_CancelRejected',
    'OrderStatus_Unknown',
    'OrderStatus_New',
    'OrderStatus_PartiallyFilled',
    'OrderStatus_Filled',
    'OrderStatus_DoneForDay',
    'OrderStatus_Canceled',
    'OrderStatus_PendingCancel',
    'OrderStatus_Stopped',
    'OrderStatus_Rejected',
    'OrderStatus_Suspended',
    'OrderStatus_PendingNew',
    'OrderStatus_Calculated',
    'OrderStatus_Expired',
    'OrderStatus_AcceptedForBidding',
    'OrderStatus_PendingReplace',
    'OrderRejectReason_Unknown',
    'OrderRejectReason_RiskRuleCheckFailed',
    'OrderRejectReason_NoEnoughCash',
    'OrderRejectReason_NoEnoughPosition',
    'OrderRejectReason_IllegalAccountId',
    'OrderRejectReason_IllegalStrategyId',
    'OrderRejectReason_IllegalSymbol',
    'OrderRejectReason_IllegalVolume',
    'OrderRejectReason_IllegalPrice',
    'OrderRejectReason_AccountDisabled',
    'OrderRejectReason_AccountDisconnected',
    'OrderRejectReason_AccountLoggedout',
    'OrderRejectReason_NotInTradingSession',
    'OrderRejectReason_OrderTypeNotSupported',
    'OrderRejectReason_Throttle',
    'CancelOrderRejectReason_OrderFinalized',
    'CancelOrderRejectReason_UnknownOrder',
    'CancelOrderRejectReason_BrokerOption',
    'CancelOrderRejectReason_AlreadyInPendingCancel',
    'OrderSide_Unknown',
    'OrderSide_Buy',
    'OrderSide_Sell',
    'OrderType_Unknown',
    'OrderType_Limit',
    'OrderType_Market',
    'OrderType_Stop',
    'OrderDuration_Unknown',
    'OrderDuration_FAK',
    'OrderDuration_FOK',
    'OrderDuration_GFD',
    'OrderDuration_GFS',
    'OrderDuration_GTD',
    'OrderDuration_GTC',
    'OrderDuration_GFA',
    'OrderQualifier_Unknown',
    'OrderQualifier_BOC',
    'OrderQualifier_BOP',
    'OrderQualifier_B5TC',
    'OrderQualifier_B5TL',
    'OrderStyle_Unknown',
    'OrderStyle_Volume',
    'OrderStyle_Value',
    'OrderStyle_Percent',
    'OrderStyle_TargetVolume',
    'OrderStyle_TargetValue',
    'OrderStyle_TargetPercent',
    'PositionSide_Unknown',
    'PositionSide_Long',
    'PositionSide_Short',
    'PositionEffect_Unknown',
    'PositionEffect_Open',
    'PositionEffect_Close',
    'PositionEffect_CloseToday',
    'PositionEffect_CloseYesterday',
    'CashPositionChangeReason_Unknown',
    'CashPositionChangeReason_Trade',
    'CashPositionChangeReason_Inout',
    'MODE_LIVE',
    'MODE_BACKTEST',
    'ADJUST_NONE',
    'ADJUST_PREV',
    'ADJUST_POST',
    'SEC_TYPE_STOCK',
    'SEC_TYPE_FUND',
    'SEC_TYPE_INDEX',
    'SEC_TYPE_FUTURE',
    'SEC_TYPE_OPTION',
    'SEC_TYPE_CONFUTURE',

]

try:
    __all__ = [str(item) for item in __all__]
    py_nfi_set_version(__version__.__version__, 'python')

    command_argv = sys.argv[1:]
    options, args = getopt.getopt(command_argv, None,
                                  ['strategy_id=', 'filename=',
                                   'mode=', 'token=',
                                   'backtest_start_time=',
                                   'backtest_end_time=',
                                   'backtest_initial_cash=',
                                   'backtest_transaction_ratio=',
                                   'backtest_commission_ratio=',
                                   'backtest_slippage_ratio=',
                                   'backtest_adjust=',
                                   'backtest_check_cache=',
                                   'serv_addr='
                                   ])

    for option, value in options:
        if option == '--serv_addr' and value:
            set_serv_addr(value)
            break
except BaseException as e:
    pass
