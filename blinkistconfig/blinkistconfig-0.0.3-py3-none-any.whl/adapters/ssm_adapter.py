import boto3

import os

DEFAULT_CLIENT = boto3.client('ssm')

class SSMAdapter():
    def get(self, key, scope=None, app_name=None, client=DEFAULT_CLIENT):
        prefix = "/application"
        key_scope = scope if scope else app_name
        print(f"Attempting to read key {prefix}/{key_scope}/{key}")
        try:
            response = client.get_parameter(Name=f"{prefix}/{key_scope}/{key}", WithDecryption=True)
            return response['Value']
        except client.exceptions.ParameterNotFound:
            return None
