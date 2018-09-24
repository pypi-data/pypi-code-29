import pybars
import logging
import pymicroconnectors.config as config

LOG = logging.getLogger(__name__)


def compile_to_string(folder: str, file_name: str, data: dict) -> str:
    file_path = f'{config.get_value("handlebars.templateFolder")}/{folder}/{file_name}'
    LOG.debug(f'Retrieving template from file [{file_path}]')
    compiler = pybars.Compiler()
    file = open(file_path, 'r', encoding="utf-8")
    file_string = file.read()
    template = compiler.compile(file_string)
    final_string = template(data)
    return final_string