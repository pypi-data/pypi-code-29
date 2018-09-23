import json
from os import path
from os import makedirs
from time import sleep
from inspect import signature
from collections import deque
from datapackage import Package
from dataflows import PackageWrapper, dump_to_path, load, Flow
from dataflows_serverless.constants import *
from functools import partial


# secondary processing of the serverless steps, all other steps are ignored
def get_secondary_chain(source_chain, secondary, num_secondaries, workdir):
    for step_idx, step in enumerate(source_chain):
        serverless_step_config = getattr(step, '__serverless_step', None)
        if serverless_step_config:
            wait_primary_step_complete(secondary, num_secondaries, step_idx, workdir)
            notify_complete = partial(notify_secondary_step_complete, step_idx, secondary, num_secondaries,
                                      workdir, serverless_step_config)
            print('secondary {}/{}: running step {} flow'.format(secondary, num_secondaries, step_idx))
            try:
                Flow(load(PRIMARY_INPUT_DATAPACKAGE_FILE_TEMPLATE.format(workdir=workdir, step_idx=step_idx)),
                     get_secondary_step(step, serverless_step_config, secondary, num_secondaries, step_idx, workdir),
                     dump_to_path(SECONDARY_OUTPUT_DATAPACKAGE_PATH_TEMPLATE.format(workdir=workdir, secondary=secondary,
                                                                                    step_idx=step_idx))).process()
            except Exception as e:
                notify_complete(str(e))
                raise
            notify_complete(None)
    return [[]]


def wait_primary_step_complete(secondary, num_secondaries, step_idx, workdir):
    print('secondary {}/{}: waiting for primary step idx {} to complete'.format(secondary, num_secondaries, step_idx))
    complete_file = PRIMARY_STEP_COMPLETE_FILE_TEMPLATE.format(workdir=workdir, step_idx=step_idx)
    while True:
        sleep(WAIT_FOR_PRIMARY_STEP_COMPLETE_DELAY_SECONDS)
        if not path.exists(complete_file):
            continue
        with open(complete_file) as f:
            complete_step_idx = json.load(f)['step_idx']
            if complete_step_idx != step_idx:
                continue
        break
    print('secondary {}/{}: primary step idx {} complete'.format(secondary, num_secondaries, step_idx))


# process the rows assigned to this secondary
def get_secondary_step(step, serverless_step_config, secondary, num_secondaries, step_idx, workdir):
    def _step(package: PackageWrapper):
        [package.pkg.remove_resource(r) for r in package.pkg.resource_names
         if r != serverless_step_config['resource_name']]
        yield package.pkg
        last_resource_names = deque(maxlen=10)
        found_resource = False
        for resource in package:
            last_resource_names.append(resource.res.name)
            if resource.res.name == serverless_step_config['resource_name']:
                found_resource = True
                yield process_secondary_rows(resource, secondary, num_secondaries, step, step_idx, workdir, True)
            else:
                deque(process_secondary_rows(resource, secondary, num_secondaries, step, step_idx, workdir, False), 0)
        assert found_resource, 'Failed to found serverless step resource name {}, ' \
                               'available resource names: {}'.format(serverless_step_config['resource_name'],
                                                                     list(last_resource_names))
    return _step


def get_secondary_input_rows(rows, secondary, num_secondaries, primary_rows_count):
    rows_per_secondary = int(primary_rows_count / num_secondaries)
    cur_secondary = 0
    cur_rows_count = 0
    for row in rows:
        if cur_secondary == secondary:
            yield row
        if cur_rows_count == rows_per_secondary:
            cur_secondary += 1
            cur_rows_count = 0
        else:
            cur_rows_count += 1


# do the processing on the relevant subset of rows for this secondary
def process_secondary_rows(rows, secondary, num_secondaries, step, step_idx, workdir, is_serverless_resource):
    if is_serverless_resource:
        print('secondary {}/{}: processing step {} serverless resource'.format(secondary, num_secondaries, step_idx))
        complete_file = PRIMARY_STEP_COMPLETE_FILE_TEMPLATE.format(workdir=workdir, step_idx=step_idx)
        with open(path.join(path.dirname(complete_file), 'rows_count')) as f:
            primary_rows_count = int(f.read())
        rows = get_secondary_input_rows(rows, secondary, num_secondaries, primary_rows_count)
    sig = signature(step)
    params = list(sig.parameters)
    assert len(params) == 1
    if params[0] == 'row':
        for row in rows:
            new_row = step(row)
            yield new_row if new_row else row
    else:
        assert params[0] == 'rows'
        for row in step(rows):
            yield row
    if is_serverless_resource:
        print('secondary {}/{}: finished procesing step {}'.format(secondary, num_secondaries, step_idx))


def notify_secondary_step_complete(step_idx, secondary, num_secondaries, workdir, serverless_step_config, error=None):
    stats = {'success': error is None,
             'step_idx': step_idx,
             'error': error}
    stats_file = SECONDARY_STATS_FILE_TEMPLATE.format(workdir=workdir, secondary=secondary,
                                                      step_idx=step_idx)
    makedirs(path.dirname(stats_file), exist_ok=True)
    with open(stats_file, 'w') as f:
        json.dump(stats, f)
    print('secondary {}/{}: complete: {}'.format(secondary, num_secondaries, stats))
