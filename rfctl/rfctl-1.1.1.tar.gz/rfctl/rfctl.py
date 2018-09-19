# -*- coding: utf-8 -*-

import base64
import json
import os
import re
import subprocess
import sys
import tarfile
from collections import defaultdict
from datetime import datetime
from io import BytesIO

import click
import refunc
import yaml
from refunc import version as rf_version
from refunc import Context, Message, current_env
from rfctl import version
from rfctl.util import gen_sh_util

from . import dirtools


@click.group()
@click.option('--debug/--no-debug', default=True)
def cli(debug=False):
    if debug:
        from refunc.util import enable_logging

        env = current_env().new(pull_logs=True)
        refunc.push_env(env)
        enable_logging()


@cli.command(name="version")
def print_version():
    '''
    print version
    '''
    print('rfctl version:  {}'.format(version))
    print('refunc version: {}'.format(rf_version))


ID_PATTERN = re.compile('^([a-z0-9][-a-z0-9_.]*)?[a-z0-9]$')


def validate_id(ctx, param, value):
    try:
        ns, name = value.split('/', 2)
        if not ID_PATTERN.match(name):
            raise ValueError(
                "name must consist of alphanumeric characters, ' - ',"
                " '_' or '.', "
                "and must start and end with an alphanumeric character"
            )
        return (ns, name)
    except ValueError as e:
        raise click.BadParameter('be the form of "namespace/name", {}'.format(e))


VALID_RUNTIMES = ['python']


@cli.command()
@click.argument('id', default='', type=click.STRING)
@click.option(
    '--id',
    callback=validate_id,
    type=click.STRING,
    prompt='The id of the func(namespace/name)',
)
@click.option(
    '--runtime',
    'env',
    type=click.Choice(VALID_RUNTIMES),
    prompt='Choose runtime:\n-  {}\n> '.format('\n-  '.join(VALID_RUNTIMES)),
    default='python',
)
@click.option(
    '--init-git', 'git_init', prompt='Init git repo', type=click.BOOL, default=False
)
@click.option('--target-dir', 'target_dir', default='', type=click.STRING)
@click.option(
    '--xenv',
    'xenvname',
    help="Override template's default runner",
    default='',
    type=click.STRING,
)
def new(id: str, env: str, git_init: bool, target_dir: str, xenvname: str):
    '''
    create a new func in current folder
    '''
    ns, name = id
    dirctx = os.path.abspath(os.getcwd() if not target_dir else target_dir)
    dirname = to_camel_case(name)
    target = os.path.join(dirctx, dirname)

    if os.path.exists(target):
        click.secho(
            'folder with the name {} already exsits'.format(dirname), err=True, fg='red'
        )
        sys.exit(1)

    click.secho('Creating "{}" in {}'.format('/'.join(id), dirname), fg='green')
    res = refunc.invoke(
        "refunc/builder", namespace=ns, name=name, template=env, xenvname=xenvname
    )
    fileobj = BytesIO(base64.decodebytes(res['data'].encode('utf-8')))

    os.makedirs(target)
    with tarfile.open(mode='r:gz', fileobj=fileobj) as tar:
        tar.extractall(target)

    if git_init:
        sh = gen_sh_util(target)
        sh('git init')
        sh('git add -A')
        sh("git commit -a " "-m '[+] Initial commit of {}/{}'".format(*id))


@cli.command()
@click.argument(
    'target',
    default=os.getcwd(),
    type=click.Path(exists=True, dir_okay=True, resolve_path=True),
)
@click.option('--output', '-o', default='', type=click.Choice(['', 'yaml', 'json']))
@click.option(
    '--force',
    help='force apply func, ignore git repo checking',
    default=False,
    type=click.BOOL,
    is_flag=True,
    show_default=True,
)
def apply(target: str, output: str, force: bool):
    '''
    update or create func under current dir context
    '''
    try:
        with open(os.path.join(target, 'refunc.yaml')) as f:
            fndef_obj = yaml.safe_load(f)
    except FileNotFoundError:
        click.secho(
            'cannot find refunc.yaml, ' '"{}" is not a valid refunc ctx'.format(target),
            err=True,
            fg='red',
        )
        sys.exit(1)

    ns, name = fndef_obj['metadata']['namespace'], fndef_obj['metadata']['name']
    idpath = '/'.join([ns, name])

    # check if target in under a git repo
    sh = gen_sh_util(target, True)
    res = sh('git rev-parse --is-inside-work-tree')
    is_git_repo = res.returncode == 0 and res.stdout.strip() == 'true'

    if is_git_repo:
        if force:
            click.secho(
                '"{}" is under a git repo, ' 'but --force is supplied'.format(idpath),
                err=True,
                fg='yellow',
            )
        else:
            click.secho(
                '"{}" is under a git repo, checking'.format(idpath),
                err=True,
                fg='green',
            )
            if not check_git_repo(target):
                click.secho(
                    '\nPlz fix the issue above, and try again', err=True, fg='red'
                )
                sys.exit(1)

    click.secho('Packing "{}"'.format(idpath), fg='green')

    # load excludes
    excludes = ['.git/', '.hg/', '.svn/']
    if os.path.exists(os.path.join(target, '.gitignore')):
        excludes += dirtools.load_patterns(os.path.join(target, '.gitignore'))
    if os.path.exists(os.path.join(target, '.refuncignore')):
        excludes += dirtools.load_patterns(os.path.join(target, '.refuncignore'))

    # .env should not in scm, but is needed for builder
    while '.env' in excludes:
        excludes.remove('.env')
    files_filter = dirtools.Dir(directory=target, excludes=excludes)

    # create tarfile
    buf = BytesIO()
    with tarfile.open(mode='x:gz', fileobj=buf) as tar:
        tar.add(target, arcname='', exclude=files_filter.is_excluded)

    click.secho('Applying "{}"'.format(idpath), fg='green')
    res = refunc.invoke(
        'refunc/builder',
        method='apply',
        data=base64.encodebytes(buf.getvalue()).decode('utf-8'),
    )
    if output == 'yaml':
        yaml.dump(res, sys.stdout)
    elif output == 'json':
        json.dump(res, sys.stdout, indent=2, sort_keys=True)
        sys.stdout.write('\n')
    else:
        click.secho('Done "{}"'.format(idpath), fg='green')
    return output


@cli.command()
@click.argument(
    'target',
    default=os.getcwd(),
    type=click.Path(exists=True, dir_okay=True, resolve_path=True),
)
def upgrade(target: str):
    try:
        with open(os.path.join(target, 'refunc.yaml')) as f:
            old = yaml.safe_load(f)
    except FileNotFoundError:
        click.secho(
            'cannot find refunc.yaml, ' '"{}" is not a valid refunc ctx'.format(target),
            err=True,
            fg='red',
        )
        sys.exit(1)

    apiver = old['apiVersion']
    ns, name = old['metadata']['namespace'], old['metadata']['name']
    idpath = '/'.join([ns, name])

    if apiver == 'k8s.refunc.io/v1':
        click.secho('{} is already the latest version'.format(idpath), fg='green')
        return

    if apiver != 'refunc.v87.xyz/v1':
        click.secho('Unsupported object "{}"'.format(apiver), err=True, fg='red')
        sys.exit(1)

    new = {
        'apiVersion': 'k8s.refunc.io/v1',
        'kind': 'Funcdef',
        'metadata': old['metadata'],
        'spec': {'maxReplicas': 1, 'runtime': {'name': 'python35', 'timeout': 9}},
    }

    if 'annotations' in new['metadata']:
        anno = new['metadata']['annotations']
        if 'sys.refunc.v87.us/builder' in anno:
            anno['sys.funcs.refunc.io/builder'] = anno.pop('sys.refunc.v87.us/builder')

    if 'storePath' in old['spec'] and 'hash' in old['spec']:
        new['spec']['body'] = old['spec']['storePath']
        new['spec']['hash'] = old['spec']['hash']

    if 'entry' in old['spec']:
        new['spec']['entry'] = old['spec']['entry']

    if 'replicas' in old['spec']:
        new['spec']['maxReplicas'] = old['spec']['replicas']

    if 'meta' in old['spec']:
        new['spec']['meta'] = old['spec']['meta']

    if 'runner' in old['spec']:
        new['spec']['runtime'] = {'name': old['spec']['runner']['name']}
        if 'config' in old['spec']['runner']:
            cfg = old['spec']['runner']['config']
            if 'envs' in cfg:
                new['spec']['runtime']['envs'] = cfg['envs']
            if 'maxTimeout' in cfg:
                new['spec']['runtime']['timeout'] = cfg['maxTimeout']
            if 'systemFunc' in cfg:
                new['spec']['runtime']['systemFunc'] = cfg['systemFunc']

    with open(os.path.join(target, 'refunc.yaml'), 'w') as f:
        yaml.dump(new, f, default_flow_style=False)
        click.secho('{} upgraded to latest version'.format(idpath), fg='green')


@cli.command()
@click.argument('funcs', nargs=-1, type=click.STRING)
def logs(funcs: [str]):
    # merge topics
    topicmap = defaultdict(dict)
    for f in funcs:
        splitted = f.split('/')
        if len(splitted) != 2:
            click.secho('invalid endpoint: {}'.format(f), err=True, fg='red')
            sys.exit(1)
        ns, name = splitted
        # only set when current ns is not listed
        if '*' not in topicmap[ns]:
            topicmap[ns][name] = ns + "." + name

    funcs = []
    for ns in topicmap:
        funcs += [topicmap[ns][name] for name in topicmap[ns]]

    if not funcs:
        click.secho('func\'s endpoint is not set', err=True, fg='red')
        sys.exit(1)

    try:
        import asyncio
        from refunc.func_nats import nats_conn
        from refunc.util import start_or_get_running_loop, get_default_threadpool
    except ImportError:
        click.secho(
            'refunc version({}) is to low to support pull logs'.format(rf_version),
            err=True,
            fg='red',
        )
        sys.exit(1)

    colors = ['green', 'blue', 'yellow', 'magenta', 'cyan']

    def color_picker():
        nonlocal colors
        color, colors = colors[0], colors[1:]
        colors.append(color)
        return color

    topic2color = defaultdict(color_picker)

    async def pull(msg):
        topic = '/'.join(msg.subject.split('.')[1:3])
        click.echo(
            click.style(
                '{}Z {}] '.format(datetime.utcnow().isoformat()[:-3], topic),
                fg=topic2color[topic],
            )
            + msg.data.decode(),
            sys.stderr,
        )

    # event loop in main thread
    loop = asyncio.get_event_loop()

    async def sub():
        click.secho(
            'start pulling logs from "{!r}"'.format(funcs), err=True, fg='yellow'
        )
        # ensure nc
        nc = None
        while True:
            nc, = await asyncio.gather(
                loop.run_in_executor(get_default_threadpool(), nats_conn)
            )
            if nc:
                break
            click.echo(
                click.style('connecting to refunc, plz wait', fg='yellow'),
                file=sys.stderr,
            )
            await asyncio.sleep(0.2)
        for func in funcs:
            subject = 'refunc.' + func + '.logs.*'
            await nc.subscribe(subject, cb=pull)

    loop.create_task(sub())

    try:
        start_or_get_running_loop(loop=loop, run_in_backgroud=False)
    except KeyboardInterrupt:
        click.secho('\r\npull logs from stopped', err=True, fg='yellow')

@cli.command()
@click.argument('func', type=click.STRING)
@click.option('--data', '-d', default='{}')
def call(func: str, data: str):
    from refunc.errors import ResultError
    func = func.strip('/')
    try:
        if '.' in func:
            func = '/'.join(func.split('.'))
        if len(func.split('/')) != 2:
            click.secho(f'bad endpoint: "{func}"', err=True, fg='red')
            sys.exit(1)
        request = json.loads(data)
        result = refunc.invoke(func, request)
        if result:
            import pprint
            pprint.pprint(result, indent=2, width=120)
    except ResultError as e:
        click.secho(e.msg, err=True, fg='red')


def check_git_repo(target: str) -> bool:
    _sh = gen_sh_util(target, True)

    def sh(cmd):
        res = _sh(cmd)
        return (
            res.returncode,
            ' '.join(res.stdout.split('\n')).strip(),
            ' '.join(res.stderr.split('\n')).strip(),
        )

    # check if current repo is clean
    code, stdout, stderr = sh(
        '''set -e
    git status --untracked-files=no --porcelain
    '''
    )
    if stdout:
        click.secho('repo is not clean, plz commit your changes:', err=True, fg='red')
        click.secho('\t' + stdout, err=True, fg='yellow')
        return False

    # check if current repo is clean
    code, stdout, stderr = sh(
        '''set -e
        git remote update >/dev/null
        LOCAL=$(git rev-parse @)
        REMOTE=$(git rev-parse @{u})
        BASE=$(git merge-base @ @{u})
        if [ $LOCAL = $REMOTE ]; then
            echo "up to date"
        elif [ $LOCAL = $BASE ]; then
            echo "using git to pull from remote"
        elif [ $REMOTE = $BASE ]; then
            echo "push push your local to remote"
        else
            echo "diverged"
        fi
    '''
    )
    if code != 0:
        click.secho('plz ensure your repo has a remote.\n' + stderr, err=True, fg='red')
        return False
    if stdout != 'up to date':
        click.secho(
            'your repo is outout sync with remote, you need:', err=True, fg='red'
        )
        click.secho('\t' + stdout, err=True, fg='yellow')
        return False

    return True


def to_camel_case(snake_str: str) -> str:
    # We capitalize the first letter of each component except the first one
    # with the 'title' method and join them together.
    return "".join(x.title() for x in snake_str.split('-'))


if __name__ == '__main__':
    cli()
