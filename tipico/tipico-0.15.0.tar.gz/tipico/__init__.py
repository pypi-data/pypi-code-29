from tipico.types.instrument_status import InstrumentStatus
from tipico.utils.constants import Constants


def _getDefaultConfigFilePath():
    from plico.utils.config_file_manager import ConfigFileManager
    cfgFileMgr= ConfigFileManager(Constants.APP_NAME,
                                  Constants.APP_AUTHOR,
                                  Constants.THIS_PACKAGE)
    return cfgFileMgr.getConfigFilePath()


defaultConfigFilePath= _getDefaultConfigFilePath()



def instrument(hostname, port):

    from tipico.client.instrument_client import InstrumentClient
    from plico.rpc.zmq_remote_procedure_call import ZmqRemoteProcedureCall
    from plico.rpc.zmq_ports import ZmqPorts
    from plico.rpc.sockets import Sockets


    rpc= ZmqRemoteProcedureCall()
    zmqPorts= ZmqPorts(hostname, port)
    sockets= Sockets(zmqPorts, rpc)
    return InstrumentClient(rpc, sockets)
