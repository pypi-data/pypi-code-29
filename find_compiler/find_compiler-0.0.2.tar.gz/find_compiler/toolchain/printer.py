import yaml
import json

_print_format='{:25}{:15}{:10}'
_allowed_keys = ['path', 'tool', 'version', 'options']

def _fiter_out_meta(meta):
  result = []
  for m in meta:
    result.append({k:v for k,v in m.iteritems() if k in _allowed_keys})
  return result

def _output_plain(meta):
  print(_print_format.format('PATH', 'TOOLCHAIN', 'VERSION'))
  for m in meta:
    print(_print_format.format(m['path'], m['tool'], m['version']))

def _output_yaml(meta):
  print yaml.dump(meta, default_flow_style=False)

def _output_json(meta):
   print json.dumps(meta, sort_keys=True, indent=2, separators=(',', ': '))

def print_toolchains(meta, output):
  meta = _fiter_out_meta(meta)
  if output == "yaml":
    _output_yaml(meta)
  elif output == "json":
    _output_json(meta)
  else:
    _output_plain(meta)
