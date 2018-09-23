from dataflows import Flow
import sys
from inspect import signature
from dataflows_serverless.constants import *
from dataflows_serverless.primary_chain import get_primary_chain
from dataflows_serverless.secondary_chain import get_secondary_chain
from dataflows_serverless.serverless_chain import get_serverless_chain


# mark a step for serverless processing
def serverless_step(step, serverless_resource_name='res_1'):
    sig = signature(step)
    params = list(sig.parameters)
    assert len(params) == 1
    if params[0] == 'row':
        _serverless_step = lambda row: step(row)
    else:
        assert params[0] == 'rows'
        _serverless_step = lambda rows: step(rows)
    _serverless_step.__serverless_step = {'resource_name': serverless_resource_name}
    return _serverless_step


class ServerlessFlow(Flow):

    def _parse_args(self):
        serverless, secondaries, primary, secondary, output_datadir = None, None, None, None, None
        workdir = DEFAULT_SERVERLESS_WORKDIR
        nfs_uuid = None
        image = None
        input_datadirs = []
        no_cleanup = None
        config = {}
        for a in sys.argv:
            if a == '--serverless':
                serverless = True
            elif a.startswith('--secondaries='):
                secondaries = int(a.replace('--secondaries=', ''))
            elif a == '--primary':
                primary = True
            elif a.startswith('--secondary='):
                secondary = int(a.replace('--secondary=', ''))
            elif a.startswith('--workdir='):
                workdir = a.replace('--workdir=', '')
            elif a.startswith('--output-datadir='):
                output_datadir = a.replace('--output-datadir=', '')
            elif a.startswith('--input-datadir='):
                input_datadirs.append(a.replace('--input-datadir=', ''))
            elif a.startswith('--nfs-uuid='):
                nfs_uuid = a.replace('--nfs-uuid=', '')
            elif a.startswith('--image='):
                image = a.replace('--image=', '')
            elif a == '--no-cleanup':
                no_cleanup = True
            elif a.startswith('--data-init-image='):
                config['data_init_image'] = a.replace('--data-init-image=', '')
            elif a.startswith('--data-init-secret='):
                config['data_init_secret'] = a.replace('--data-init-secret=', '')
            elif a == '--debug':
                config['debug'] = True
        return serverless, secondaries, primary, secondary, workdir, output_datadir, input_datadirs, nfs_uuid, image, no_cleanup, config


    # initialize serverless or normal flow based on command line arguments
    def serverless(self):
        serverless, secondaries, primary, secondary, workdir, output_datadir, input_datadirs, nfs_uuid, image, no_cleanup, config = self._parse_args()
        if serverless:
            assert secondaries > 0
            if primary:
                self.chain = get_primary_chain(self.chain, secondaries, workdir)
            elif secondary is not None:
                self.chain = get_secondary_chain(self.chain, secondary, secondaries, workdir)
            else:
                self.chain = get_serverless_chain(self.chain, secondaries, output_datadir, input_datadirs, nfs_uuid, image, no_cleanup, config)
        return self
