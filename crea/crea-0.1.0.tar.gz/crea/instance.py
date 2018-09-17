import crea as stm
import sys

_shared_cread_instance = None


def get_config_node_list():
    from creabase.storage import configStorage
    nodes = configStorage.get('nodes', None)
    if nodes:
        return nodes.split(',')


def shared_cread_instance():
    """ This method will initialize _shared_cread_instance and return it.
    The purpose of this method is to have offer single default Crea
    instance that can be reused by multiple classes.  """

    global _shared_cread_instance
    if not _shared_cread_instance:
        if sys.version >= '3.0':
            _shared_cread_instance = stm.cread.Cread(
                nodes=get_config_node_list())
        else:
            _shared_cread_instance = stm.Cread(
                nodes=get_config_node_list())
    return _shared_cread_instance


def set_shared_cread_instance(cread_instance):
    """ This method allows us to override default Crea instance for all
    users of _shared_cread_instance.  """

    global _shared_cread_instance
    _shared_cread_instance = cread_instance
