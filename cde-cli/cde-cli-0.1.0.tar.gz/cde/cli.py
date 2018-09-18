# -*- coding: utf-8 -*-

"""Console script for cde."""
import os
from pathlib import Path

import click
import git

from . import config
# import cde.container


CFG = None


@click.group()
def main():
    global CFG
    CFG = config.load()
    if not config.validate(CFG):
        sys.exit(1)


# @main.command()
# def shell():
#     cm = cde.container.Docker()
#     cm.shell(cfg['image'], cfg['tag'])


@main.command()
def clone():
    for name, repo in CFG['repos'].items():
        path = Path('.') / name

        if os.path.exists(path):
            # todo check remote URL
            print('✔ {} already exists'.format(name))
        else:
            print('▽ {} cloning...'.format(name), end='', flush=True)
            git_repo = git.Repo.clone_from(repo['url'], str(path))
            print('\r⚑ {} cloned    '.format(name))

        # TODO ensure we are on the right commit

def env_var_name(name):
    name = name.upper().replace('-', '_')
    return name


@main.command()
def env():
    for name, repo in ctx.obj['cfg']['repos'].items():
        env_var = env_var_name(name)
        print('{}={}'.format(env_var, repo['commit']))


@main.command()
def check():
    import cde.check
    cde.check.main()


if __name__ == "__main__":
    main()
