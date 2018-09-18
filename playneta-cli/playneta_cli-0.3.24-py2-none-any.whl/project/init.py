import subprocess
import util


def help(parser):
    pass


def command(project, args, file_root):
    util.project_script('init')

    subprocess.call('cp -rT ' + file_root + '/boilerplate .', shell=True)
    subprocess.call('ansible-galaxy install -f -r .ansible/requirements.yml',
                    shell=True)
