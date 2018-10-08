#!/usr/bin/env python
from django.core.management.base import BaseCommand
from decimal import Decimal
from price_onixcoin.models import Yobit
import os
import requests

BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))) + '/commands/'


class Command(BaseCommand):
    help = "Comando para registar los valores de onx en yobit"

    def handle(self, *args, **options):
        headers = {'Content-Type': 'application/json'}
        url = 'https://yobit.net/api/2/onx_btc/ticker'
        r = requests.get(url, headers=headers)
        resp = r.json()

        btc_onx_buy = resp['ticker']['buy']
        btc_onx_sell = resp['ticker']['sell']

        url = 'https://yobit.net/api/2/btc_usd/ticker'
        r = requests.get(url, headers=headers)
        resp = r.json()

        usd_btc_buy = resp['ticker']['sell']
        usd_btc_sell = resp['ticker']['buy']

        Yobit(
            btc_onx_sell=Decimal(btc_onx_sell),
            usd_btc_sell=Decimal(usd_btc_sell),
            btc_onx_buy=Decimal(btc_onx_buy),
            usd_btc_buy=Decimal(usd_btc_buy),
        ).save()
