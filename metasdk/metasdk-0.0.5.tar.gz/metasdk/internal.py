"""

ВНИМАНИЕ! Только для использования внутри кода SDK
Запрещено добавление общих утилит в этот файл

"""
import platform
from os.path import expanduser

import os

import json


def read_developer_settings():
    """
    Читает конфигурации разработчика с локальной машины или из переменных окружения
    При этом переменная окружения приоритетнее

    :return: dict|None
    """
    ret = None

    dev_key_path = "/.rwmeta/developer_settings.json"
    if OS_NAME == "windows":
        dev_key_path = dev_key_path.replace("/", "\\")
    dev_key_full_path = expanduser("~") + dev_key_path
    if os.path.isfile(dev_key_full_path):
        with open(dev_key_full_path, 'r') as myfile:
            ret = json.loads(myfile.read())

    env_developer_settings = os.environ.get('META_SERVICE_ACCOUNT_SECRET', None)
    if not env_developer_settings:
        env_developer_settings = os.environ.get('X-META-Developer-Settings', None)
    if env_developer_settings:
        ret = json.loads(env_developer_settings)

    return ret


def __get_os():
    if os.name == "nt":
        return "windows"

    if platform.system() == "Darwin":
        return "macos"

    return "linux"


OS_NAME = __get_os()
