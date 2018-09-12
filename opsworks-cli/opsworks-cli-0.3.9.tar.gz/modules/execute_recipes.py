#!/usr/bin/env python
# Copyright 2018 Chathuranga Abeyrathna. All Rights Reserved.
# AWS OpsWorks deployment cli

# execute recipes

import sys
import getopt
import boto3
import time
from common_functions import *


def execute_recipes():
    try:
        opts, args = getopt.getopt(sys.argv[2:], 'r:s:l:i:c:j:h', [
            'region=', 'stack=', 'layer=', 'instances=', 'cookbook=', 'custom-json=', 'help'
        ])
    except getopt.GetoptError:
        execute_recipes_usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            execute_recipes_usage()
        elif opt in ('-r', '--region'):
            region = arg
        elif opt in ('-s', '--stack'):
            stack = arg
        elif opt in ('-l', '--layer'):
            layer = arg
        elif opt in ('-i', '--instances'):
            instances = arg
        elif opt in ('-c', '--cookbook'):
            cookbook = arg
        elif opt in ('-j', '--custom-json'):
            custom_json = arg
        else:
            execute_recipes_usage()
    try:
        custom_json
    except NameError:
        custom_json = str({})
    try:
        layer
    except NameError:
        layer = None
    if layer is None:
        print "running execute_recipe with " + str(cookbook) + "and Custom-Json" + str(custom_json)
        # initiate boto3 client
        client = boto3.client('opsworks', region_name=region)
        # calling deployment to specified stack layer
        run_recipes = client.create_deployment(
            StackId=stack,
            Command={
                'Name': 'execute_recipes',
                'Args': {
                    'recipes': [
                        cookbook,
                    ]
                }
            },
            Comment='automated execute_recipes job',
            CustomJson=custom_json
        )
    else:
        print "running execute_recipe with " + str(cookbook)+ "without custom json"
        # initiate boto3 client
        client = boto3.client('opsworks', region_name=region)
        # calling deployment to specified stack layer
        run_recipes = client.create_deployment(
            StackId=stack,
            LayerIds=[
                layer,
            ],
            Command={
                'Name': 'execute_recipes',
                'Args': {
                    'recipes': [
                        cookbook,
                    ]
                }
            },
            Comment='automated execute_recipes job'
        )

    deploymentId = run_recipes['DeploymentId']
    # sending describe command to get status"""  """
    get_status(deploymentId, region, instances)