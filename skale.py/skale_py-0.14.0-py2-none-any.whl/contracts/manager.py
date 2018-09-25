from web3 import Web3
import socket
import logging

from skale.contracts import BaseContract
import skale.utils.helper as Helper
from skale.utils.helper import sign_and_send

from skale.utils.constants import NODE_DEPOSIT, GAS, OP_TYPES

logger = logging.getLogger(__name__)


class Manager(BaseContract):

    def create_node(self, ip, port, name, wallet):
        logger.info(f'create_node: {ip}:{port}, name: {name}')

        token = self.skale.get_contract_by_name('token')
        skale_nonce = Helper.generate_nonce()
        transaction_data = self.create_node_data_to_bytes(ip, port, name, wallet['address'], skale_nonce)

        op = token.contract.functions.transfer(self.address, NODE_DEPOSIT, transaction_data)
        tx = sign_and_send(self.skale, op, GAS['create_node'], wallet)
        return {'tx': tx, 'nonce': skale_nonce}

    def create_node_data_to_bytes(self, ip, port, name, address, nonce):
        address_fx = Web3.toChecksumAddress(address)[2:]  # fix & cut 0x

        type_bytes = OP_TYPES['create_node'].to_bytes(1, byteorder='big')
        port_bytes = port.to_bytes(4, byteorder='big')
        nonce_bytes = nonce.to_bytes(4, byteorder='big')  # todo
        ip_bytes = socket.inet_aton(ip)
        address_bytes = bytes.fromhex(address_fx)
        name_bytes = name.encode()

        data_bytes = type_bytes + port_bytes + nonce_bytes + ip_bytes + address_bytes + name_bytes
        logger.info(f'create_node_data_to_bytes bytes: {self.skale.web3.toHex(data_bytes)}')

        return data_bytes

    def get_bounty(self, node_id, wallet):
        op = self.contract.functions.getBounty(node_id)
        tx = sign_and_send(self.skale, op, GAS['get_bounty'], wallet)
        return {'tx': tx}

    def send_verdict(self, validator, node_id, downtime, latency, wallet):
        op = self.contract.functions.sendVerdict(validator, node_id, downtime, latency)
        tx = sign_and_send(self.skale, op, GAS['send_verdict'], wallet)
        return {'tx': tx}

    def get_node_next_reward_date(self, node_index):
        return self.contract.functions.getNodeNextRewardDate(node_index).call()