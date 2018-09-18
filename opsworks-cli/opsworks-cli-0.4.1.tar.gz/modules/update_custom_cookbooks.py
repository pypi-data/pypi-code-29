#!/usr/bin/env python
# Copyright 2018 Chathuranga Abeyrathna. All Rights Reserved.
# AWS OpsWorks deployment cli

# update custom cookbooks

import sys
import getopt
import boto3
import time
from common_functions import *


def update_custom_cookbooks():
    try:
        opts, args = getopt.getopt(sys.argv[2:], 'r:s:l:i:h', [
            'region=', 'stack=', 'layer=', 'instances=', 'help'
        ])
    except getopt.GetoptError:
        update_custom_cookbooks_usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            update_custom_cookbooks_usage()
        elif opt in ('-r', '--region'):
            region = arg
        elif opt in ('-s', '--stack'):
            stack = arg
        elif opt in ('-l', '--layer'):
            layer = arg
        elif opt in ('-i', '--instances'):
            instances = arg
        else:
            update_custom_cookbooks_usage()

    print "running update_custom_cookbooks"
    # initiate boto3 client
    client = boto3.client('opsworks', region_name=region)
    # calling deployment to specified stack layer
    run_update_custom_cookbooks = client.create_deployment(
        StackId=stack,
        LayerIds=[
            layer,
        ],
        Command={
            'Name': 'update_custom_cookbooks'
        },
        Comment='automated update_custom_cookbooks job'
    )

    deploymentId = run_update_custom_cookbooks['DeploymentId']
    # sending describe command to get status"""  """
    get_status(deploymentId, region, instances)