#!/usr/bin/env python3
import os
import json
import hgapi
import subprocess
import fnmatch
import argparse


class ModifiedCondition:
    def __init__(self, config_dict):
        self.glob = config_dict['glob']

    def test(self):

        if not os.environ('HG_NODE'):
            return False

        repo = hgapi.Repo('.')
        modified = self.get_changed(repo, os.environ['HG_NODE'], 'tip')
        for changed in modified:
            if fnmatch.fnmatch(changed, self.glob):
                return True
        return False

    def get_changed(self, repo, start, end):
        style = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                             "filelist.txt")
        files = set((f for f in repo.hg_log(identifier="{}:{}".format(
            start, end), style=style).split("\n") if f))
        return files


class BranchCondition:
    def __init__(self, config_dict):
        self.branch = config_dict['branch']

    def test(self):
        repo = hgapi.Repo('.')
        return repo.hg_branch() == self.branch


class ShellDeploy:
    def __init__(self, config_dict):
        self.conditions = [CONDITIONS[c['type']](c) for c in
                           config_dict.get('conditions')] or []
        self.cwd = config_dict.get('cwd', '.')
        self.command = config_dict['command']

    def execute(self):
        return subprocess.call(self.command, cwd=self.cwd, shell=True)


DEPLOY = {
    'sh': ShellDeploy
}

CONDITIONS = {
    "modified": ModifiedCondition,
    "branch": BranchCondition,
}


def check_conditions(node):
    if not node.conditions:
        return True
    return all((condition.test()
                for condition in node.conditions))


def run_meep(config, cwd, verbose):
    curdir = os.path.abspath(os.curdir)
    try:
        if verbose:
            print("CWD to ", cwd)
        os.chdir(cwd)
        deploy = config.get("deploy")

        if deploy is not None:
            for deploy_step in deploy:
                deploy = DEPLOY[deploy_step['type']](deploy_step)
                if check_conditions(deploy):
                    deploy.execute()
                else:
                    print("Skipping deploy step")
            print("Deploy Done")
    finally:
        os.chdir(os.curdir)


def meep_config(filepath):
    return json.load(open(filepath))


def find_meeps(path='.'):
    for root, dirs, files in os.walk(path):
        if "meep.json" in files:
            yield os.path.join(root, "meep.json")


def meep(update=False, update_ref='tip', verbose=False):
    repo = hgapi.Repo('.')

    if update:
        if verbose:
            print("Updating to ", update_ref)
        repo.hg_update(update_ref, clean=True)

    meeps = find_meeps()
    if not meeps:
        print('No meep config')
    for config in meeps:
        print("Using ", config)
        run_meep(meep_config(config), os.path.split(config)[0], verbose)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--update', action='store_true', default=False)
    parser.add_argument('-r', '--rev', type=str, default='tip')
    parser.add_argument('-v', '--verbose', action='store_true', default=False)
    args = parser.parse_args()
    meep(update=not args.no_update, update_ref=args.update_ref, verbose=args.verbose)


if __name__ == "__main__":
    main()
