import json
import logging
import urllib.parse
from collections import OrderedDict

import paypalrestsdk
from django import forms
from django.contrib import messages
from django.core import signing
from django.http import HttpRequest
from django.template.loader import get_template
from django.utils.translation import ugettext as __, ugettext_lazy as _

from pretix.base.decimal import round_decimal
from pretix.base.models import OrderPayment, OrderRefund, Quota
from pretix.base.payment import BasePaymentProvider, PaymentException
from pretix.base.services.mail import SendMailException
from pretix.helpers.urls import build_absolute_uri as build_global_uri
from pretix.multidomain.urlreverse import build_absolute_uri
from pretix.plugins.paypal.models import ReferencedPayPalObject

logger = logging.getLogger('pretix.plugins.paypal')


class Paypal(BasePaymentProvider):
    identifier = 'paypal'
    verbose_name = _('PayPal')
    payment_form_fields = OrderedDict([
    ])

    @property
    def settings_form_fields(self):
        d = OrderedDict(
            [
                ('endpoint',
                 forms.ChoiceField(
                     label=_('Endpoint'),
                     initial='live',
                     choices=(
                         ('live', 'Live'),
                         ('sandbox', 'Sandbox'),
                     ),
                 )),
                ('client_id',
                 forms.CharField(
                     label=_('Client ID'),
                     max_length=80,
                     min_length=80,
                     help_text=_('<a target="_blank" rel="noopener" href="{docs_url}">{text}</a>').format(
                         text=_('Click here for a tutorial on how to obtain the required keys'),
                         docs_url='https://docs.pretix.eu/en/latest/user/payments/paypal.html'
                     )
                 )),
                ('secret',
                 forms.CharField(
                     label=_('Secret'),
                     max_length=80,
                     min_length=80,
                 ))
            ] + list(super().settings_form_fields.items())
        )
        d.move_to_end('_enabled', False)
        return d

    def settings_content_render(self, request):
        return "<div class='alert alert-info'>%s<br /><code>%s</code></div>" % (
            _('Please configure a PayPal Webhook to the following endpoint in order to automatically cancel orders '
              'when payments are refunded externally.'),
            build_global_uri('plugins:paypal:webhook')
        )

    def init_api(self):
        paypalrestsdk.set_config(
            mode="sandbox" if "sandbox" in self.settings.get('endpoint') else 'live',
            client_id=self.settings.get('client_id'),
            client_secret=self.settings.get('secret'))

    def payment_is_valid_session(self, request):
        return (request.session.get('payment_paypal_id', '') != ''
                and request.session.get('payment_paypal_payer', '') != '')

    def payment_form_render(self, request) -> str:
        template = get_template('pretixplugins/paypal/checkout_payment_form.html')
        ctx = {'request': request, 'event': self.event, 'settings': self.settings}
        return template.render(ctx)

    def checkout_prepare(self, request, cart):
        self.init_api()
        kwargs = {}
        if request.resolver_match and 'cart_namespace' in request.resolver_match.kwargs:
            kwargs['cart_namespace'] = request.resolver_match.kwargs['cart_namespace']

        payment = paypalrestsdk.Payment({
            'intent': 'sale',
            'payer': {
                "payment_method": "paypal",
            },
            "redirect_urls": {
                "return_url": build_absolute_uri(request.event, 'plugins:paypal:return', kwargs=kwargs),
                "cancel_url": build_absolute_uri(request.event, 'plugins:paypal:abort', kwargs=kwargs),
            },
            "transactions": [
                {
                    "item_list": {
                        "items": [
                            {
                                "name": __('Order for %s') % str(request.event),
                                "quantity": 1,
                                "price": self.format_price(cart['total']),
                                "currency": request.event.currency
                            }
                        ]
                    },
                    "amount": {
                        "currency": request.event.currency,
                        "total": self.format_price(cart['total'])
                    },
                    "description": __('Event tickets for {event}').format(event=request.event.name)
                }
            ]
        })
        request.session['payment_paypal_order'] = None
        return self._create_payment(request, payment)

    def format_price(self, value):
        return str(round_decimal(value, self.event.currency, {
            # PayPal behaves differently than Stripe in deciding what currencies have decimal places
            # Source https://developer.paypal.com/docs/classic/api/currency_codes/
            'HUF': 0,
            'JPY': 0,
            'MYR': 0,
            'TWD': 0,
            # However, CLPs are not listed there while PayPal requires us not to send decimal places there. WTF.
            'CLP': 0,
            # Let's just guess that the ones listed here are 0-based as well
            # https://developers.braintreepayments.com/reference/general/currencies
            'BIF': 0,
            'DJF': 0,
            'GNF': 0,
            'KMF': 0,
            'KRW': 0,
            'LAK': 0,
            'PYG': 0,
            'RWF': 0,
            'UGX': 0,
            'VND': 0,
            'VUV': 0,
            'XAF': 0,
            'XOF': 0,
            'XPF': 0,
        }))

    @property
    def abort_pending_allowed(self):
        return False

    def _create_payment(self, request, payment):
        try:
            if payment.create():
                if payment.state not in ('created', 'approved', 'pending'):
                    messages.error(request, _('We had trouble communicating with PayPal'))
                    logger.error('Invalid payment state: ' + str(payment))
                    return
                request.session['payment_paypal_id'] = payment.id
                for link in payment.links:
                    if link.method == "REDIRECT" and link.rel == "approval_url":
                        if request.session.get('iframe_session', False):
                            signer = signing.Signer(salt='safe-redirect')
                            return (
                                build_absolute_uri(request.event, 'plugins:paypal:redirect') + '?url=' +
                                urllib.parse.quote(signer.sign(link.href))
                            )
                        else:
                            return str(link.href)
            else:
                messages.error(request, _('We had trouble communicating with PayPal'))
                logger.error('Error on creating payment: ' + str(payment.error))
        except Exception as e:
            messages.error(request, _('We had trouble communicating with PayPal'))
            logger.error('Error on creating payment: ' + str(e))

    def checkout_confirm_render(self, request) -> str:
        """
        Returns the HTML that should be displayed when the user selected this provider
        on the 'confirm order' page.
        """
        template = get_template('pretixplugins/paypal/checkout_payment_confirm.html')
        ctx = {'request': request, 'event': self.event, 'settings': self.settings}
        return template.render(ctx)

    def execute_payment(self, request: HttpRequest, payment: OrderPayment):
        if (request.session.get('payment_paypal_id', '') == '' or request.session.get('payment_paypal_payer', '') == ''):
            raise PaymentException(_('We were unable to process your payment. See below for details on how to '
                                     'proceed.'))

        self.init_api()
        pp_payment = paypalrestsdk.Payment.find(request.session.get('payment_paypal_id'))
        ReferencedPayPalObject.objects.get_or_create(order=payment.order, payment=payment, reference=pp_payment.id)
        if str(pp_payment.transactions[0].amount.total) != str(payment.amount) or pp_payment.transactions[0].amount.currency \
                != self.event.currency:
            logger.error('Value mismatch: Payment %s vs paypal trans %s' % (payment.id, str(pp_payment)))
            raise PaymentException(_('We were unable to process your payment. See below for details on how to '
                                     'proceed.'))

        return self._execute_payment(pp_payment, request, payment)

    def _execute_payment(self, payment, request, payment_obj):
        if payment.state == 'created':
            payment.replace([
                {
                    "op": "replace",
                    "path": "/transactions/0/item_list",
                    "value": {
                        "items": [
                            {
                                "name": __('Order {slug}-{code}').format(slug=self.event.slug.upper(),
                                                                         code=payment_obj.order.code),
                                "quantity": 1,
                                "price": self.format_price(payment_obj.amount),
                                "currency": payment_obj.order.event.currency
                            }
                        ]
                    }
                },
                {
                    "op": "replace",
                    "path": "/transactions/0/description",
                    "value": __('Order {order} for {event}').format(
                        event=request.event.name,
                        order=payment_obj.order.code
                    )
                }
            ])
            payment.execute({"payer_id": request.session.get('payment_paypal_payer')})

        payment_obj.refresh_from_db()
        if payment.state == 'pending':
            messages.warning(request, _('PayPal has not yet approved the payment. We will inform you as soon as the '
                                        'payment completed.'))
            payment_obj.info = json.dumps(payment.to_dict())
            payment_obj.state = OrderPayment.PAYMENT_STATE_PENDING
            payment_obj.save()
            return

        if payment.state != 'approved':
            payment_obj.state = OrderPayment.PAYMENT_STATE_FAILED
            payment_obj.save()
            logger.error('Invalid state: %s' % str(payment))
            raise PaymentException(_('We were unable to process your payment. See below for details on how to '
                                     'proceed.'))

        if payment_obj.state == OrderPayment.PAYMENT_STATE_CONFIRMED:
            logger.warning('PayPal success event even though order is already marked as paid')
            return

        try:
            payment_obj.info = json.dumps(payment.to_dict())
            payment_obj.save(update_fields=['info'])
            payment_obj.confirm()
        except Quota.QuotaExceededException as e:
            raise PaymentException(str(e))

        except SendMailException:
            messages.warning(request, _('There was an error sending the confirmation mail.'))
        return None

    def payment_pending_render(self, request, payment) -> str:
        retry = True
        try:
            if payment.info and payment.info_data['state'] == 'pending':
                retry = False
        except KeyError:
            pass
        template = get_template('pretixplugins/paypal/pending.html')
        ctx = {'request': request, 'event': self.event, 'settings': self.settings,
               'retry': retry, 'order': payment.order}
        return template.render(ctx)

    def payment_control_render(self, request: HttpRequest, payment: OrderPayment):
        template = get_template('pretixplugins/paypal/control.html')
        ctx = {'request': request, 'event': self.event, 'settings': self.settings,
               'payment_info': payment.info_data, 'order': payment.order}
        return template.render(ctx)

    def payment_partial_refund_supported(self, payment: OrderPayment):
        return True

    def payment_refund_supported(self, payment: OrderPayment):
        return True

    def execute_refund(self, refund: OrderRefund):
        self.init_api()

        sale = None
        for res in refund.payment.info_data['transactions'][0]['related_resources']:
            for k, v in res.items():
                if k == 'sale':
                    sale = paypalrestsdk.Sale.find(v['id'])
                    break

        pp_refund = sale.refund({
            "amount": {
                "total": self.format_price(refund.amount),
                "currency": refund.order.event.currency
            }
        })
        if not pp_refund.success():
            raise PaymentException(_('Refunding the amount via PayPal failed: {}').format(pp_refund.error))
        else:
            sale = paypalrestsdk.Payment.find(refund.payment.info_data['id'])
            refund.payment.info = json.dumps(sale.to_dict())
            refund.info = json.dumps(pp_refund.to_dict())
            refund.done()

    def payment_prepare(self, request, payment_obj):
        self.init_api()
        payment = paypalrestsdk.Payment({
            'intent': 'sale',
            'payer': {
                "payment_method": "paypal",
            },
            "redirect_urls": {
                "return_url": build_absolute_uri(request.event, 'plugins:paypal:return'),
                "cancel_url": build_absolute_uri(request.event, 'plugins:paypal:abort'),
            },
            "transactions": [
                {
                    "item_list": {
                        "items": [
                            {
                                "name": __('Order {slug}-{code}').format(slug=self.event.slug.upper(),
                                                                         code=payment_obj.order.code),
                                "quantity": 1,
                                "price": self.format_price(payment_obj.amount),
                                "currency": payment_obj.order.event.currency
                            }
                        ]
                    },
                    "amount": {
                        "currency": request.event.currency,
                        "total": self.format_price(payment_obj.amount)
                    },
                    "description": __('Order {order} for {event}').format(
                        event=request.event.name,
                        order=payment_obj.order.code
                    )
                }
            ]
        })
        request.session['payment_paypal_order'] = payment_obj.order.pk
        request.session['payment_paypal_payment'] = payment_obj.pk
        return self._create_payment(request, payment)

    def shred_payment_info(self, obj):
        if obj.info:
            d = json.loads(obj.info)
            new = {
                'id': d.get('id'),
                'payer': {
                    'payer_info': {
                        'email': '█'
                    }
                },
                'update_time': d.get('update_time'),
                'transactions': [
                    {
                        'amount': t.get('amount')
                    } for t in d.get('transactions', [])
                ],
                '_shredded': True
            }
            obj.info = json.dumps(new)
            obj.save(update_fields=['info'])

        for le in obj.order.all_logentries().filter(action_type="pretix.plugins.paypal.event").exclude(data=""):
            d = le.parsed_data
            if 'resource' in d:
                d['resource'] = {
                    'id': d['resource'].get('id'),
                    'sale_id': d['resource'].get('sale_id'),
                    'parent_payment': d['resource'].get('parent_payment'),
                }
            le.data = json.dumps(d)
            le.shredded = True
            le.save(update_fields=['data', 'shredded'])
