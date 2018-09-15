
import datetime

from betdaq.enums import Boolean
from betdaq.utils import listy_mc_list
from betdaq.endpoints.baseendpoint import BaseEndpoint
from betdaq.errorparsers.betting import err_cancel_market, err_suspend_orders
from betdaq.resources.bettingresources import (
    parse_orders, parse_single_order, parse_orders_receipt, parse_order_update,
    parse_cancelled_order, parse_suspended_order,
)


class Betting(BaseEndpoint):

    def get_orders(self, sequence_number=-1, want_settled_orders_on_unsettled_markets=Boolean.T.value):
        """
        Get the initial list of orders that's need to be taken into consideration when establishing positions. 
        Information about the following orders will be returned:
            •	active orders
            •	fully matched orders
            •	cancelled orders that have a matched portion 
            •	suspended orders
            •	some settled or voided orders under some conditions

        :param sequence_number: lower bound cutoff for sequence updates to include,
                               -1 will set to earliest possible sequence.
        :type sequence_number: int
        :param want_settled_orders_on_unsettled_markets: Flag indicating whether or not information about settled orders
                                                    on unsettled markets should be returned.
        :type want_settled_orders_on_unsettled_markets: bool
        :return: orders that have changed.
        """
        params = {
            'SequenceNumber': sequence_number,
            'wantSettledOrdersOnUnsettledMarkets': want_settled_orders_on_unsettled_markets
        }
        date_time_sent = datetime.datetime.utcnow()
        response = self.request('ListBootstrapOrders', params, secure=True)
        data = self.process_response(response, date_time_sent, 'Orders')
        return [parse_orders(order) for order in data.get('data', {}).get('Order', [])] if data.get('data') else []

    def get_maximum_sequence_number_order(self):
        """
        Get the maximum sequence number for orders

        :return: Maximum sequence Number
        """
        params = {'SequenceNumber': -1, 'wantSettledOrdersOnUnsettledMarkets': Boolean.T.value}
        response = self.request('ListBootstrapOrders', params, secure=True)
        return response.get('MaximumSequenceNumber')

    def get_orders_diff(self, sequence_number):
        """
        Get a list of orders for the logged in user that have changed since a given sequence number.
        Utilised to maintain position information after initial position is established with list_orders.

        :param sequence_number: lower bound cutoff for sequence updates to include.
        :type sequence_number: int
        :return: orders that have changed.
        """
        params = {'SequenceNumber': sequence_number}
        date_time_sent = datetime.datetime.utcnow()
        response = self.request('ListOrdersChangedSince', params, secure=True)
        data = self.process_response(response, date_time_sent, 'Orders')
        return [parse_orders(order) for order in data.get('data', {}).get('Order', [])] if data.get('data') else []

    def get_single_order(self, order_id):
        """
        Get full detail and history about an individual order.

        :param order_id: id of the order we wish to get history for.
        :type order_id: int
        :return: single orders history and current status.
        """
        params = {'OrderId': order_id}
        date_time_sent = datetime.datetime.utcnow()
        response = self.request('GetOrderDetails', params, secure=True)
        data = self.process_response(response, date_time_sent, None)
        return listy_mc_list(parse_single_order(data.get('data', {})) if data.get('data') else {})

    def place_orders(self, order_list, want_all_or_nothing_behaviour=Boolean.T.value, receipt=True):
        """
        Places one or more orders at exchange. 
        Receipt determines whether to wait for complete matching cycle or just return the order ID.
        
        :param order_list: List of orders to be sent to exchange
        :type order_list: list of betdaq_py.filters.create_order
        :param want_all_or_nothing_behaviour: defines whether to kill all orders on any error or place orders
         independently.
        :type want_all_or_nothing_behaviour: bool
        :param receipt: whether to wait for matching cycle and return full info of order or not.
        :type receipt: bool
        :return: the order ID or full order information depending on receipt.
        """
        date_time_sent = datetime.datetime.utcnow()
        if receipt:
            method = 'PlaceOrdersWithReceipt'
            params = self.client.secure_types['%sRequest' % method](Orders={'Order': order_list})
        else:
            method = 'PlaceOrdersNoReceipt'
            params = self.client.secure_types['%sRequest' % method](
                WantAllOrNothingBehaviour=want_all_or_nothing_behaviour, Orders={'Order': order_list}
            )
        response = self.request(method, params, secure=True)
        data = self.process_response(response, date_time_sent, 'Orders')
        return [
            parse_orders_receipt(order) for order in data.get('data', {}).get('Order', [])
        ] if data.get('data') else []

    def update_orders(self, order_list):
        """
        Update orders on exchange
        
        :param order_list: list of order updates to be sent to exchange.
        :type order_list: list of betdaq_py.filters.update_order
        :return: BetID and status of update.
        """
        params = self.client.secure_types['UpdateOrdersNoReceiptRequest'](Orders={'Order': order_list})
        date_time_sent = datetime.datetime.utcnow()
        response = self.request('UpdateOrdersNoReceipt', params, secure=True)
        data = self.process_response(response, date_time_sent, 'Orders')
        return [
            parse_order_update(update) for update in data.get('data', {}).get('Order', [])
        ] if data.get('data') else []

    def cancel_orders(self, order_ids):
        """
        Cancel one or more orders on exchange
        
        :param order_ids: list of order ids to be cancelled.
        :type order_ids: list of ints
        :return: information on the cancellation status of each order.
        """
        params = self.client.secure_types['CancelOrdersRequest'](
            _value_1=[{'OrderHandle': order_id} for order_id in order_ids]
        )
        date_time_sent = datetime.datetime.utcnow()
        response = self.request('CancelOrders', params, secure=True)
        data = self.process_response(response, date_time_sent, 'Orders')
        return [
            parse_cancelled_order(cancel) for cancel in data.get('data', {}).get('Order', [])
        ] if data.get('data') else []

    def cancel_orders_by_market(self, market_ids):
        """
        Cancel all orders on one or more markets on exchange
        
        :param market_ids: list of market ids to be cancelled.
        :type market_ids: list of ints
        :return: information on the cancellation status of each order.
        """
        params = self.client.secure_types['CancelAllOrdersOnMarketRequest'](
            _value_1=[{'MarketIds': market} for market in market_ids]
        )
        date_time_sent = datetime.datetime.utcnow()
        response = self.request('CancelAllOrdersOnMarket', params, secure=True)
        data = self.process_response(response, date_time_sent, 'Order', error_handler=err_cancel_market)
        return [parse_cancelled_order(cancel) for cancel in data.get('data', [])] if data.get('data') else []

    def cancel_all_orders(self):
        """
        Cancels all unmatched orders across all markets.

        :return: information on the cancellation status of each order.
        """
        date_time_sent = datetime.datetime.utcnow()
        response = self.request('CancelAllOrders', {}, secure=True)
        data = self.process_response(response, date_time_sent, 'Orders')
        return [
            parse_cancelled_order(cancel) for cancel in data.get('data', {}).get('Order', [])
        ] if data.get('data') else []

    def suspend_orders(self, order_ids):
        """
        Suspend one or more orders on exchange

        :param order_ids: list of order ids to be suspended.
        :type order_ids: list of ints
        :return: information on the suspension status of each order.
        """
        params = self.client.secure_types['SuspendOrdersRequest'](
            _value_1=[{'OrderIds': order_id} for order_id in order_ids]
        )
        date_time_sent = datetime.datetime.utcnow()
        response = self.request('SuspendOrders', params, secure=True)
        data = self.process_response(response, date_time_sent, 'Orders', error_handler=err_suspend_orders)
        return [parse_suspended_order(suspend) for suspend in data.get('data', [])] if data.get('data') else []

    def suspend_orders_by_market(self, market_ids):
        """
        Suspend all orders on a given market.

        :param market_ids: market id to be suspend orders on.
        :type market_ids: ints
        :return: information on the suspension status of each order.
        """
        # params = clean_locals(locals())
        params = {'MarketIds': market_ids}
        date_time_sent = datetime.datetime.utcnow()
        response = self.request('SuspendAllOrdersOnMarket', params, secure=True)
        data = self.process_response(response, date_time_sent, 'Orders', error_handler=err_suspend_orders)
        return [parse_suspended_order(suspend) for suspend in data.get('data', [])] if data.get('data') else []

    def suspend_all_orders(self):
        """
        Suspend all orders across all markets.

        :return: information on the suspension status of each order.
        """
        date_time_sent = datetime.datetime.utcnow()
        response = self.request('SuspendAllOrders', {}, secure=True)
        data = self.process_response(response, date_time_sent, 'Orders', error_handler=err_suspend_orders)
        return [parse_suspended_order(suspend) for suspend in data.get('data', [])] if data.get('data') else []

    def unsuspend_orders(self, order_ids):
        """
        Unsuspend one or more suspended orders
        
        :param order_ids: list of order ids to unsuspend.
        :type order_ids: list
        :return: 
        """
        params = self.client.secure_types['UnsuspendOrdersRequest'](
            _value_1=[{'OrderIds': order_id} for order_id in order_ids]
        )
        date_time_sent = datetime.datetime.utcnow()
        response = self.request('UnsuspendOrders', params, secure=True)
        self.process_response(response, date_time_sent, None)
        return []
