import os
import sys
import time
import platform
import tempfile
import subprocess
from configparser import ConfigParser


def print_help():
    print("""
Usage: jennfier run <startup_command ...>

startup_command: your wsgi service startup command and options
""")


def run_master(bin, config_path, log_path, sock_file):
    arch = {
        'x86_64': 'amd64',
        'x86': '386',
    }[platform.machine()]

    path = os.path.join(bin, sys.platform, arch, 'jennifer_agent')
    log_stream = open(log_path, 'w+')
    process = subprocess.Popen(
        [
            path,
            config_path,
            sock_file,
        ],
        stdout=log_stream,
        stderr=log_stream,
    )

def run(args):
    if len(args) < 2:
        print_help()
        return
    startup_path = args[1]
    config_path = os.environ.get('JENNIFER_CONFIG_FILE')
    if config_path is None:
        raise EnvironmentError("JENNIFER_CONFIG_FILE is not set")
    config_path = os.path.join(os.getcwd(), config_path)
    if not os.path.exists(config_path):
        raise FileNotFoundError(config_path + " not exist")

    root_dir = os.path.dirname(__import__('jennifer').__file__)
    bootstrap = os.path.join(root_dir, 'bootstrap')

    python_path = bootstrap
    if 'PYTHONPATH' in os.environ:
        path = os.environ['PYTHONPATH'].split(os.path.pathsep)
        if bootstrap not in path:
            python_path = os.path.pathsep.join([bootstrap] + path)
    os.environ['PYTHONPATH'] = python_path

    if not os.path.dirname(startup_path):
        for path in os.environ.get('PATH', '').split(os.path.pathsep):
            path = os.path.join(path, startup_path)
            if os.path.exists(path) and os.access(path, os.X_OK):
                startup_path = path
                break

    if not os.path.exists(startup_path):
        raise FileNotFoundError('{0} not found'.format(startup_path))

    sock = os.path.join(tempfile.gettempdir(), 'jennifer-%d.sock' % time.time())
    os.environ['JENNIFER_MASTER_ADDRESS'] = sock
    config = ConfigParser()
    config.read(config_path)
    log_path = config['JENNIFER'].get(
        'log_path', '/tmp/jennifer-python-agent.log')
    os.environ['JENNIFER_LOG_PATH'] = log_path

    # Start!
    pid = os.fork()
    if pid > 0:  # parent process
        os.waitpid(pid, 0)
        os.execl(startup_path, *args[1:])
    else:  # child process
        run_master(os.path.join(root_dir, 'bin'), config_path, log_path, sock)
