#!/usr/bin/env python

# ########################################################################
# Copyright (C) Rigetti & Co. Inc. - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
# July, 2018
# ########################################################################

from setuptools import setup
try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements

with open("VERSION.txt", "r") as f:
    VERSION = f.read().strip()

setup(
    # Application name:
    name="rpcq",

    # Version number (initial):
    version=VERSION,

    # Application author details:
    author="Rigetti Computing",
    author_email="info@rigetti.com",

    # Packages
    packages=[
        "rpcq.base",
        "rpcq.core_messages",
        "rpcq.json_rpc",
        "rpcq.json_rpc.test",
        "rpcq.test",
    ],

    description="""Rigetti QCS Message protocols and ZMQ JSON-RPC client-server infrastructure.""",

    # Dependent packages (distributions)
    install_requires=[
        str(req.req) for req in parse_requirements('requirements.txt', session='hack')
    ],
)
