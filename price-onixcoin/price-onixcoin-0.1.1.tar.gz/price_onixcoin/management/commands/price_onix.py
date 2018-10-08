#!/usr/bin/env python
from django.core.management.base import BaseCommand
from price_onixcoin.models import PriceOnix, \
    PriceBtcLocalbitcoin, Yobit, Country
import os

BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))) + '/commands/'


class Command(BaseCommand):
    help = "Comando para recabar un historico de precios"

    def handle(self, *args, **options):
        data_yobit = Yobit.objects.all()[:1]
        data_yobit = data_yobit[0]
        # buscar los paises
        paises = Country.objects.all()

        for pais in paises:

            data_btc = PriceBtcLocalbitcoin.objects.filter(country=pais).defer('created_at')[:1]
            data_btc = data_btc[0]

            list_data_bs = {
                data_btc.price_btc_bs_avg_1h,
                data_btc.price_btc_bs_avg_6h,
                data_btc.price_btc_bs_avg_12h,
                data_btc.price_btc_bs_avg_24h
            }

            list_data_usd = {
                data_btc.price_btc_usd_avg_1h,
                data_btc.price_btc_usd_avg_6h,
                data_btc.price_btc_usd_avg_12h,
                data_btc.price_btc_usd_avg_24h,
            }

            # determinar el maximo promedio del precio del bitcoin en bolivares (MONEDA LOCAL)
            price_max_btc_bs = sorted(
                list_data_bs, reverse=True)[0]

            price_max_btc_usd = sorted(
                list_data_usd, reverse=True)[0]

            onx_bs_sell = data_yobit.btc_onx_sell * price_max_btc_bs
            onx_bs_buy = data_yobit.btc_onx_buy * price_max_btc_bs

            onx_usd_sell = data_yobit.btc_onx_sell * price_max_btc_usd
            onx_usd_buy = data_yobit.btc_onx_buy * price_max_btc_usd


            PriceOnix(
                btc_onx_buy=data_yobit.btc_onx_buy,
                onx_bs_buy=onx_bs_buy,
                usd_onx_buy=onx_usd_buy,
                btc_onx_sell=data_yobit.btc_onx_sell,
                onx_bs_sell=onx_bs_sell,
                usd_onx_sell=onx_usd_sell,
                country=pais
            ).save()