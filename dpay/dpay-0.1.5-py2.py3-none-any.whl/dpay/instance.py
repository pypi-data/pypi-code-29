import dpay as stm
import sys

_shared_dpayd_instance = None


def get_config_node_list():
    from dpaybase.storage import configStorage
    nodes = configStorage.get('nodes', None)
    if nodes:
        return nodes.split(',')


def shared_dpayd_instance():
    """ This method will initialize _shared_dpayd_instance and return it.
    The purpose of this method is to have offer single default dPay
    instance that can be reused by multiple classes.  """

    global _shared_dpayd_instance
    if not _shared_dpayd_instance:
        if sys.version >= '3.0':
            _shared_dpayd_instance = stm.dpayd.DPayd(
                nodes=get_config_node_list())
        else:
            _shared_dpayd_instance = stm.DPayd(
                nodes=get_config_node_list())
    return _shared_dpayd_instance


def set_shared_dpayd_instance(dpayd_instance):
    """ This method allows us to override default dPay instance for all
    users of _shared_dpayd_instance.  """

    global _shared_dpayd_instance
    _shared_dpayd_instance = dpayd_instance
