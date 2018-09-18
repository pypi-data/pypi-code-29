

def GetBlockchain():
    from kaze.Core.Blockchain import Blockchain
    return Blockchain.Default()


def GetGenesis():
    from kaze.Core.Blockchain import Blockchain
    return Blockchain.GenesisBlock()


def GetSystemCoin():
    from kaze.Core.Blockchain import Blockchain
    return Blockchain.SystemCoin()


def GetSystemShare():
    from kaze.Core.Blockchain import Blockchain
    return Blockchain.SystemShare()


def GetStateReader():
    from kaze.SmartContract.StateReader import StateReader
    return StateReader()


def GetConsensusAddress(validators):
    from kaze.Core.Blockchain import Blockchain
    return Blockchain.GetConsensusAddress(validators)
