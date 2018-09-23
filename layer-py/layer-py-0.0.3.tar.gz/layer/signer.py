import requests
import base64
import json

DEFAULT_SIGNER_ENDPOINT = 'http://34.201.171.237:5000'

class Signer:
    """
    Signer class
    """

    # Layer Signer api endpoint url
    api_endpoint = None

    def __init__(self, api_endpoint=None):
        """
        Signer constructor
        """
        if not api_endpoint:
            api_endpoint = DEFAULT_SIGNER_ENDPOINT

        self.api_endpoint = api_endpoint

    def get_key_hashes(self):
        """Get key hashes array from signer server
        Returns:
            array: Array of key hashes.
        """
        try:
            res = requests.get(self.api_endpoint + '/keys')
            res = res.json()
            if (res['status'] == 200):
                return res['data']
        except Exception:
            pass
        return None

    def get_key_by_type(self, type):
        """Get key hash from signer server
        type: {'rsa', 'dsa', 'ecdsa'}
        Returns: key_hash
        """
        try:
            res = requests.get(self.api_endpoint + '/key/type/' + type)
            res = res.json()

            if (res['status'] == 200):
                return res['data']
        except Exception:
            pass
        return None

    def get_key_detail(self, key_hash):
        """Get key details from a key hash
        Args:
            key_hash (str): A hash of a key to get detail
        Returns:
            map: A map object which contains public key, algorithm ...
        """
        try:
            res = requests.get(self.api_endpoint + '/key/details/' + key_hash)
            res = res.json()
            # print(self.api_endpoint, 'key_hash', key_hash, 'res', res)

            if (res['status'] == 200):
                return {
                    'hash': res['data']['hash'],
                    'algorithm': res['data']['algorithm'],
                    'public_key': base64.b64decode(res['data']['publicKey']),
                    'created_at': res['data']['createdAt'],
                }
        except Exception:
            pass
        return None

    def get_signature(self, raw_data, key_hash: str) -> map:
        """Get signer signature of raw data with a key hash
        For consistancy, it only use ECDSA algorithm
        Args:
            raw_data (str): Raw data to get hash (i.e JSON dumped string)
            key_hash (str): A hash of a key to use for sign
        Returns:
            map: A map object which is response from signer, containing signature
        """
        try:
            if isinstance(raw_data, dict):
                raw_data = json.dumps(raw_data, sort_keys=True)

            encoded_data = base64.b64encode(raw_data.encode()).decode('utf-8')
            res = requests.post(
                self.api_endpoint + '/signature/ecdsa',
                data=json.dumps(
                    {'data': encoded_data, 'hash': key_hash}, sort_keys=True),
                headers={'content-type': 'application/json'}
            )
            json_res = res.json()

            if json_res['status'] == 200:
                res_data = json_res['data']
                rawData = res_data['rawData']
                signature = res_data['signature']
                return signature
        except Exception as e:
            pass
        return None
