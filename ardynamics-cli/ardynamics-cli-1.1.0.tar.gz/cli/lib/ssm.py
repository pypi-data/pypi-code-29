import boto3, sys


class Ssm:
    _ssm = None

    def __init__(self):
        session = boto3.Session(region_name='eu-central-1')
        self._ssm = session.client('ssm')

    def get_parameter(self, parameter_name, decrypt=False):
        try:
            return self._ssm.get_parameter(
                Name='/ardynamics/hosting/' + parameter_name,
                WithDecryption=decrypt
            )['Parameter']['Value']
        except:
            print('Unable to get parameter ' + parameter_name + ':', sys.exc_info()[0])
            raise
