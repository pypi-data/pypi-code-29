from ruamel import yaml
from datadog_deployer.monitor import Monitor


def calculate_operations(new_monitors: list('Monitor')):
    monitors = {v['name']: v for v in new_monitors}
    deployed = {v['name']: v for v in Monitor.read_all()}

    insert = []
    delete = []
    update = []
    noop = []

    for name, monitor in monitors.items():
        if name in deployed:
            if monitor.normalized() == deployed[name].normalized():
                noop.append(monitor)
            else:
                monitor['id'] = deployed['name']['id']
                update.append(monitor)
        else:
            insert.append(monitor)

    for name, monitor in deployed.items():
        if name not in monitors:
            monitor['id'] = deployed['name']['id']
            delete.append(monitor)

    return (insert, update, delete, noop)


def deploy(filename, verbose=True, dry_run=True):
    with open(filename, 'r') as stream:
        dsc = yaml.load(stream, Loader=yaml.Loader)

    monitors = map(lambda m: Monitor(m), dsc['monitors'])
    inserts, updates, deletes, noops = calculate_operations(monitors)
    print('INFO: {} inserts, {} updates, {} deletes and {} unchanged.'.format(
        len(inserts), len(updates), len(deletes), len(noops)))

    for name, monitor in inserts:
        if verbose:
            print('INFO: inserting {}'.format(name))
        if not dry_run:
            monitor.create()

    for name, monitor in updates:
        if verbose:
            print('INFO: updating {}'.format(name))
        if not dry_run:
            monitor.update()
    for name, monitor in deletes:
        if verbose:
            print('INFO: deleting {}'.format(name))
        if not dry_run:
            monitor.delete()
