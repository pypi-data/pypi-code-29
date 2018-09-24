from skale.contracts import BaseContract
from skale.utils.helper import format, ip_from_bytes

class SChains(BaseContract):
    fields = [
        'owner',
        'name',
        'storageBytes',
        'cpu',
        'transactionThroughput',
        'lifetime',
        'creationDate',
        'maxNodes',
        'deposit'
    ]

    def __get_raw(self, name):
        return self.contract.functions.getSchain(name).call()

    @format(fields)
    def get(self, name):
        return self.__get_raw(name)

    def __get_schain_nodes_raw(self, schain_name):
        return self.contract.functions.getSchainNodes(schain_name).call()

    def get_schain_nodes(self, schain_name):
        nodes = []
        raw_nodes = self.__get_schain_nodes_raw(schain_name)

        for i, node in enumerate(raw_nodes):
            node_id_bytes = node[0:10]
            node_id = int.from_bytes(node_id_bytes, byteorder='big')

            ip_bytes = node[10:14]
            ip = ip_from_bytes(ip_bytes)

            port_bytes = node[14:16]
            port = int.from_bytes(port_bytes, byteorder='big')

            nodes.append({
                'schainIndex': i,
                'nodeID': node_id,
                'ip': ip,
                'basePort': port
            })
        return nodes

    def get_schain_list_size(self, account):
        return self.contract.functions.getSchainListSize().call({'from': account})

    def get_schain_by_index(self, index):
        return self.contract.functions.getSchainByIndex(index).call()

    def get_schain_name_by_schain_id(self, schain_id):
        return self.contract.functions.getSchainNameBySchainId(schain_id).call()

    def get_schain_ids_for_node(self, node_id):
        return self.contract.functions.getSchainIdsForNode(node_id).call()

    def get_schains_for_node(self, node_id):
        schains = []
        schain_contract = self.skale.get_contract_by_name('schains')
        schain_ids = self.get_schain_ids_for_node(node_id)
        for schain_id in schain_ids:
            name = self.get_schain_name_by_schain_id(schain_id)
            schain = schain_contract.get(name)
            schains.append(schain)
        return schains
