from eth_account.messages import (
    defunct_hash_message,
)
from web3 import Web3
from web3.auto import (
    w3,
)

from request_network.api import (
    RequestNetwork,
)
from request_network.exceptions import (
    InvalidRequestHash,
    InvalidRequestParameters,
    InvalidRequestSignature,
    InvalidRequestState,
)
from request_network.services.core import (
    RequestCoreService,
)
from request_network.types import (
    States,
)
from request_network.utils import (
    get_request_bytes_representation,
    hash_request_object,
)


class RequestEthereumService(RequestCoreService):

    def _get_currency_contract_artifact_name(self):
        return 'last-RequestEthereum'

    def accept_request(self, request_id, payer_address):
        """ Accept the Request identified by request_id.
        """
        request_api = RequestNetwork()
        request = request_api.get_request_by_id(request_id)

        if request.state != States.CREATED:
            raise InvalidRequestState(
                'Request {} is not in "created" state'.format(request_id))

        if payer_address != request.payer:
            raise InvalidRequestParameters(
                'Broadcasting account must be the payer account'
            )

        currency_contract_data = self.get_currency_contract_data()
        currency_contract = currency_contract_data['instance']

        # TODO why accept this as an arg? Why not just take it from the Request?
        transaction_options = {
            'from': request.payer,
        }

        tx_hash = currency_contract.functions.accept(
            _requestId=request_id
        ).transact(transaction_options)
        return Web3.toHex(tx_hash)

    def cancel_request(self, request_id, from_address):
        """ Cancel the Request identified by request_id.

            payer can cancel when state==created
            payee can cancel when state==accelted
        """
        request_api = RequestNetwork()
        request = request_api.get_request_by_id(request_id)

        if from_address not in [request.payer, request.id_addresses[0]]:
            raise InvalidRequestParameters(
                'from_address must be either payer or payee'
            )

        if request.state == States.CANCELED:
            raise InvalidRequestState(
                'Request has already been cancelled')

        if request.state == States.CREATED and request.payer != from_address:
            raise InvalidRequestState(
                'Only the payer can cancel a created Request')

        if request.state == States.ACCEPTED and request.id_addresses[0] != from_address:
            raise InvalidRequestState(
                'Only the payee can cancel an accepted Request'
            )

        if len(request.payments):
            raise InvalidRequestState(
                'Request can not be cancelled as payments have already been made'
            )

        transaction_options = {
            # TODO support request's options param for tx options?
            'from': from_address,
        }

        currency_contract_data = self.get_currency_contract_data()
        currency_contract = currency_contract_data['instance']

        tx_hash = currency_contract.functions.cancel(
            _requestId=request_id
        ).transact(transaction_options)
        return Web3.toHex(tx_hash)

    def broadcast_signed_request_as_payer(self, signed_request, payer_address,
                                          payment_amounts=None, additional_payments=None):
        """

        :param signed_request:
        :type signed_request: request_network.types.Request
        :param payment_amounts: Amounts to pay when Request is broadcast
        :param additional_payments: Extra amounts to pay, in addition to payment_amounts
        :return:
        """
        # In case we do not have payment_amounts/additional_payments, generate a list
        # of 0s of the same size as payees
        empty_payments = [0] * len(signed_request.payees)
        additional_payments = additional_payments if additional_payments else empty_payments
        payment_amounts = payment_amounts if payment_amounts else empty_payments
        # Add the additional amount, if any, to the payment amount
        payment_amounts = [a + b for a, b in zip(payment_amounts, additional_payments)]

        # TODO Complete validation, more DRY
        if payer_address == signed_request.id_addresses[0]:
            raise InvalidRequestParameters(
                'Payer can not be the main payee'
            )

        if not all(i >= 0 for i in payment_amounts):
            raise InvalidRequestParameters(
                'payment_amounts must be positive integers')

        if not all(i >= 0 for i in additional_payments):
            raise InvalidRequestParameters(
                'additional_payments must be positive integers')

        # Generate the hash from the Request's info and check it matches the provided hash
        computed_hash = hash_request_object(signed_request)
        if signed_request.hash != computed_hash:
            raise InvalidRequestHash()

        # Recover the signer's address and make sure this Request was signed
        # by the main payee.
        message_hash = defunct_hash_message(hexstr=computed_hash)
        signer_address = w3.eth.account.recoverHash(
            message_hash,
            signature=signed_request.signature)
        if signer_address != signed_request.id_addresses[0]:
            raise InvalidRequestSignature('payee is not the signer'.format(
                signer_address, payer_address
            ))

        currency_contract_data = self.get_currency_contract_data()
        currency_contract = currency_contract_data['instance']
        estimated_value = currency_contract.functions.collectEstimation(
            _expectedAmount=sum(a for a in signed_request.amounts)
        ).call()

        transaction_options = {
            'from': payer_address,
            'value': estimated_value + sum(payment_amounts),
        }
        request_bytes = get_request_bytes_representation(
            payee_id_addresses=signed_request.id_addresses,
            amounts=signed_request.amounts,
            payer=None,
            ipfs_hash=signed_request.ipfs_hash
        )

        tx_hash = currency_contract.functions.broadcastSignedRequestAsPayer(
            _requestData=Web3.toBytes(hexstr=request_bytes),
            _payeesPaymentAddress=signed_request.payment_addresses,
            _payeeAmounts=payment_amounts,
            _additionals=additional_payments,
            _expirationDate=signed_request.expiration_date,
            _signature=Web3.toBytes(hexstr=signed_request.signature)
        ).transact(transaction_options)

        return Web3.toHex(tx_hash)

    def pay_request(self, request_id, payment_amounts, from_address,
                    additional_payments=None):
        """ Pay a Request.

            Note that this implementation differs from the JS version.

            In JS, payment_amounts includes the additional amounts. e.g.
            to send a standard payment of 100 with an additional 50,
            paymentAction would be called with _amountsToPay=[150], and
            additionals=[50].

            IMO this violates the principle of least surprise - one would
            expect the payment amounts to be separate from the additional
            amounts, otherwise what is the point of having aditionals as
            a separate argument? It could be calculated by comparing
            _amountsToPay with the Request's expected amounts.

            This implementation treats `payment_amounts` and
            `additional_payments` separately. To send a payment of 100 with
            an additional 50, this function should be called with
            payment_amounts=[100] and additional_payments=[50].

            To maintain compatibility with the smart contracts, the data
            is sent to the contract in the JS-format (i.e. additional amounts
            are added to payment amounts, but also sent in the _additionals
            parameter).

        :param request_id:
        :param payment_amounts:
        :param from_address:
        :param additional_payments:
        :return:
        """
        request_api = RequestNetwork()
        request = request_api.get_request_by_id(request_id)

        empty_payments = [0] * len(request.payees)
        additional_payments = additional_payments if additional_payments else empty_payments
        # Add the additional amount, if any, to the payment amount
        payment_amounts = [a + b for a, b in zip(payment_amounts, additional_payments)]

        if request.state == States.CANCELED:
            raise InvalidRequestState(
                'A cancelled Request can not be paid'
            )

        if len(request.payees) != len(payment_amounts):
            raise InvalidRequestParameters(
                'Payees and payment_amounts must be the same length'
            )

        if len(request.payees) != len(additional_payments):
            raise InvalidRequestParameters(
                'Payees and additional_payments must be the same length'
            )

        if not all(i >= 0 for i in payment_amounts):
            raise InvalidRequestParameters(
                'payment_amounts must be positive integers')

        if not all(i >= 0 for i in additional_payments):
            raise InvalidRequestParameters(
                'additional_payments must be positive integers')

        if sum(additional_payments) > 0 and request.payer != from_address:
            raise InvalidRequestParameters(
                'Only the Payer can add additionals'
            )

        if request.payees[0].id_address == from_address:
            raise InvalidRequestParameters(
                'The payer can not be the main payee'
            )

        transaction_options = {
            'from': from_address,
            'value': sum(payment_amounts),
        }

        currency_contract_data = self.get_currency_contract_data()
        currency_contract = currency_contract_data['instance']
        tx_hash = currency_contract.functions.paymentAction(
            _requestId=request_id,
            _payeeAmounts=payment_amounts,
            _additionalAmounts=additional_payments
        ).transact(transaction_options)

        return Web3.toHex(tx_hash)

    def refund_request(self, request_id, refund_amount, from_address):
        """ Refund a Request.

        Only the payees' id_addresses or payment_addresses can refund a
        Request.

        Refunding updates the balance attribute of the on-chain Request.

        :param request_id:
        :param refund_amount:
        :param from_address:
        :return:
        """
        request_api = RequestNetwork()
        request = request_api.get_request_by_id(request_id)

        if from_address not in request.id_addresses + request.payment_addresses:
            raise InvalidRequestParameters(
                "Request can only be refunded by the payee's ID or payment addresses"
            )

        if refund_amount < 0:
            raise InvalidRequestParameters(
                "Refund amount must be a positive integer"
            )

        if request.state == States.CANCELED:
            raise InvalidRequestParameters(
                "A cancelled Request can not be refunded"
            )

        transaction_options = {
            'from': from_address,
            'value': refund_amount
        }

        currency_contract_data = self.get_currency_contract_data()
        currency_contract = currency_contract_data['instance']
        tx_hash = currency_contract.functions.refundAction(
            _requestId=request_id
        ).transact(transaction_options)

        return Web3.toHex(tx_hash)

    def add_additional_payment(self, request_id, amounts, from_address):
        """ Add an extra payment to a Request (e.g. a tip/bonus)

        :param request_id:
        :param amounts:
        :param from_address:
        :return:
        """
        request_api = RequestNetwork()
        request = request_api.get_request_by_id(request_id)

        if from_address != request.payer:
            raise InvalidRequestParameters(
                "Additional amounts can only be added by the payer"
            )

        if len(amounts) != len(request.amounts):
            raise InvalidRequestParameters(
                "Additional amounts must be the same length as Request amounts"
            )

        if request.state not in [States.ACCEPTED, States.CREATED]:
            raise InvalidRequestState(
                "Additional amounts can only be added to Requests with a "
                "state of accepted or created"
            )

        if not all(i >= 0 for i in amounts):
            raise InvalidRequestParameters(
                'Additional amounts must be positive integers')

        transaction_options = {
            'from': from_address,
        }

        currency_contract_data = self.get_currency_contract_data()
        currency_contract = currency_contract_data['instance']
        tx_hash = currency_contract.functions.additionalAction(
            _requestId=request_id,
            _additionalAmounts=amounts
        ).transact(transaction_options)

        return Web3.toHex(tx_hash)

    def add_discount(self, request_id, amounts, from_address):
        """ Add a discount to the Request (i.e. decrease the expected amounts)

        :param request_id:
        :param amounts:
        :param from_address:
        :return:
        """
        request_api = RequestNetwork()
        request = request_api.get_request_by_id(request_id)

        if from_address != request.id_addresses[0]:
            raise InvalidRequestParameters(
                "Discounts can only be added by the main payee"
            )

        if len(amounts) != len(request.amounts):
            raise InvalidRequestParameters(
                "Discounts amounts must be the same length as Request amounts"
            )

        if request.state not in [States.ACCEPTED, States.CREATED]:
            raise InvalidRequestState(
                "Discounts can only be added to Requests with a "
                "state of accepted or created"
            )

        if not all(i >= 0 for i in amounts):
            raise InvalidRequestParameters(
                'Discount amounts must be positive integers')

        if not all(a < b for a, b in zip(amounts, request.amounts)):
            raise InvalidRequestParameters(
                'Discounts can not be higher than the expected amount')

        transaction_options = {
            'from': from_address,
        }

        currency_contract_data = self.get_currency_contract_data()
        currency_contract = currency_contract_data['instance']
        tx_hash = currency_contract.functions.subtractAction(
            _requestId=request_id,
            _subtractAmounts=amounts
        ).transact(transaction_options)

        return Web3.toHex(tx_hash)
