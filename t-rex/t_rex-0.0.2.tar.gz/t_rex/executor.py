from redis import Redis
from enum import Enum


r = Redis()

type2command = {
        'hash': 'hkeys ',
        'string': 'get ',
        }

class ResultType(Enum):
    PATTERN = 0
    DETAIL = 1
    ERROR = 2

def _process_KEYS(keys):
    results = map(lambda x: x.decode('utf-8'), keys)
    output = '\n'.join(results)
    return output

def _process_GET(byte_s):
    output = byte_s.decode('utf-8')
    return output


_process_TYPE = _process_GET

result_processors = {
        'keys': (ResultType.PATTERN, _process_KEYS),
        'hkeys': (ResultType.PATTERN, _process_KEYS),
        'get': (ResultType.DETAIL, _process_GET),
        'type': (ResultType.DETAIL, _process_GET),
        }

def execute(cmd):
    try:
        results = r.execute_command(cmd)
    except Exception as e:
        return (ResultType.ERROR, '\n\n{}'.format(e))
    return postprocess(cmd, results)

def execute_subcommand(line):
    redis_type = _process_TYPE(r.execute_command('type {}'.format(line)))
    cmd = type2command[redis_type]
    try:
        results = r.execute_command(cmd + line)
    except Exception as e:
        return (ResultType.ERROR, '\n\n{}'.format(e))
    return postprocess(cmd, results)



def postprocess(cmd, output):
    cmd_class = cmd.split()[0]
    category, processor = result_processors.get(cmd_class.lower())
    return category, processor(output)
