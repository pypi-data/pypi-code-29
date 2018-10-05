from os.path import expanduser

import os
import subprocess

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    __CURRENT_DIR__ = os.getcwd() + "/"
    # Установка зависимостей для работы с gcloud endpoints
    subprocess.run('python3 -m pip install -r ' + __CURRENT_DIR__ + 'apis_requirements.txt', shell=True, check=True)
    googleapis_dir = expanduser("~") + '/grpc-api-common-protos'
    if not os.path.isdir(googleapis_dir):
        subprocess.run('git clone https://github.com/devision-io/api-common-protos ' + googleapis_dir, shell=True, check=True)
