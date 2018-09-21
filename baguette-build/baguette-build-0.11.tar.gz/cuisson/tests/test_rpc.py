#-*- coding:utf-8 -*-
"""
Test the deployment process using RPC.
"""
#pylint:disable=wildcard-import,unused-wildcard-import,redefined-outer-name
from .fixtures import *


def test_rpc_post_receive(rpc_server_factory, docker_registry_build, docker_registry_push, docker_registry_cleanup):
    """
    Test the full workflow when cuisson is called by RPC:
    will failed 'cause the dummy rpc server doesn't have git.
    """
    server = rpc_server_factory('post_receive')
    owner, repo, branch = gen_str(), gen_str(), gen_str()
    with pytest.raises(farine.exceptions.RPCError):
        for _ in  farine.rpc.Client('cuisson').post_receive(owner, repo, branch, __stream__=True):
            pass
