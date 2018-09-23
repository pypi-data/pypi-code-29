import json
from web3 import Web3, HTTPProvider

from layer import config
from layer.common import web3_sign

# Layer contract address, abi 
layerContractAddress = Web3.toChecksumAddress(config.LAYER_CONTRACT_ADDRESS)
layerContractAbi = config.LAYER_CONTRACT_ABI

# Claim issuer contract address, abi
claimContractAddress = Web3.toChecksumAddress(config.CLAIM_CONTRACT_ADDRESS)
claimContractAbi = config.CLAIM_CONTRACT_ABI

# User contract abi only
userContractAbi = config.USER_CONTRACT_ABI


DEFAULT_WEB3_PROVIDER = config.DEFAULT_WEB3_PROVIDER

ENUM_CLAIM_TYPE = ['email', 'phone', 'cc']
ENUM_SCHEME_TYPE = ['ecdsa', 'dsa', 'rsa']

class Contracts:
    __w3 = None
    layer_contract = None
    claim_contract = None

    def __init__(self, geth_rpc_host=DEFAULT_WEB3_PROVIDER):
        w3 = Web3(HTTPProvider(geth_rpc_host))
        print('w3.isConnected', w3.isConnected())
        self.__w3 = w3
        self.layer_contract = self.__w3.eth.contract(
            address=layerContractAddress, abi=layerContractAbi
        )
        self.claim_contract = self.__w3.eth.contract(
            address=claimContractAddress, abi=claimContractAbi
        )

    def getBlockNumber(self):
        return self.__w3.eth.blockNumber

    def getLayerNodes(self):
        return self.layer_contract.functions.getLayerNodes().call()

    def getLayerNodeByAddress(self, addr):
        try:
            addr = Web3.toChecksumAddress(addr)
        except Exception:
            return None

        try:
            info = self.layer_contract.functions.getLayerNodeByAddress(
                addr).call()
            return {
                'address': info[0],
                'url': info[1],
                'approved': info[2]
            }
        except Exception:
            return None

    def getProviders(self):
        return self.layer_contract.functions.getProviders().call()

    def getProviderByAddress(self, addr):
        try:
            addr = Web3.toChecksumAddress(addr)
        except Exception:
            return None

        try:
            info = self.layer_contract.functions.getProviderByAddress(
                addr).call()
            return {
                'address': info[0],
                'name': info[1],
                'approved': info[2],
                'category': info[3],
            }
        except Exception:
            return None
 
    def owner(self):
        return self.layer_contract.functions.owner().call()

    # setter

    def transferOwnership(self, newOwner):
        return self.layer_contract.functions.transferOwnership(newOwner).call()

    def addLayerNode(self, my_address, my_privKey, address, url):
        try:
            my_address = Web3.toChecksumAddress(my_address)
        except Exception:
            return 'invalid my_address', None

        if not my_privKey:
            return 'empty my_privKey', None

        try:
            address = Web3.toChecksumAddress(address)
        except Exception:
            return 'invalid address', None

        if not url:
            return 'empty url', None

        try:
            encodedABI = self.layer_contract.encodeABI(
                fn_name='addLayerNode', args=[address, url])
            gasPrice = self.__w3.eth.gasPrice
            gasEstimate = self.__w3.eth.estimateGas(
                {'from': my_address, 'to': layerContractAddress, 'data': encodedABI})
            signed_txn = self.__w3.eth.account.signTransaction(dict(
                nonce=self.__w3.eth.getTransactionCount(my_address),
                gasPrice=self.__w3.eth.gasPrice,
                # gas=2000000,
                gas=gasEstimate,
                to=layerContractAddress,
                value=0,
                data=encodedABI,
            ), my_privKey,)
            tx_hash = self.__w3.eth.sendRawTransaction(
                signed_txn.rawTransaction)
            return None, tx_hash
        except Exception as e:
            # print('encodeABI error: ', e)
            return str(e), None

    def addProvider(self, my_address, my_privKey, address, name, approved, category):
        try:
            my_address = Web3.toChecksumAddress(my_address)
        except Exception:
            return 'invalid my_address', None

        if not my_privKey:
            return 'empty my_privKey', None

        try:
            address = Web3.toChecksumAddress(address)
        except Exception:
            return 'invalid address', None

        if not name:
            return 'empty name', None

        if not category:
            return 'empty category', None

        try:
            encodedABI = self.layer_contract.encodeABI(
                fn_name='addProvider', args=[address, name, approved, category])
            gasPrice = self.__w3.eth.gasPrice
            gasEstimate = self.__w3.eth.estimateGas(
                {'from': my_address, 'to': layerContractAddress, 'data': encodedABI})
            signed_txn = self.__w3.eth.account.signTransaction(dict(
                nonce=self.__w3.eth.getTransactionCount(my_address),
                gasPrice=self.__w3.eth.gasPrice,
                # gas=2000000,
                gas=gasEstimate,
                to=layerContractAddress,
                value=0,
                data=encodedABI,
            ), my_privKey,)
            tx_hash = self.__w3.eth.sendRawTransaction(
                signed_txn.rawTransaction)
            return None, tx_hash
        except Exception as e:
            # print('encodeABI error: ', e)
            return str(e), None


    def addClaim(self, issuer, issuerPrivateKey, user, userContractAddress, claimType, scheme, data, url=""):
        """Add claim of identity to a user

        Args:
            issuer (str): ETH address of the issuer
            issuerPrivateKey (str): ETH private key of the issuer
            user (str): ETH address of user to claim
            userContractAddress (str): Deployed user contract address to call
            claimType (str): Verify method used in claiming (i.e. 'email' or 'phone')
            scheme (str): Algorithm used in signature generation
            data (bytes): data used in claim (i.e user email address or phone number)
            url (str): Reference url

        Returns:
            err(str): Error string if any error, otherwise None
            txHash(str): Transaction Hash if succeeded, None if error
        """
        try:
            # Validate issuer, issuer private key, user, user contract address
            issuer = Web3.toChecksumAddress(issuer)
            user = Web3.toChecksumAddress(user)
            userContractAddress = Web3.toChecksumAddress(userContractAddress)

            if not issuer:
                raise Exception('Invalid issuer address')
            if not issuerPrivateKey:
                raise Exception('Invalid issuer private key')
            if not user:
                raise Exception('Invalid user address')
            if not userContractAddress:
                raise Exception('Invalid user contract address')

            # Validate claim data
            if claimType not in ENUM_CLAIM_TYPE:
                raise Exception('Invalid claim type')
            if scheme not in ENUM_SCHEME_TYPE:
                raise Exception('Invalid scheme type')
            if isinstance(data, str):
                data = Web3.toHex(text=data)
            if not data:
                raise Exception('Invalid data paramemter')
               
            claimType = ENUM_CLAIM_TYPE.index(claimType)
            scheme = ENUM_SCHEME_TYPE.index(scheme)
           
            # Generate signature
            msg = Web3.soliditySha3(['address', 'uint256', 'bytes'], [user, claimType, data])
            signatureData = self.__w3.eth.account.signHash(
                msg, issuerPrivateKey
            )
            signature = signatureData.signature

            # Initiate user contract
            userContract = self.__w3.eth.contract(
                address=userContractAddress, abi=userContractAbi
            )
            encodedABI = userContract.encodeABI(
                fn_name='addClaim', args=[claimType, scheme, issuer, signature, data, url])
            print(claimType, scheme, issuer, signature, data, url)

            # Validate transaction and get gas estimation
            gasEstimate = self.__w3.eth.estimateGas(
                {'from': issuer, 'to': userContractAddress, 'data': encodedABI})
            print(gasEstimate)

            signed_txn = self.__w3.eth.account.signTransaction(dict(
                nonce=self.__w3.eth.getTransactionCount(issuer),
                gasPrice=self.__w3.eth.gasPrice,
                gas=gasEstimate,
                to=userContractAddress,
                value=0,
                data=encodedABI,
                chainId=3
            ), issuerPrivateKey,)
            tx_hash = self.__w3.eth.sendRawTransaction(
                signed_txn.rawTransaction)
            tx_hash = tx_hash.hex()
            return None, tx_hash
        except Exception as e:
            return str(e), None
