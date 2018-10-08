from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Country(models.Model):
    code_country = models.CharField(max_length=3, primary_key=True)
    country = models.CharField(max_length=60, null=False, blank=False, verbose_name=_('Páis'))
    code_currency = models.CharField(max_length=3, null=False, blank=False, verbose_name=_('Simbolo de moneda'))


    def __str__(self):
        return self.country

    class Meta:
        db_table = 'onx_price_country'
        verbose_name_plural = _('Paises')


class PriceBtcLocalbitcoin(models.Model):
    price_btc_usd_avg_1h = models.DecimalField(
        max_digits=20, decimal_places=8, null=False, blank=False
    )
    price_btc_usd_avg_6h = models.DecimalField(
        max_digits=20, decimal_places=8, null=False, blank=False
    )
    price_btc_usd_avg_12h = models.DecimalField(
        max_digits=20, decimal_places=8, null=False, blank=False
    )
    price_btc_usd_avg_24h = models.DecimalField(
        max_digits=20, decimal_places=8, null=False, blank=False
    )
    price_btc_bs_avg_1h = models.DecimalField(
        max_digits=20, decimal_places=8, null=False, blank=False,
        verbose_name=_('BTC EN MONEDA LOCAL AVG 1H')
    )
    price_btc_bs_avg_6h = models.DecimalField(
        max_digits=20, decimal_places=8, null=False, blank=False,
        verbose_name=_('BTC EN MONEDA LOCAL AVG 6H')
    )
    price_btc_bs_avg_12h = models.DecimalField(
        max_digits=20, decimal_places=8, null=False, blank=False,
        verbose_name = _('BTC EN MONEDA LOCAL AVG 12H')
    )
    price_btc_bs_avg_24h = models.DecimalField(
        max_digits=20, decimal_places=8, null=False, blank=False,
        verbose_name=_('BTC EN MONEDA LOCAL AVG 24H')
    )
    country = models.ForeignKey(Country, default='VEN', on_delete=models.PROTECT)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'onx_price_btc'
        ordering = ['-created_at']

        verbose_name_plural = _('Precios bitcoins')

class PriceOnix(models.Model):
    btc_onx_buy = models.DecimalField(
        max_digits=20, decimal_places=8, null=False, blank=False
    )
    onx_bs_buy = models.DecimalField(
        max_digits=20, decimal_places=8, null=False, blank=False,
        verbose_name=_('ONX EN MONEDA LOCAL PARA LA COMPRA')
    )
    usd_onx_buy = models.DecimalField(
        max_digits=20, decimal_places=8, null=False, blank=False
    )
    btc_onx_sell = models.DecimalField(
        max_digits=20, decimal_places=8, null=False, blank=False
    )
    onx_bs_sell = models.DecimalField(
        max_digits=20, decimal_places=8, null=False, blank=False,
        verbose_name=_('ONX EN MONEDA LOCAL PARA LA VENTA')
    )
    usd_onx_sell = models.DecimalField(
        max_digits=20, decimal_places=8, null=False, blank=False,
    )
    country = models.ForeignKey(Country, default='VEN', on_delete=models.PROTECT)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'onx_historico_price'
        ordering = ['-created_at']
        verbose_name_plural = _('Precios del onix')

class Yobit(models.Model):
    btc_onx_sell = models.DecimalField(
        max_digits=20, decimal_places=8, null=False, blank=False)
    usd_btc_sell = models.DecimalField(
        max_digits=20, decimal_places=8, null=False, blank=False)
    btc_onx_buy = models.DecimalField(
        max_digits=20, decimal_places=8, null=False, blank=False)
    usd_btc_buy = models.DecimalField(
        max_digits=20, decimal_places=8, null=False, blank=False)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'yobit_onix'
        ordering = ['-created_at']
