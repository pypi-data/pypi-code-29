#!/usr/bin/env python
# Copyright 2018 Chathuranga Abeyrathna. All Rights Reserved.
# AWS OpsWorks deployment cli

# execute setup

import sys
import getopt
import boto3
import time
from common_functions import *


def setup():
    try:
        opts, args = getopt.getopt(sys.argv[2:], 'r:s:l:i:h', [
            'region=', 'stack=', 'layer=', 'instances=', 'help'
        ])
    except getopt.GetoptError:
        setup_usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            setup_usage()
        elif opt in ('-r', '--region'):
            region = arg
        elif opt in ('-s', '--stack'):
            stack = arg
        elif opt in ('-l', '--layer'):
            layer = arg
        elif opt in ('-i', '--instances'):
            instances = arg
        else:
            setup_usage()

    print "running setup..."
    # initiate boto3 client
    client = boto3.client('opsworks', region_name=region)
    # calling deployment to specified stack layer
    run_setup = client.create_deployment(
        StackId=stack,
        LayerIds=[
            layer,
        ],
        Command={
            'Name': 'setup'
        },
        Comment='automated setup job'
    )

    deploymentId = run_setup['DeploymentId']
    # sending describe command to get status"""  """
    get_status(deploymentId, region, instances)
