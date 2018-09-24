from skale.contracts import BaseContract
from skale.utils.helper import format

class Nodes(BaseContract):
    fields =  ['owner', 'name', 'ip', 'port', 'last_reward_date', 'leaving_date', 'start_date']

    def __get_raw(self, node_id):
        return self.contract.functions.getNode(node_id).call()

    @format(fields)
    def get(self, node_id):
        return self.__get_raw(node_id)

    def get_active_node_ids(self):
        return self.contract.functions.getActiveNodeIds().call()

    def get_active_node_ips(self):
        return self.contract.functions.getActiveNodeIPs().call()

    def get_active_nodes_by_address(self, account):
        return self.contract.functions.getActiveNodesByAddress().call({'from': account})