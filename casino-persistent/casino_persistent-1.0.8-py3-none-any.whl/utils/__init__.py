import time

from casino_persistent.utils.balance import Balance
from casino_persistent.utils.shatoshi_parser import ShatoshiParser


def get_epochtime_ms():
    return int(time.time())


def calculate_time_bet():
    return 15


def update_balance(balance):
    if balance[Balance.AMOUNT.value]:
        balance[Balance.AMOUNT.value] = ShatoshiParser.convert_coin_to_shatoshi(balance[Balance.AMOUNT.value])
    return balance


def update_balance_to_float(balance):
    if balance[Balance.AMOUNT.value]:
        balance[Balance.AMOUNT.value] = ShatoshiParser.convert_shatoshi_to_coin(balance[Balance.AMOUNT.value])
    return balance
