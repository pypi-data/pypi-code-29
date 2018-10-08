#!/usr/bin/env python
import decimal

from django.core.management.base import BaseCommand
from decimal import Decimal

import os
import requests
from price_onixcoin.models import PriceBtcLocalbitcoin, Country

BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))) + '/commands/'


class Command(BaseCommand):
    help = "Comando para registar el precio del btc desde localbitcoin"

    def handle(self, *args, **options):
        headers = {'Content-Type': 'application/json'}
        url = 'https://localbitcoins.com/bitcoinaverage/ticker-all-currencies/'
        r = requests.get(url, headers=headers)
        resp = r.json()

        precio_btc_usd_local = resp['USD']

        # buscar los paises
        paises = Country.objects.all()

        try:
            for pais in paises:
                precio_btc_bs_local = resp[pais.code_currency]
                PriceBtcLocalbitcoin(
                    price_btc_usd_avg_1h=Decimal(precio_btc_usd_local['rates']['last']),
                    price_btc_usd_avg_6h=Decimal(precio_btc_usd_local['avg_6h']),
                    price_btc_usd_avg_12h=Decimal(
                        precio_btc_usd_local['avg_12h']),
                    price_btc_usd_avg_24h=Decimal(
                        precio_btc_usd_local['avg_24h']),

                    price_btc_bs_avg_1h=Decimal(precio_btc_bs_local['rates']['last']),
                    price_btc_bs_avg_6h=Decimal(precio_btc_bs_local['avg_6h']),
                    price_btc_bs_avg_12h=Decimal(precio_btc_bs_local['avg_12h']),
                    price_btc_bs_avg_24h=Decimal(precio_btc_bs_local['avg_24h']),
                    country=pais
                ).save()
        except decimal.InvalidOperation as e:
            pass
