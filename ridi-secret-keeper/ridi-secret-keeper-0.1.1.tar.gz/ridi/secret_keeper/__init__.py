import os

import boto3

SECRETKEEPER_AWS_ACCESS_KEY = os.environ['SECRETKEEPER_AWS_ACCESS_KEY']
SECRETKEEPER_AWS_SECRET_KEY = os.environ['SECRETKEEPER_AWS_SECRET_KEY']
SECRETKEEPER_AWS_REGION = os.environ['SECRETKEEPER_AWS_REGION']


client = boto3.client(
    'ssm',
    region_name=SECRETKEEPER_AWS_REGION,
    aws_access_key_id=SECRETKEEPER_AWS_ACCESS_KEY,
    aws_secret_access_key=SECRETKEEPER_AWS_SECRET_KEY,
)


def get(alias):
    response = client.get_parameter(
        Name=alias, WithDecryption=True,
    )
    return response['Parameter']['Value']
