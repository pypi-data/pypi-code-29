from enum import Enum
from logging import getLogger
from typing import List, Set, Tuple

import eth_abi
from django_eth.constants import NULL_ADDRESS
from ethereum.utils import check_checksum, sha3
from hexbytes import HexBytes
from py_eth_sig_utils import encode_typed_data
from web3.exceptions import BadFunctionCallOutput

from .contracts import (get_paying_proxy_contract,
                        get_paying_proxy_deployed_bytecode,
                        get_safe_contract)
from .ethereum_service import EthereumService, EthereumServiceProvider
from .safe_creation_tx import SafeCreationTx

logger = getLogger(__name__)


class SafeServiceException(Exception):
    pass


class InvalidMultisigTx(SafeServiceException):
    pass


class NotEnoughFundsForMultisigTx(SafeServiceException):
    pass


class InvalidRefundReceiver(SafeServiceException):
    pass


class InvalidProxyContract(SafeServiceException):
    pass


class InvalidMasterCopyAddress(SafeServiceException):
    pass


class SafeGasEstimationError(SafeServiceException):
    pass


class SignatureNotProvidedByOwner(SafeServiceException):
    pass


class CannotPayGasWithEther(SafeServiceException):
    pass


class InvalidChecksumAddress(SafeServiceException):
    pass


class SafeOperation(Enum):
    CALL = 0
    DELEGATE_CALL = 1
    CREATE = 2


class SafeServiceProvider:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            from django.conf import settings
            ethereum_service = EthereumServiceProvider()
            cls.instance = SafeService(ethereum_service,
                                       settings.SAFE_CONTRACT_ADDRESS,
                                       settings.SAFE_VALID_CONTRACT_ADDRESSES,
                                       settings.SAFE_TX_SENDER_PRIVATE_KEY,
                                       settings.SAFE_FUNDER_PRIVATE_KEY)
        return cls.instance

    @classmethod
    def del_singleton(cls):
        if hasattr(cls, "instance"):
            del cls.instance


class SafeTeamServiceProvider:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            from django.conf import settings
            ethereum_service = EthereumServiceProvider()
            cls.instance = SafeTeamService(ethereum_service,
                                           settings.SAFE_TEAM_CONTRACT_ADDRESS,
                                           settings.SAFE_TEAM_VALID_CONTRACT_ADDRESSES,
                                           settings.SAFE_TX_SENDER_PRIVATE_KEY,
                                           settings.SAFE_FUNDER_PRIVATE_KEY)
        return cls.instance

    @classmethod
    def del_singleton(cls):
        if hasattr(cls, "instance"):
            del cls.instance


class SafeService:
    def __init__(self, ethereum_service: EthereumService,
                 master_copy_address: str,
                 valid_master_copy_addresses: Set[str],
                 tx_sender_private_key: str=None,
                 funder_private_key: str=None):
        self.ethereum_service = ethereum_service
        self.w3 = self.ethereum_service.w3

        for address in [master_copy_address] + list(valid_master_copy_addresses):
            if address and not check_checksum(address):
                raise InvalidChecksumAddress

        self.master_copy_address = master_copy_address
        self.valid_master_copy_addresses = set(valid_master_copy_addresses)
        if master_copy_address:
            self.valid_master_copy_addresses.add(master_copy_address)
        else:
            logger.warning('Master copy address for SafeService is None')

        self.tx_sender_private_key = tx_sender_private_key
        self.funder_private_key = funder_private_key
        if self.funder_private_key:
            self.funder_address = self.ethereum_service.private_key_to_address(self.funder_private_key)
        else:
            self.funder_address = None

    def get_contract(self, safe_address=None):
        if safe_address:
            return get_safe_contract(self.w3, address=safe_address)
        else:
            return get_safe_contract(self.w3)

    def build_safe_creation_tx(self, s: int, owners: List[str], threshold: int, gas_price: int) -> SafeCreationTx:
        safe_creation_tx = SafeCreationTx(w3=self.w3,
                                          owners=owners,
                                          threshold=threshold,
                                          signature_s=s,
                                          master_copy=self.master_copy_address,
                                          gas_price=gas_price,
                                          funder=self.funder_address)

        assert safe_creation_tx.contract_creation_tx.nonce == 0
        return safe_creation_tx

    def deploy_master_contract(self, deployer_account=None, deployer_private_key=None) -> str:
        """
        Deploy master contract. Takes deployer_account (if unlocked in the node) or the deployer private key
        :param deployer_account: Unlocked ethereum account
        :param deployer_private_key: Private key of an ethereum account
        :return: deployed contract address
        """
        assert deployer_account or deployer_private_key

        safe_personal_contract = self.get_contract()
        constructor = safe_personal_contract.constructor()
        gas = 6000000

        if deployer_private_key:
            deployer_account = self.ethereum_service.private_key_to_address(deployer_private_key)
            tx = constructor.transact({'gas': gas}).buildTransaction()
            signed_tx = self.w3.eth.account.signTransaction(tx, private_key=deployer_private_key)
            tx_hash = self.ethereum_service.send_raw_transaction(signed_tx.rawTransaction)
        else:
            tx_hash = constructor.transact({'from': deployer_account, 'gas': gas})

        tx_receipt = self.ethereum_service.get_transaction_receipt(tx_hash, timeout=60)
        assert tx_receipt.status

        contract_address = tx_receipt.contractAddress

        # Init master copy
        master_safe = self.get_contract(contract_address)
        setup_function = master_safe.functions.setup(
            # We use 2 owners that nobody controls for the master copy
            ["0x0000000000000000000000000000000000000002", "0x0000000000000000000000000000000000000003"],
            # Maximum security
            2,
            NULL_ADDRESS,
            b''
        )

        if deployer_private_key:
            tx = setup_function.transact({'gas': gas}).buildTransaction()
            signed_tx = self.w3.eth.account.signTransaction(tx, private_key=deployer_private_key)
            tx_hash = self.ethereum_service.send_raw_transaction(signed_tx.rawTransaction)
        else:
            tx_hash = setup_function.transact({'from': deployer_account})

        tx_receipt = self.ethereum_service.get_transaction_receipt(tx_hash, timeout=60)
        assert tx_receipt.status

        logger.info("Deployed and initialized Safe Master Contract=%s by %s", contract_address, deployer_account)
        return contract_address

    def deploy_proxy_contract(self, deployer_account=None, deployer_private_key=None) -> str:
        """
        Deploy proxy contract. Takes deployer_account (if unlocked in the node) or the deployer private key
        :param deployer_account: Unlocked ethereum account
        :param deployer_private_key: Private key of an ethereum account
        :return: deployed contract address
        """
        assert deployer_account or deployer_private_key

        safe_proxy_contract = get_paying_proxy_contract(self.w3)
        constructor = safe_proxy_contract.constructor(self.master_copy_address, b'', NULL_ADDRESS, NULL_ADDRESS, 0)
        gas = 5125602

        if deployer_account:
            tx_hash = constructor.transact({'from': deployer_account, 'gas': gas})
        else:
            tx = constructor.transact({'gas': gas}).buildTransaction()
            signed_tx = self.w3.eth.account.signTransaction(tx, private_key=deployer_private_key)
            tx_hash = self.ethereum_service.send_raw_transaction(signed_tx.rawTransaction)

        tx_receipt = self.ethereum_service.get_transaction_receipt(tx_hash, timeout=60)

        contract_address = tx_receipt.contractAddress
        return contract_address

    def check_master_copy(self, address) -> bool:
        master_copy_address = self.retrieve_master_copy_address(address)
        return master_copy_address in self.valid_master_copy_addresses

    def check_proxy_code(self, address) -> bool:
        """
        Check if proxy is valid
        :param address: address of the proxy
        :return: True if proxy is valid, False otherwise
        """
        deployed_proxy_code = self.w3.eth.getCode(address)
        proxy_code = get_paying_proxy_deployed_bytecode()

        return deployed_proxy_code == proxy_code

    def get_gas_token(self):
        return NULL_ADDRESS

    def get_refund_receiver(self):
        return NULL_ADDRESS

    def retrieve_master_copy_address(self, safe_address) -> str:
        return get_paying_proxy_contract(self.w3, safe_address).functions.implementation().call(
            block_identifier='pending')

    def retrieve_nonce(self, safe_address) -> int:
        return self.get_contract(safe_address).functions.nonce().call(block_identifier='pending')

    def retrieve_threshold(self, safe_address) -> int:
        return self.get_contract(safe_address).functions.getThreshold().call(block_identifier='pending')

    def estimate_tx_gas(self, safe_address: str, to: str, value: int, data: bytes, operation: int) -> int:
        data = data or b''
        # Add 10k else we will fail in case of nested calls
        base_gas = 10000
        try:
            tx = self.get_contract(safe_address).functions.requiredTxGas(
                to,
                value,
                data,
                operation
            ).buildTransaction({
                'from': safe_address,
                'gas': 5000000
            })
            # If we build the tx web3 will not try to decode it for us
            result = self.w3.eth.call(tx, block_identifier='pending').hex()
            # 2 - 0x
            # 8 - error method id
            # 64 - position
            # 64 - length
            estimated_gas_hex = result[138:]

            # Estimated gas in hex must be 64
            if len(estimated_gas_hex) != 64:
                logger.warning('Exception estimating gas, returned value is %s', result)
                raise SafeGasEstimationError(result)

            estimated_gas = int(estimated_gas_hex, 16)
            return estimated_gas + base_gas
        except ValueError as e:
            data = e.args[0]['data']
            key = list(data.keys())[0]
            result = data[key]['return']
            if result == '0x0':
                raise e
            else:
                # Ganache-Cli with no `--noVMErrorsOnRPCResponse` flag enabled
                logger.warning('You should use `--noVMErrorsOnRPCResponse` flag with Ganache-cli')
                estimated_gas_hex = result[138:]
                assert len(estimated_gas_hex) == 64
                estimated_gas = int(estimated_gas_hex, 16)
                return estimated_gas + base_gas

    def estimate_tx_data_gas(self, safe_address: str, to: str, value: int, data: bytes,
                             operation: int, estimate_tx_gas: int):
        data = data or b''
        paying_proxy_contract = self.get_contract(safe_address)
        threshold = self.retrieve_threshold(safe_address)
        nonce = self.retrieve_nonce(safe_address)

        # Calculate gas for signatures
        signature_gas = threshold * (1 * 68 + 2 * 32 * 68)

        safe_tx_gas = estimate_tx_gas
        data_gas = 0
        gas_price = 1
        gas_token = NULL_ADDRESS
        signatures = b''
        refund_receiver = NULL_ADDRESS
        data = HexBytes(paying_proxy_contract.functions.execTransaction(
            to,
            value,
            data,
            operation,
            safe_tx_gas,
            data_gas,
            gas_price,
            gas_token,
            refund_receiver,
            signatures,
        ).buildTransaction({
            'gas': 1,
            'gasPrice': 1,
            'nonce': nonce
        })['data'])

        data_gas = signature_gas + self.ethereum_service.estimate_data_gas(data)

        # Add aditional gas costs
        if data_gas > 65536:
            data_gas += 64
        else:
            data_gas += 128

        data_gas += 32000  # Base tx costs, transfer costs...

        return data_gas

    def check_funds_for_tx_gas(self, safe_address: str, gas: int, data_gas: int, gas_price: int, gas_token: str
                               )-> bool:
        """
        Check safe has enough funds to pay for a tx
        :param safe_address: Address of the safe
        :param gas: Start gas
        :param data_gas: Data gas
        :param gas_price: Gas Price
        :param gas_token: Gas Token, still not supported. Must be the NULL address
        :return: True if enough funds, False, otherwise
        """
        # Gas token is still not supported
        assert gas_token == NULL_ADDRESS

        balance = self.ethereum_service.get_balance(safe_address)
        return balance >= ((gas + data_gas) * gas_price)

    def check_refund_receiver(self, refund_receiver: str) -> bool:
        # We only support tx.origin as refund receiver right now
        # In the future we can also accept transactions where it is set to our service account to receive the payments.
        # This would prevent that anybody can front-run our service
        return refund_receiver == NULL_ADDRESS

    def send_multisig_tx(self,
                         safe_address: str,
                         to: str,
                         value: int,
                         data: bytes,
                         operation: int,
                         safe_tx_gas: int,
                         data_gas: int,
                         gas_price: int,
                         gas_token: str,
                         refund_receiver: str,
                         signatures: bytes,
                         tx_sender_private_key=None,
                         tx_gas=None,
                         tx_gas_price=None) -> Tuple[str, any]:

        data = data or b''
        gas_token = gas_token or NULL_ADDRESS
        refund_receiver = refund_receiver or NULL_ADDRESS
        to = to or NULL_ADDRESS

        # Make sure refund receiver is set to 0x0 so that the contract refunds the gas costs to tx.origin
        if not self.check_refund_receiver(refund_receiver):
            raise InvalidRefundReceiver(refund_receiver)

        # Make sure proxy contract is ours
        if not self.check_proxy_code(safe_address):
            raise InvalidProxyContract(safe_address)

        # Make sure master copy is updated
        if not self.check_master_copy(safe_address):
            raise InvalidMasterCopyAddress

        # Check enough funds to pay for the gas
        if not self.check_funds_for_tx_gas(safe_address, safe_tx_gas, data_gas, gas_price, gas_token):
            raise NotEnoughFundsForMultisigTx

        tx_gas = tx_gas or (safe_tx_gas + data_gas) * 2

        # Use wrapped tx gas_price if not provided
        tx_gas_price = tx_gas_price or gas_price
        tx_sender_private_key = tx_sender_private_key or self.tx_sender_private_key

        safe_contract = get_safe_contract(self.w3, address=safe_address)
        try:
            success = safe_contract.functions.execTransaction(
                to,
                value,
                data,
                operation,
                safe_tx_gas,
                data_gas,
                gas_price,
                gas_token,
                refund_receiver,
                signatures,
            ).call(block_identifier='pending')

            if not success:
                raise InvalidMultisigTx
        except BadFunctionCallOutput as exc:
            str_exc = str(exc)
            if 'Signature not provided by owner' in str_exc:
                raise SignatureNotProvidedByOwner
            elif 'Could not pay gas costs with ether' in str_exc:
                raise CannotPayGasWithEther

        tx_sender_address = self.ethereum_service.private_key_to_address(tx_sender_private_key)

        tx = safe_contract.functions.execTransaction(
            to,
            value,
            data,
            operation,
            safe_tx_gas,
            data_gas,
            gas_price,
            gas_token,
            refund_receiver,
            signatures,
        ).buildTransaction({
            'from': tx_sender_address,
            'gas': tx_gas,
            'gasPrice': tx_gas_price,
            'nonce': self.ethereum_service.get_nonce_for_account(tx_sender_address)
        })

        tx_signed = self.w3.eth.account.signTransaction(tx, tx_sender_private_key)

        return self.w3.eth.sendRawTransaction(tx_signed.rawTransaction), tx

    @staticmethod
    def get_hash_for_safe_tx(safe_address: str, to: str, value: int, data: bytes,
                             operation: int, safe_tx_gas: int, data_gas: int, gas_price: int,
                             gas_token: str, refund_receiver: str, nonce: int) -> HexBytes:

        data = data.hex() if data else ''
        gas_token = gas_token or NULL_ADDRESS
        refund_receiver = refund_receiver or NULL_ADDRESS
        to = to or NULL_ADDRESS

        data = {
                "types": {
                    "EIP712Domain": [
                        { "name": 'verifyingContract', "type": 'address' },
                    ],
                    "SafeTx": [
                        { "name": 'to', "type": 'address' },
                        { "name": 'value', "type": 'uint256' },
                        { "name": 'data', "type": 'bytes' },
                        { "name": 'operation', "type": 'uint8' },
                        { "name": 'safeTxGas', "type": 'uint256' },
                        { "name": 'dataGas', "type": 'uint256' },
                        { "name": 'gasPrice', "type": 'uint256' },
                        { "name": 'gasToken', "type": 'address' },
                        { "name": 'refundReceiver', "type": 'address' },
                        { "name": 'nonce', "type": 'uint256' }
                    ]
                },
                "primaryType": 'SafeTx',
                "domain": {
                    "verifyingContract": safe_address,
                },
                "message": {
                    "to": to,
                    "value": value,
                    "data": data,
                    "operation": operation,
                    "safeTxGas": safe_tx_gas,
                    "dataGas": data_gas,
                    "gasPrice": gas_price,
                    "gasToken": gas_token,
                    "refundReceiver": refund_receiver,
                    "nonce": nonce,
                },
            }

        return HexBytes(encode_typed_data(data))

    def check_hash(self, tx_hash: str, signatures: bytes, owners: List[str]) -> bool:
        for i, owner in enumerate(sorted(owners, key=lambda x: x.lower())):
            v, r, s = self.signature_split(signatures, i)
            if self.ethereum_service.get_signing_address(tx_hash, v, r, s) != owner:
                return False
        return True

    @staticmethod
    def signature_split(signatures: bytes, pos: int) -> Tuple[int, int, int]:
        """
        :param signatures: signatures in form of {bytes32 r}{bytes32 s}{uint8 v}
        :param pos: position of the signature
        :return: Tuple with v, r, s
        """
        signature_pos = 65 * pos
        v = signatures[64 + signature_pos]
        r = int.from_bytes(signatures[signature_pos:32 + signature_pos], 'big')
        s = int.from_bytes(signatures[32 + signature_pos:64 + signature_pos], 'big')

        return v, r, s

    @classmethod
    def signatures_to_bytes(cls, signatures: List[Tuple[int, int, int]]) -> bytes:
        """
        Convert signatures to bytes
        :param signatures: list of v, r, s
        :return: 65 bytes per signature
        """
        return b''.join([cls.signature_to_bytes(vrs) for vrs in signatures])

    @staticmethod
    def signature_to_bytes(vrs: Tuple[int, int, int]) -> bytes:
        """
        Convert signature to bytes
        :param vrs: tuple of v, r, s
        :return: signature in form of {bytes32 r}{bytes32 s}{uint8 v}
        """

        byte_order = 'big'

        v, r, s = vrs

        return (r.to_bytes(32, byteorder=byte_order) +
                s.to_bytes(32, byteorder=byte_order) +
                v.to_bytes(1, byteorder=byte_order))
