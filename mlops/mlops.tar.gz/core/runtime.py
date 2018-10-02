""" Core Runtime """

import os
from google.protobuf.json_format import MessageToDict, ParseDict

from mlops.core.res_pb2 import TrainingJob
from mlops.core.util import import_module, load_yaml

API_GROUPS = ['mlops.ornew.io']

KIND_TABLE = {
  'train': 'TrainingJob',
  'training-job': 'TrainingJob',
}

DEFAULT_CONFIG = dict(
  log_verbosity                 = 'INFO',
  random_seed                   = None,
  save_summary_steps            = 1,
  save_checkpoints_steps        = None,
  save_checkpoints_secs         = None,
  keep_checkpoint_max           = 10,
  keep_checkpoint_every_n_hours = None,
  log_step_count_steps          = 100,
  train_max_steps               = None,
  eval_name                     = 'eval',
  eval_steps                    = 1,
  eval_start_delay_secs         = 120,
  eval_throttle_secs            = 600,
)

def with_default_config(user_config):
  #TODO: check deprecated item in user config
  config = {}
  config.update(DEFAULT_CONFIG)
  config.update(user_config)
  return config

class ResourcePool:
  def __init__(self):
    self._map = {}
  def lookup(self, query):
    _query = query.split('/')
    if len(_query) != 2:
      #TODO: exception invalid arg
      raise 'The resource name must be "<kind-alias>/<metadata-name>"'
    kind, name = _query
    resolved_kind = KIND_TABLE.get(kind, None)
    if resolved_kind is None:
      raise 'Unknown kind type {}'.format(kind)
    key = '{}/{}'.format(resolved_kind, name)
    #TODO: handle `KeyError`
    return self._map[key]
  def register(self, res):
    # read metadata
    #TODO: validation
    #TODO: handle `KeyError`
    name = res['metadata']['name']
    kind = res['kind']
    key = '{}/{}'.format(kind, name)
    self._map[key] = res
    print('registered: {}'.format(key))

def load_resouces(files):
  pool = ResourcePool()
  for file in files:
    resources = load_yaml(file) # load yaml
    for res in resources:
      # read api version
      ver = res['apiVersion'].split('/') #TODO: handle `KeyError`
      # k8s builtin api <ver>, or <group>/<ver>
      if len(ver) not in (1,2):
        #TODO: exception class
        raise 'Invalid apiVersion'
      # skip if unknown group resource
      if ver[0] not in API_GROUPS:
        #TODO: log verbosity
        print('skip unknown API group resource: {} (in {})'.format(ver[0], file))
        continue
      # register to pool
      pool.register(res)
  return pool

def run_training_job(res):
  #TODO: handle parse error
  res = ParseDict(res, TrainingJob())
  spec = res.spec
  # resolve driver kinds
  if res.spec.driver.WhichOneof('kind') == 'python':
    module, ver = res.spec.driver.python.path.split(':')
    driver = import_module(module)
    result = driver.run(
      version  = ver,
      metadata = res.metadata,
      params   = res.spec.params,
      config   = with_default_config(res.spec.config),
      args     = res.spec.driver.python.args)
    # process result
    return result
  else:
    raise NotImplementedError(spec.driver.kind)

_WELL_KNOWN = [
  './mlops.yaml'
]
def _check_well_known_config():
  return [
    i for i in _WELL_KNOWN
    if os.path.exists(i)
  ]

def run(name, res_files=[]):
  well_known_files = _check_well_known_config()
  pool = load_resouces(well_known_files + res_files)
  res = pool.lookup(name)
  # resolve resource type handler
  if res['kind'] == 'TrainingJob':
    return run_training_job(res)
  else:
    raise NotImplementedError(res['kind'])
