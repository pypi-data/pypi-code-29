from pprint import pprint
import subprocess
import urllib3
import json
import os


def project_script(name):
    try:
        subprocess.call('./project-' + name, shell=True)
    except OSError:
        print 'Skip build command execution'

def send_slack(channel, msg):
    url = "https://hooks.slack.com/services/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"
#    url = "https://hooks.slack.com/services/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" @my
    payload = {'text': msg, 'channel': channel}
    http = urllib3.PoolManager()
    r = http.request('POST', url, fields={'payload': json.dumps(payload)})


def is_git_master():
    cmd = ['git', 'branch', '--no-color']
    output = subprocess.check_output(cmd)
    branch = [line for line in output.split('\n') if line.startswith('*')][0]
    if branch == '* master':
        return True


def get_git_lines(from_commit):
    commits_info = '{}..HEAD'.format(from_commit)
    cmd = ['git', 'log', '--pretty=format:"%h %s @%an"', '--no-color',
           '--abbrev-commit', commits_info]
    try:
        output = subprocess.check_output(cmd)
        return output
    except Exception:
        print('some git logs error')

def get_last_commit():
    cmd = ['git', 'log', '-n1', '--oneline']
    try:
        output = subprocess.check_output(cmd)
        return output.split()[0]
    except Exception:
        print ('cant find last commit hash')

def get_deployer_name():
    logname = os.getenv("LOGNAME")
    return logname if logname else 'Undefined'
