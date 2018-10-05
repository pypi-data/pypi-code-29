import subprocess


def exec_cmd(cmd):
    subprocess.run(cmd, shell=True, check=True)
