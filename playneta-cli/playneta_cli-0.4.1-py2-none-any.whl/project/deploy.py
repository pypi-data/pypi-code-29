# -*- coding: utf-8 -*-
import subprocess
from pprint import pprint
import sys

import util



def help(parser):
    parser.add_argument('--role',
                        dest='role',
                        required=True,
                        choices=['dev', 'admin'],
                        help='deploy role ')

    parser.add_argument('--env',
                        dest='env',
                        required=True,
                        help='deploy environment')

def command(project, args, file_root):
    user = 'root'

    if args.role == 'dev':
        user = project['name']

    util.project_script('deploy ' + args.env)

    subprocess.call('ansible-playbook '
                    '-e "ansible_user=' + user + '" '
                    '-l ' + args.env + ' '
                    '-i .ansible/inventory.py '
                    '.ansible/playbook.yml', shell=True)

    if util.is_git_master():
        deployer_name = util.get_deployer_name()
        last_hash = project.get('deploy_hash')
        if last_hash:
            git_logs = util.get_git_lines(last_hash)
            msg = "Deploy to {}, by {}\n\n{}".format(args.env, deployer_name, git_logs)
            project['deploy_hash'] = util.get_last_commit()

            channel = project.get('notify_channel')
            if channel:
                util.send_slack('#' + channel, msg)
