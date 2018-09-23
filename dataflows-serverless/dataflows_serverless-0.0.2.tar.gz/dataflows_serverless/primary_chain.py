import json
from time import sleep
from collections import deque
from os import makedirs
from os import path
from dataflows import PackageWrapper, load, dump_to_path, Flow
from kvfile import KVFile
from datapackage import Package
from dataflows_serverless.constants import *


# runs the source_chain with steps marked as serverless replaced for serverless processing
def get_primary_chain(source_chain, num_secondaries, workdir):
    chain = []
    for step_idx, step in enumerate(source_chain):
        serverless_step_config = getattr(step, '__serverless_step', None)
        if serverless_step_config:
            complete_file = PRIMARY_STEP_COMPLETE_FILE_TEMPLATE.format(workdir=workdir, step_idx=step_idx)
            makedirs(path.dirname(complete_file), exist_ok=True)
            chain.append(dump_to_path(PRIMARY_INPUT_DATAPACKAGE_PATH_TEMPLATE.format(
                workdir=workdir, step_idx=step_idx)))
            chain.append(primary_input_rows_counter(serverless_step_config, workdir, step_idx))
            Flow(*chain).process()
            notify_primary_step_complete(workdir, step_idx)
            wait_for_secondaries(step_idx, num_secondaries, workdir)
            chain = [load(PRIMARY_INPUT_DATAPACKAGE_FILE_TEMPLATE.format(workdir=workdir, step_idx=step_idx)),
                     get_joined_secondaries_output(num_secondaries, workdir, serverless_step_config, step_idx)]
        else:
            chain.append(step)
    return chain


def primary_input_rows_counter(serverless_step_config, workdir, step_idx):
    def step(rows):
        if rows.res.name == serverless_step_config['resource_name']:
            i = 0
            for row in rows:
                i += 1
                yield row
            complete_file = PRIMARY_STEP_COMPLETE_FILE_TEMPLATE.format(workdir=workdir, step_idx=step_idx)
            with open(path.join(path.dirname(complete_file), 'rows_count'), 'w') as f:
                f.write(str(i))
        else:
            yield from rows
    return step


# notifies the secondaries that they can start processing
def notify_primary_step_complete(workdir, step_idx):
    print('primary: notify secondaries that primary step {} is complete'.format(step_idx))
    complete_file = PRIMARY_STEP_COMPLETE_FILE_TEMPLATE.format(workdir=workdir, step_idx=step_idx)
    with open(complete_file, 'w') as f:
        json.dump({'step_idx': step_idx}, f)


def wait_for_secondaries(step_idx, num_secondaries, workdir):
    secondaries_stats = {}
    print('primary: waiting for step {} secondaries to complete'.format(step_idx))
    while len(secondaries_stats) < num_secondaries:
        sleep(WAIT_FOR_SECONDARIES_DELAY_SECONDS)
        for secondary in [s for s in range(num_secondaries) if s not in secondaries_stats]:
            secondary_stats = get_secondary_stats(workdir, secondary, step_idx)
            if secondary_stats and secondary_stats['step_idx'] == step_idx:
                secondaries_stats[secondary] = secondary_stats
                print('primary: step {} secondary {} complete'.format(step_idx, secondary))
                print(secondary_stats)
    assert all([stats.get('success') for stats in secondaries_stats.values()]), \
        'primary: step {} some secondaries failed, aborting'.format(step_idx)
    print('primary: step {} secondaries complete'.format(step_idx))


# when secondary stats are available it also means secondary finished processing
def get_secondary_stats(workdir, secondary, step_idx):
    stats_file = SECONDARY_STATS_FILE_TEMPLATE.format(workdir=workdir, secondary=secondary,
                                                      step_idx=step_idx)
    if path.exists(stats_file):
        with open(stats_file) as f:
            return json.load(f)
    else:
        return None


# yield the rows from all secondaries' outputs
def get_joined_secondaries_output(num_secondaries, workdir, serverless_step_config, step_idx):
    def step(package: PackageWrapper):
        yield package.pkg
        for resource in package:
            if resource.res.name == serverless_step_config['resource_name']:
                yield get_joined_secondaries_rows(num_secondaries, workdir, serverless_step_config, step_idx)
            else:
                yield resource
    return step


def get_joined_secondaries_rows(num_secondaries, workdir, serverless_step_config, step_idx):
    print('primary: step {} yielding joined secondary data'.format(step_idx))
    for secondary in range(num_secondaries):
        datapackage_file = SECONDARY_OUTPUT_DATAPACKAGE_FILE_TEMPLATE.format(workdir=workdir,
                                                                             secondary=secondary,
                                                                             step_idx=step_idx)
        dp = Package(datapackage_file)
        r = dp.get_resource(serverless_step_config['resource_name'])
        for row in r.iter(keyed=True):
            yield row
