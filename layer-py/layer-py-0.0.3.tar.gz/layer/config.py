DEFAULT_WEB3_PROVIDER = "http://34.233.128.254:8555"

LAYER_CONTRACT_ADDRESS = "0x1eec085e9c39eeccb3277d1104599ac18ab8fe27"
LAYER_CONTRACT_ABI = """[
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"name": "previousOwner",
				"type": "address"
			},
			{
				"indexed": true,
				"name": "newOwner",
				"type": "address"
			}
		],
		"name": "OwnershipTransferred",
		"type": "event"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_addr",
				"type": "address"
			},
			{
				"name": "_url",
				"type": "string"
			}
		],
		"name": "addLayerNode",
		"outputs": [
			{
				"name": "",
				"type": "address"
			},
			{
				"name": "",
				"type": "string"
			},
			{
				"name": "",
				"type": "address[]"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_addr",
				"type": "address"
			},
			{
				"name": "_name",
				"type": "string"
			},
			{
				"name": "_approved",
				"type": "bool"
			},
			{
				"name": "_category",
				"type": "uint256"
			}
		],
		"name": "addProvider",
		"outputs": [
			{
				"name": "",
				"type": "address"
			},
			{
				"name": "",
				"type": "string"
			},
			{
				"name": "",
				"type": "bool"
			},
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_addr",
				"type": "address"
			}
		],
		"name": "deleteLayerNodeByAddress",
		"outputs": [
			{
				"name": "",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_addr",
				"type": "address"
			}
		],
		"name": "deleteProviderByAddress",
		"outputs": [
			{
				"name": "",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_addr",
				"type": "address"
			},
			{
				"name": "_approve",
				"type": "bool"
			}
		],
		"name": "setApproveLayerNode",
		"outputs": [
			{
				"name": "",
				"type": "address"
			},
			{
				"name": "",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_addr",
				"type": "address"
			},
			{
				"name": "_approve",
				"type": "bool"
			}
		],
		"name": "setApproveProvider",
		"outputs": [
			{
				"name": "",
				"type": "address"
			},
			{
				"name": "",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "newOwner",
				"type": "address"
			}
		],
		"name": "transferOwnership",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_addr",
				"type": "address"
			},
			{
				"name": "_url",
				"type": "string"
			}
		],
		"name": "updateLayerNodeUrl",
		"outputs": [
			{
				"name": "",
				"type": "address"
			},
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "_addr",
				"type": "address"
			}
		],
		"name": "getLayerNodeByAddress",
		"outputs": [
			{
				"name": "",
				"type": "address"
			},
			{
				"name": "",
				"type": "string"
			},
			{
				"name": "",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "getLayerNodes",
		"outputs": [
			{
				"name": "",
				"type": "address[]"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "_addr",
				"type": "address"
			}
		],
		"name": "getProviderByAddress",
		"outputs": [
			{
				"name": "",
				"type": "address"
			},
			{
				"name": "",
				"type": "string"
			},
			{
				"name": "",
				"type": "bool"
			},
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "getProviders",
		"outputs": [
			{
				"name": "",
				"type": "address[]"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "owner",
		"outputs": [
			{
				"name": "",
				"type": "address"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	}
]"""

CLAIM_CONTRACT_ADDRESS = "0x6d824b8755b8c865c9f176a844771c62e28b85c5"
CLAIM_CONTRACT_ABI = """[
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"name": "executionId",
				"type": "uint256"
			},
			{
				"indexed": false,
				"name": "approved",
				"type": "bool"
			}
		],
		"name": "Approved",
		"type": "event"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_user",
				"type": "address"
			},
			{
				"name": "_scheme",
				"type": "uint256"
			},
			{
				"name": "_issuer",
				"type": "address"
			},
			{
				"name": "_claimType",
				"type": "uint256"
			},
			{
				"name": "_signature",
				"type": "bytes"
			},
			{
				"name": "_data",
				"type": "bytes"
			},
			{
				"name": "_uri",
				"type": "string"
			}
		],
		"name": "addClaim",
		"outputs": [
			{
				"name": "claimRequestId",
				"type": "bytes32"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"name": "executionId",
				"type": "uint256"
			},
			{
				"indexed": true,
				"name": "to",
				"type": "address"
			},
			{
				"indexed": true,
				"name": "value",
				"type": "uint256"
			},
			{
				"indexed": false,
				"name": "data",
				"type": "bytes"
			}
		],
		"name": "Executed",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"name": "executionId",
				"type": "uint256"
			},
			{
				"indexed": true,
				"name": "to",
				"type": "address"
			},
			{
				"indexed": true,
				"name": "value",
				"type": "uint256"
			},
			{
				"indexed": false,
				"name": "data",
				"type": "bytes"
			}
		],
		"name": "ExecutionRequested",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"name": "key",
				"type": "bytes32"
			},
			{
				"indexed": true,
				"name": "purpose",
				"type": "uint256"
			},
			{
				"indexed": true,
				"name": "keyType",
				"type": "uint256"
			}
		],
		"name": "KeyRemoved",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"name": "key",
				"type": "bytes32"
			},
			{
				"indexed": true,
				"name": "purpose",
				"type": "uint256"
			},
			{
				"indexed": true,
				"name": "keyType",
				"type": "uint256"
			}
		],
		"name": "KeyAdded",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"name": "executionId",
				"type": "uint256"
			},
			{
				"indexed": true,
				"name": "to",
				"type": "address"
			},
			{
				"indexed": true,
				"name": "value",
				"type": "uint256"
			},
			{
				"indexed": false,
				"name": "data",
				"type": "bytes"
			}
		],
		"name": "ExecutionFailed",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"name": "claimId",
				"type": "bytes32"
			},
			{
				"indexed": true,
				"name": "claimType",
				"type": "uint256"
			},
			{
				"indexed": false,
				"name": "scheme",
				"type": "uint256"
			},
			{
				"indexed": true,
				"name": "issuer",
				"type": "address"
			},
			{
				"indexed": false,
				"name": "signature",
				"type": "bytes"
			},
			{
				"indexed": false,
				"name": "data",
				"type": "bytes"
			},
			{
				"indexed": false,
				"name": "uri",
				"type": "string"
			}
		],
		"name": "ClaimChanged",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"name": "claimId",
				"type": "bytes32"
			},
			{
				"indexed": true,
				"name": "claimType",
				"type": "uint256"
			},
			{
				"indexed": false,
				"name": "scheme",
				"type": "uint256"
			},
			{
				"indexed": true,
				"name": "issuer",
				"type": "address"
			},
			{
				"indexed": false,
				"name": "signature",
				"type": "bytes"
			},
			{
				"indexed": false,
				"name": "data",
				"type": "bytes"
			},
			{
				"indexed": false,
				"name": "uri",
				"type": "string"
			}
		],
		"name": "ClaimRemoved",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"name": "claimId",
				"type": "bytes32"
			},
			{
				"indexed": true,
				"name": "claimType",
				"type": "uint256"
			},
			{
				"indexed": false,
				"name": "scheme",
				"type": "uint256"
			},
			{
				"indexed": true,
				"name": "issuer",
				"type": "address"
			},
			{
				"indexed": false,
				"name": "signature",
				"type": "bytes"
			},
			{
				"indexed": false,
				"name": "data",
				"type": "bytes"
			},
			{
				"indexed": false,
				"name": "uri",
				"type": "string"
			}
		],
		"name": "ClaimAdded",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"name": "claimId",
				"type": "bytes32"
			},
			{
				"indexed": true,
				"name": "claimType",
				"type": "uint256"
			},
			{
				"indexed": true,
				"name": "issuer",
				"type": "address"
			},
			{
				"indexed": false,
				"name": "signatureType",
				"type": "uint256"
			},
			{
				"indexed": false,
				"name": "signature",
				"type": "bytes32"
			},
			{
				"indexed": false,
				"name": "claim",
				"type": "bytes"
			},
			{
				"indexed": false,
				"name": "uri",
				"type": "string"
			}
		],
		"name": "ClaimAdded",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"name": "claimRequestId",
				"type": "uint256"
			},
			{
				"indexed": true,
				"name": "claimType",
				"type": "uint256"
			},
			{
				"indexed": false,
				"name": "scheme",
				"type": "uint256"
			},
			{
				"indexed": true,
				"name": "issuer",
				"type": "address"
			},
			{
				"indexed": false,
				"name": "signature",
				"type": "bytes"
			},
			{
				"indexed": false,
				"name": "data",
				"type": "bytes"
			},
			{
				"indexed": false,
				"name": "uri",
				"type": "string"
			}
		],
		"name": "ClaimRequested",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"name": "previousOwner",
				"type": "address"
			},
			{
				"indexed": true,
				"name": "newOwner",
				"type": "address"
			}
		],
		"name": "OwnershipTransferred",
		"type": "event"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_claimType",
				"type": "uint256"
			},
			{
				"name": "_scheme",
				"type": "uint256"
			},
			{
				"name": "_issuer",
				"type": "address"
			},
			{
				"name": "_signature",
				"type": "bytes"
			},
			{
				"name": "_data",
				"type": "bytes"
			},
			{
				"name": "_uri",
				"type": "string"
			}
		],
		"name": "addClaim",
		"outputs": [
			{
				"name": "claimRequestId",
				"type": "bytes32"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"name": "_identity",
				"type": "address"
			},
			{
				"indexed": false,
				"name": "claimType",
				"type": "uint256"
			}
		],
		"name": "ClaimInvalid",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"name": "_identity",
				"type": "address"
			},
			{
				"indexed": false,
				"name": "claimType",
				"type": "uint256"
			}
		],
		"name": "ClaimValid",
		"type": "event"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_user",
				"type": "address"
			},
			{
				"name": "_signer",
				"type": "address"
			},
			{
				"name": "_identityHash",
				"type": "string"
			},
			{
				"name": "_keyHash",
				"type": "string"
			}
		],
		"name": "addIdentity",
		"outputs": [
			{
				"name": "result",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_key",
				"type": "bytes32"
			},
			{
				"name": "_purpose",
				"type": "uint256"
			},
			{
				"name": "_type",
				"type": "uint256"
			}
		],
		"name": "addKey",
		"outputs": [
			{
				"name": "success",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_id",
				"type": "uint256"
			},
			{
				"name": "_approve",
				"type": "bool"
			}
		],
		"name": "approve",
		"outputs": [
			{
				"name": "success",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_identity",
				"type": "address"
			},
			{
				"name": "claimType",
				"type": "uint256"
			}
		],
		"name": "checkClaim",
		"outputs": [
			{
				"name": "claimValid",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_to",
				"type": "address"
			},
			{
				"name": "_value",
				"type": "uint256"
			},
			{
				"name": "_data",
				"type": "bytes"
			}
		],
		"name": "execute",
		"outputs": [
			{
				"name": "executionId",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_user",
				"type": "address"
			},
			{
				"name": "_claimId",
				"type": "bytes32"
			}
		],
		"name": "removeClaim",
		"outputs": [
			{
				"name": "success",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_claimId",
				"type": "bytes32"
			}
		],
		"name": "removeClaim",
		"outputs": [
			{
				"name": "success",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_key",
				"type": "bytes32"
			}
		],
		"name": "removeKey",
		"outputs": [
			{
				"name": "success",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "newOwner",
				"type": "address"
			}
		],
		"name": "transferOwnership",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "_identity",
				"type": "address"
			},
			{
				"name": "claimType",
				"type": "uint256"
			}
		],
		"name": "claimIsValid",
		"outputs": [
			{
				"name": "claimValid",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "_claimId",
				"type": "bytes32"
			}
		],
		"name": "getClaim",
		"outputs": [
			{
				"name": "claimType",
				"type": "uint256"
			},
			{
				"name": "scheme",
				"type": "uint256"
			},
			{
				"name": "issuer",
				"type": "address"
			},
			{
				"name": "signature",
				"type": "bytes"
			},
			{
				"name": "data",
				"type": "bytes"
			},
			{
				"name": "uri",
				"type": "string"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "_claimType",
				"type": "uint256"
			}
		],
		"name": "getClaimIdsByType",
		"outputs": [
			{
				"name": "claimIds",
				"type": "bytes32[]"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "_key",
				"type": "bytes32"
			}
		],
		"name": "getKey",
		"outputs": [
			{
				"name": "purpose",
				"type": "uint256"
			},
			{
				"name": "keyType",
				"type": "uint256"
			},
			{
				"name": "key",
				"type": "bytes32"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "_key",
				"type": "bytes32"
			}
		],
		"name": "getKeyPurpose",
		"outputs": [
			{
				"name": "purpose",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "_purpose",
				"type": "uint256"
			}
		],
		"name": "getKeysByPurpose",
		"outputs": [
			{
				"name": "_keys",
				"type": "bytes32[]"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "sig",
				"type": "bytes"
			},
			{
				"name": "dataHash",
				"type": "bytes32"
			}
		],
		"name": "getRecoveredAddress",
		"outputs": [
			{
				"name": "addr",
				"type": "address"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "_key",
				"type": "bytes32"
			},
			{
				"name": "_purpose",
				"type": "uint256"
			}
		],
		"name": "keyHasPurpose",
		"outputs": [
			{
				"name": "result",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "owner",
		"outputs": [
			{
				"name": "",
				"type": "address"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	}
]"""

USER_CONTRACT_ABI = """[
	{
		"constant": true,
		"inputs": [
			{
				"name": "_key",
				"type": "bytes32"
			}
		],
		"name": "getKeyPurpose",
		"outputs": [
			{
				"name": "purpose",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "_key",
				"type": "bytes32"
			}
		],
		"name": "getKey",
		"outputs": [
			{
				"name": "purpose",
				"type": "uint256"
			},
			{
				"name": "keyType",
				"type": "uint256"
			},
			{
				"name": "key",
				"type": "bytes32"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_key",
				"type": "bytes32"
			},
			{
				"name": "_purpose",
				"type": "uint256"
			},
			{
				"name": "_type",
				"type": "uint256"
			}
		],
		"name": "addKey",
		"outputs": [
			{
				"name": "success",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "_claimType",
				"type": "uint256"
			}
		],
		"name": "getClaimIdsByType",
		"outputs": [
			{
				"name": "claimIds",
				"type": "bytes32[]"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_claimId",
				"type": "bytes32"
			}
		],
		"name": "removeClaim",
		"outputs": [
			{
				"name": "success",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_id",
				"type": "uint256"
			},
			{
				"name": "_approve",
				"type": "bool"
			}
		],
		"name": "approve",
		"outputs": [
			{
				"name": "success",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_key",
				"type": "bytes32"
			}
		],
		"name": "removeKey",
		"outputs": [
			{
				"name": "success",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "_purpose",
				"type": "uint256"
			}
		],
		"name": "getKeysByPurpose",
		"outputs": [
			{
				"name": "_keys",
				"type": "bytes32[]"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_claimType",
				"type": "uint256"
			},
			{
				"name": "_scheme",
				"type": "uint256"
			},
			{
				"name": "_issuer",
				"type": "address"
			},
			{
				"name": "_signature",
				"type": "bytes"
			},
			{
				"name": "_data",
				"type": "bytes"
			},
			{
				"name": "_uri",
				"type": "string"
			}
		],
		"name": "addClaim",
		"outputs": [
			{
				"name": "claimRequestId",
				"type": "bytes32"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_to",
				"type": "address"
			},
			{
				"name": "_value",
				"type": "uint256"
			},
			{
				"name": "_data",
				"type": "bytes"
			}
		],
		"name": "execute",
		"outputs": [
			{
				"name": "executionId",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "_claimId",
				"type": "bytes32"
			}
		],
		"name": "getClaim",
		"outputs": [
			{
				"name": "claimType",
				"type": "uint256"
			},
			{
				"name": "scheme",
				"type": "uint256"
			},
			{
				"name": "issuer",
				"type": "address"
			},
			{
				"name": "signature",
				"type": "bytes"
			},
			{
				"name": "data",
				"type": "bytes"
			},
			{
				"name": "uri",
				"type": "string"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "_key",
				"type": "bytes32"
			},
			{
				"name": "_purpose",
				"type": "uint256"
			}
		],
		"name": "keyHasPurpose",
		"outputs": [
			{
				"name": "result",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"name": "claimRequestId",
				"type": "uint256"
			},
			{
				"indexed": true,
				"name": "claimType",
				"type": "uint256"
			},
			{
				"indexed": false,
				"name": "scheme",
				"type": "uint256"
			},
			{
				"indexed": true,
				"name": "issuer",
				"type": "address"
			},
			{
				"indexed": false,
				"name": "signature",
				"type": "bytes"
			},
			{
				"indexed": false,
				"name": "data",
				"type": "bytes"
			},
			{
				"indexed": false,
				"name": "uri",
				"type": "string"
			}
		],
		"name": "ClaimRequested",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"name": "claimId",
				"type": "bytes32"
			},
			{
				"indexed": true,
				"name": "claimType",
				"type": "uint256"
			},
			{
				"indexed": true,
				"name": "issuer",
				"type": "address"
			},
			{
				"indexed": false,
				"name": "signatureType",
				"type": "uint256"
			},
			{
				"indexed": false,
				"name": "signature",
				"type": "bytes32"
			},
			{
				"indexed": false,
				"name": "claim",
				"type": "bytes"
			},
			{
				"indexed": false,
				"name": "uri",
				"type": "string"
			}
		],
		"name": "ClaimAdded",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"name": "claimId",
				"type": "bytes32"
			},
			{
				"indexed": true,
				"name": "claimType",
				"type": "uint256"
			},
			{
				"indexed": false,
				"name": "scheme",
				"type": "uint256"
			},
			{
				"indexed": true,
				"name": "issuer",
				"type": "address"
			},
			{
				"indexed": false,
				"name": "signature",
				"type": "bytes"
			},
			{
				"indexed": false,
				"name": "data",
				"type": "bytes"
			},
			{
				"indexed": false,
				"name": "uri",
				"type": "string"
			}
		],
		"name": "ClaimAdded",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"name": "claimId",
				"type": "bytes32"
			},
			{
				"indexed": true,
				"name": "claimType",
				"type": "uint256"
			},
			{
				"indexed": false,
				"name": "scheme",
				"type": "uint256"
			},
			{
				"indexed": true,
				"name": "issuer",
				"type": "address"
			},
			{
				"indexed": false,
				"name": "signature",
				"type": "bytes"
			},
			{
				"indexed": false,
				"name": "data",
				"type": "bytes"
			},
			{
				"indexed": false,
				"name": "uri",
				"type": "string"
			}
		],
		"name": "ClaimRemoved",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"name": "claimId",
				"type": "bytes32"
			},
			{
				"indexed": true,
				"name": "claimType",
				"type": "uint256"
			},
			{
				"indexed": false,
				"name": "scheme",
				"type": "uint256"
			},
			{
				"indexed": true,
				"name": "issuer",
				"type": "address"
			},
			{
				"indexed": false,
				"name": "signature",
				"type": "bytes"
			},
			{
				"indexed": false,
				"name": "data",
				"type": "bytes"
			},
			{
				"indexed": false,
				"name": "uri",
				"type": "string"
			}
		],
		"name": "ClaimChanged",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"name": "executionId",
				"type": "uint256"
			},
			{
				"indexed": true,
				"name": "to",
				"type": "address"
			},
			{
				"indexed": true,
				"name": "value",
				"type": "uint256"
			},
			{
				"indexed": false,
				"name": "data",
				"type": "bytes"
			}
		],
		"name": "ExecutionFailed",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"name": "key",
				"type": "bytes32"
			},
			{
				"indexed": true,
				"name": "purpose",
				"type": "uint256"
			},
			{
				"indexed": true,
				"name": "keyType",
				"type": "uint256"
			}
		],
		"name": "KeyAdded",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"name": "key",
				"type": "bytes32"
			},
			{
				"indexed": true,
				"name": "purpose",
				"type": "uint256"
			},
			{
				"indexed": true,
				"name": "keyType",
				"type": "uint256"
			}
		],
		"name": "KeyRemoved",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"name": "executionId",
				"type": "uint256"
			},
			{
				"indexed": true,
				"name": "to",
				"type": "address"
			},
			{
				"indexed": true,
				"name": "value",
				"type": "uint256"
			},
			{
				"indexed": false,
				"name": "data",
				"type": "bytes"
			}
		],
		"name": "ExecutionRequested",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"name": "executionId",
				"type": "uint256"
			},
			{
				"indexed": true,
				"name": "to",
				"type": "address"
			},
			{
				"indexed": true,
				"name": "value",
				"type": "uint256"
			},
			{
				"indexed": false,
				"name": "data",
				"type": "bytes"
			}
		],
		"name": "Executed",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"name": "executionId",
				"type": "uint256"
			},
			{
				"indexed": false,
				"name": "approved",
				"type": "bool"
			}
		],
		"name": "Approved",
		"type": "event"
	}
]"""
