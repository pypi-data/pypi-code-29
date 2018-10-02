from collections import (
    defaultdict,
    namedtuple,
)
from unittest import (
    mock,
)

from eth_abi import (
    decode_abi,
)
from eth_abi.decoding import (
    StringDecoder,
    decode_uint_256,
)
from eth_utils import (
    event_abi_to_log_topic,
)
from web3 import Web3
from web3.auto import (
    w3,
)
from web3.utils.datastructures import (
    AttributeDict,
)
from web3.utils.events import (
    get_event_data,
)

from request_network.artifact_manager import (
    ArtifactManager,
)
from request_network.constants import (
    EMPTY_BYTES_20,
)
from request_network.exceptions import (
    RequestNotFound,
    RoleNotSupported,
    TransactionNotFound,
)
from request_network.types import (
    Payee,
    Payment,
    Request,
    Roles,
)
from request_network.utils import (
    get_service_for_currency,
    retrieve_ipfs_data,
)


class RequestNetwork(object):
    """ The main interaction point with the Request Network API.
    """

    def create_request(self, role, currency, payees, payer, data=None):
        """ Create a Request.

        If the Request is being created by the payer it is possible to create
        it and pay in a single transaction, using the `Payee.payment_amount`
        and `Payee.additional_amount` parameters.

        Note that this method broadcasts the transaction which will create the
        Request, but does not confirm that the transaction is included in the
        block. The Request's `is_broadcast` property can be used to check this -
        it will be True if the Request can be successfully retrieved from
        the blockchain using its transaction hash.

        :param role: Role of the caller, i.e. Payer or Payee
        :type role: types.Roles.PAYEE
        :param currency: The currency in which payment will be made
        :type currency: currency.Currency
        :param payees: List of Payees
        :type payees: [types.Payee]
        :param payer: A Payer representing the address which will pay the Request
        :type payer: types.Payer
        :param data: Optional dictionary of data which will be stored on IPFS
        :type data: dict
        :return: The transaction hash of the transaction which, if successfully
            included in a block, will create this Request.
        """

        service_args = {
            'payer_id_address': payer.id_address,
            'payer_refund_address': payer.refund_address,
            'id_addresses': [payee.id_address for payee in payees],
            'payment_addresses': [payee.payment_address for payee in payees],
            'amounts': [payee.amount for payee in payees],
            'data': data
        }
        service = get_service_for_currency(currency)
        if role == Roles.PAYEE:
            method = getattr(service, 'create_request_as_payee')
        elif role == Roles.PAYER:
            method = getattr(service, 'create_request_as_payer')
            service_args['additional_payments'] = [p.additional_amount for p in payees]
            service_args['creation_payments'] = [p.payment_amount for p in payees]
        else:
            raise RoleNotSupported('{} is not a valid role'.format(role))

        return method(**service_args)

    def create_signed_request(self, role, currency, payees,
                              expiration_date, data=None):
        """ Create a signed Request instance

        :param role: Role of the signer - payer or payee (currently only payee is supported)
        :type role: types.Roles.PAYEE
        :param currency: The currency in which payment will be made
        :type currency: currency.Currency
        :param payees: List of Payee objects
        :type payees: [types.Payee]
        :param expiration_date: Unix timestamp after which Request can no longer be broadcast
        :param data: Optional dictionary of data which will be stored on IPFS
        :type data: dict
        :return: A Request instance
        :rtype: request_network.types.Request
        """
        if role != Roles.PAYEE:
            raise NotImplementedError('Signing Requests as the payer is not yet supported')

        service_args = {
            'id_addresses': [payee.id_address for payee in payees],
            'payment_addresses': [payee.payment_address for payee in payees],
            'amounts': [payee.amount for payee in payees],
            'expiration_date': expiration_date,
            'data': data
        }
        service = get_service_for_currency(currency)
        return service.sign_request_as_payee(**service_args)

    def broadcast_signed_request(self, signed_request, payer_address, payment_amounts=None,
                                 additional_payments=None):
        """ Broadcast a signed Request.

            Currently the Request API only supports signing requests as the payee,
            therefore this function only supports broadcasting a signed request
            as the payer.

        :param signed_request: The previously-signed Request to broadcast
        :type signed_request: types.Request
        :param payment_amounts: A list of integers specifying how much should be
            paid to each payee when the Request is created.
            The amount is in the currency of the Request.
        :type payment_amounts: [int]
        :param additional_payments: Additional amounts to pay on top of the `payment_amounts`.
        :type additional_payments: [int]
        :return: The transaction hash of the transaction which, if successfully
            included in a block, will create (and possibly pay, depending on `payment_amounts`)
            this Request.
        """
        am = ArtifactManager()
        service_class = am.get_service_class_by_address(signed_request.currency_contract_address)
        # currency = signed_request.currency_cont
        service_args = {
            'signed_request': signed_request,
            'payment_amounts': payment_amounts,
            'additional_payments': additional_payments,
            'payer_address': payer_address
        }
        service = service_class()
        return service.broadcast_signed_request_as_payer(**service_args)

    def get_request_by_id(self, request_id, block_number=None):
        """ Get a Request from its ID.

        :param request_id: The Request ID as a 32 byte hex string
        :param block_number: If provided, only search for Created events from this block onwards.
        :return: A Request instance
        :rtype: request_network.types.Request
        """
        core_contract_address = Web3.toChecksumAddress(request_id[:42])
        am = ArtifactManager()
        core_contract_data = am.get_contract_data(core_contract_address)

        core_contract = w3.eth.contract(
            address=core_contract_address,
            abi=core_contract_data['abi'])

        # Converts the data returned from 'RequestCore:getRequest' into a friendly object
        RequestContractData = namedtuple('RequestContractData', [
            'payer_address', 'currency_contract_address', 'state',
            'payee_id_address', 'amount', 'balance'
        ])

        try:
            request_data = RequestContractData(*core_contract.functions.getRequest(
                request_id).call())
        except ValueError:
            # web3 will raise a ValueError if the contract at core_contract_address is not
            # a valid contract address. This could happen if the given Request ID contains
            # an invalid core_contract_address, so we treat it as an invalid Request ID.
            raise RequestNotFound('Request ID {} has an invalid core contract address {}'.format(
                request_id,
                core_contract_address
            ))

        if request_data.payer_address == EMPTY_BYTES_20:
            raise RequestNotFound('Request ID {} not found on core contract {}'.format(
                request_id,
                core_contract_address
            ))

        # Payment addresses for payees are not stored with the Request in the contract,
        # so they need to be looked up separately
        service_contract = am.get_contract_instance(request_data.currency_contract_address)
        payees = [
            Payee(
                id_address=request_data.payee_id_address,
                amount=request_data.amount,
                balance=request_data.balance,
                payment_address=service_contract.functions.payeesPaymentAddress(
                    request_id, 0).call()
            )
        ]

        sub_payees_count = core_contract.functions.getSubPayeesCount(request_id).call()
        for i in range(sub_payees_count):
            (address, amount, balance) = core_contract.functions.subPayees(request_id, i).call()
            payment_address = service_contract.functions.payeesPaymentAddress(
                request_id, i + 1).call()
            payees.append(Payee(
                id_address=address,
                payment_address=payment_address,
                balance=balance,
                amount=amount
            ))

        # To find the creator and data for a Request we need to find the Created event
        # that was emitted when the Request was created
        # web3.py provides helpers for getting logs for a specific contract event but
        # they rely on `eth_newFilter` which is not supported on Infura. As a workaround
        # the logs are retrieved with `web3.eth`getLogs` which does not require a new
        # filter to be created.
        created_event_signature = Web3.toHex(event_abi_to_log_topic(
            event_abi=core_contract.events.Created().abi
        ))
        logs = w3.eth.getLogs({
            'fromBlock': block_number if block_number else core_contract_data['block_number'],
            'address': core_contract_address,
            'topics': [created_event_signature, request_id]
        })
        assert len(logs) == 1, "Incorrect number of logs returned"

        # Work around Solidity bug. See note in read_padded_data_from_stream.
        with mock.patch.object(
                StringDecoder,
                'read_data_from_stream',
                new=read_padded_data_from_stream):
            created_event_data = get_event_data(
                event_abi=core_contract.events.Created().abi,
                log_entry=logs[0]
            )

        # creator = log_data.args.creator
        # See if we have an IPFS hash, and get the file if so
        if created_event_data.args.data != '':
            ipfs_hash = created_event_data.args.data
            data = retrieve_ipfs_data(ipfs_hash)
        else:
            ipfs_hash = None
            data = {}

        # Iterate through UpdateBalance events to build a list of payments made for this request
        updated_event_signature = Web3.toHex(event_abi_to_log_topic(
            event_abi=core_contract.events.UpdateBalance().abi
        ))
        logs = w3.eth.getLogs({
            'fromBlock': block_number if block_number else core_contract_data['block_number'],
            'address': core_contract_address,
            'topics': [updated_event_signature, request_id]
        })

        payments = []
        for log in logs:
            event_data = get_event_data(
                event_abi=core_contract.events.UpdateBalance().abi,
                log_entry=log
            )
            payments.append(Payment(
                payee_index=event_data.args.payeeIndex,
                delta_amount=event_data.args.deltaAmount
            ))
            payees[event_data.args.payeeIndex].paid_amount += event_data.args.deltaAmount

        return Request(
            id=request_id,
            state=request_data.state,
            creator=created_event_data.args.creator,
            currency_contract_address=request_data.currency_contract_address,
            payer=request_data.payer_address,
            payees=payees,
            payments=payments,
            ipfs_hash=ipfs_hash,
            data=data,
            transaction_hash=Web3.toHex(created_event_data.transactionHash)
        )

    def get_request_by_transaction_hash(self, transaction_hash):
        """ Get a Request from an Ethereum transaction hash.

        :param transaction_hash: The hash of the transaction which created the Request
        :return: A Request instance
        :rtype: request_network.types.Request
        """
        tx_data = w3.eth.getTransaction(transaction_hash)
        if not tx_data:
            raise TransactionNotFound(transaction_hash)

        am = ArtifactManager()
        currency_contract = am.get_contract_instance(tx_data['to'])

        # Decode the transaction input data to get the function arguments
        func = currency_contract.get_function_by_selector(tx_data['input'][:10])
        arg_types = [i['type'] for i in func.abi['inputs']]
        arg_names = [i['name'] for i in func.abi['inputs']]
        arg_values = decode_abi(arg_types, Web3.toBytes(hexstr=tx_data['input'][10:]))
        function_args = dict(zip(arg_names, arg_values))

        # If this is a 'simple' Request we can take the ID from the transaction input.
        if '_requestId' in function_args:
            return self.get_request_by_id(
                Web3.toHex(function_args['_requestId']))

        # For more complex Requests (e.g. those created by broadcasting a signed Request)
        # we need to find the 'Created' event log that was emitted and take the ID from there.
        tx_receipt = w3.eth.getTransactionReceipt(transaction_hash)
        if not tx_receipt:
            raise Exception('TODO could not get tx receipt')

        # Extract the event args from the tx_receipt to retrieve the request_id
        core_contract = am.get_contract_instance(tx_receipt['logs'][0].address)
        # Work around Solidity bug. See note in read_padded_data_from_stream.
        with mock.patch.object(
                StringDecoder,
                'read_data_from_stream',
                new=read_padded_data_from_stream):
            logs = core_contract.events.Created().processReceipt(tx_receipt)
        request_id = logs[0].args.requestId

        return self.get_request_by_id(
            Web3.toHex(request_id),
            block_number=tx_data['blockNumber'])

    def get_request_events(self, request_id, from_block=None, to_block=None):
        """ Return a list of Events relating to the given request_id.

            The events follow the format used by `web3.utils.events.get_event_data`,
            except we decode the Request ID, transaction hash and block hash
            from bytes to hex strings.

        :param request_id:
        :param from_block:
        :param to_block:
        :return:
        """
        core_contract_address = Web3.toChecksumAddress(request_id[:42])
        am = ArtifactManager()
        core_contract_data = am.get_contract_data(core_contract_address)
        core_contract = core_contract_data['instance']

        event_names = ['Created', 'Accepted', 'Canceled', 'UpdateBalance',
                       'UpdateExpectedAmount', 'NewSubPayee']

        # Iterate through all available events, retrieving matching logs for
        # each. Iterate through logs and decode them according to the event's
        # ABI so we get an AttrDict containing all event data.

        # Events are temporarily stored in a dict(dict(list)) structure, so
        # they can be indexed by block number and log index. This is
        # required so we can return events in the order they were broadcast.
        events = defaultdict(lambda: defaultdict(list))
        for event_name in event_names:
            event_obj = getattr(core_contract.events, event_name)
            event_signature = Web3.toHex(event_abi_to_log_topic(
                event_abi=event_obj().abi))

            logs = w3.eth.getLogs({
                'fromBlock': from_block if from_block else core_contract_data['block_number'],
                'toBlock': to_block if to_block else w3.eth.blockNumber,
                'address': core_contract_data['address'],
                'topics': [event_signature, request_id]
            })
            for log in logs:
                # get_event_data returns an immutable AttributeDict, but we want
                # to decode some of the args. So we convert it to a dict, decode
                # some data, and then return a new AttributeDict.
                event_data = get_event_data(
                    event_abi=event_obj().abi,
                    log_entry=log
                ).__dict__
                event_data['args'] = event_data['args'].__dict__
                # Convert request ID, tx/block hash from bytes -> hex string
                event_data['args']['requestId'] = Web3.toHex(event_data['args']['requestId'])
                event_data['blockHash'] = Web3.toHex(event_data['blockHash'])
                event_data['transactionHash'] = Web3.toHex(event_data['transactionHash'])
                event_data['args'] = AttributeDict(dictionary=event_data['args'])

                events[event_data['blockNumber']][event_data['logIndex']].append(
                    AttributeDict(dictionary=event_data)
                )

        # Iterate through blocks, logs, and events to get a list of sorted events
        sorted_events = []
        for block in sorted(events.keys()):
            for log_index in sorted(events[block].keys()):
                for event in events[block][log_index]:
                    sorted_events.append(event)

        return sorted_events

    def pay_request(self, request_id, amounts,
                    additional_payments=None,
                    transaction_options=None):
        """ Pay a Request.

        :param request_id:
        :param amounts:
        :param additional_payments:
        :param transaction_options:
        :return:
        """
        # TODO validaton

        empty_payments = [0] * len(amounts)
        additional_payments = additional_payments if additional_payments else empty_payments

        request = self.get_request_by_id(request_id)

        service_args = {
            'request_id': request_id,
            'payment_amounts': amounts,
            'additional_payments': additional_payments,
            # TODO pass through entire transaction_options, refactor later
            'from_address': transaction_options['from']
        }
        service = self._get_service_for_request(request)
        return service.pay_request(**service_args)

    def _get_service_for_request(self, request):
        """ Returns an instance of the service class for a given Request.

        :param request: request_network.types.Request
        :return:
        """
        am = ArtifactManager()
        service_class = am.get_service_class_by_address(request.currency_contract_address)
        # TODO fix this later so we can pass in token_address for ERC20 service
        return service_class()

    def accept_request(self, request_id, transaction_options):
        """ Accept a Request.

        :param request_id:
        :param transaction_options:
        :return:
        """
        request = self.get_request_by_id(request_id)
        service = self._get_service_for_request(request)
        service_args = {
            'request_id': request_id,
            'payer_address': transaction_options['from']  # TODO
        }
        return service.accept_request(**service_args)

    def cancel_request(self, request_id, transaction_options):
        """ Cancel a Request.

        :param request_id:
        :param transaction_options:
        :return:
        """
        request = self.get_request_by_id(request_id)
        service = self._get_service_for_request(request)
        service_args = {
            'request_id': request_id,
            'from_address': transaction_options['from']  # TODO
        }
        return service.cancel_request(**service_args)

    def refund_request(self, request_id, refund_amount, transaction_options):
        """ Refund a Request.

        :param request_id:
        :param refund_amount:
        :param transaction_options:
        :return:
        """
        request = self.get_request_by_id(request_id)
        service = self._get_service_for_request(request)
        service_args = {
            'request_id': request_id,
            'refund_amount': refund_amount,
            'from_address': transaction_options['from']  # TODO
        }
        return service.refund_request(**service_args)

    def add_additional_payment(self, request_id, amounts, transaction_options):
        """ Add additional payments to an existing Request.

        :param request_id:
        :param amounts:
        :param transaction_options:
        :return:
        """
        request = self.get_request_by_id(request_id)
        service = self._get_service_for_request(request)
        service_args = {
            'request_id': request_id,
            'amounts': amounts,
            'from_address': transaction_options['from']  # TODO
        }
        return service.add_additional_payment(**service_args)

    def add_discount(self, request_id, amounts, transaction_options):
        """ Add a discount to an existing Request.

        :param request_id:
        :param amounts:
        :param transaction_options:
        :return:
        """
        request = self.get_request_by_id(request_id)
        service = self._get_service_for_request(request)
        service_args = {
            'request_id': request_id,
            'amounts': amounts,
            'from_address': transaction_options['from']  # TODO
        }
        return service.add_discount(**service_args)


def read_padded_data_from_stream(self, stream):
    """ This function exists to work around a bug in Solidity:
        https://github.com/ethereum/web3.py/issues/602
        https://github.com/ethereum/solidity/issues/3493

        Data from logs differs if the event is emitted during an external
        or internal solidity function call.

        The workaround is to pad the data until if fits the padded length.

    :param self:
    :param stream:
    :return:
    """
    from eth_abi.utils.numeric import ceil32
    data_length = decode_uint_256(stream)
    padded_length = ceil32(data_length)

    data = stream.read(padded_length)

    # Start change
    # Manually pad data to force it to desired length
    if len(data) < padded_length:
        data += b'\x00' * (padded_length - data_length)
    # End change

    if len(data) < padded_length:
        from eth_abi.exceptions import InsufficientDataBytes
        raise InsufficientDataBytes(
            "Tried to read {0} bytes.  Only got {1} bytes".format(
                padded_length,
                len(data),
            )
        )

    padding_bytes = data[data_length:]

    if padding_bytes != b'\x00' * (padded_length - data_length):
        from eth_abi.exceptions import NonEmptyPaddingBytes
        raise NonEmptyPaddingBytes(
            "Padding bytes were not empty: {0}".format(repr(padding_bytes))
        )

    return data[:data_length]
