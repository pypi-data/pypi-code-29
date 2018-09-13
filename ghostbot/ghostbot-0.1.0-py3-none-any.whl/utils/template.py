from jinja2 import Template
from ghostbot import StatusCode
from ghostbot.core import Basis
from ghostbot.utils.logger import Logger
from ghostbot.utils.os import Hash, FileSystem as fs


class TemplateEngine(Basis):

    def __init__(self):
        super().__init__()
        self.logger = Logger(__name__)
        self._cache = {}

    def _load(self, template_file):
        result = None
        if fs.exists(template_file):
            key = Hash.digest(template_file, digit=8)
            if key not in self._cache:
                with open(template_file) as file:
                    result = Template(file.read())
                    self._cache[key] = result
            else:
                result = self._cache[key]
        else:
            self.error(StatusCode[504], template_file)
        return result

    def render(self, template_file, params=None):
        result = None
        try:
            template = self._load(template_file)
            result = template.render(params)
        except Exception as e:
            self.error(StatusCode[610], e.args)
        return result

    def build(self, output_file, template_file, params=None):
        directory = fs.directory(output_file)
        if fs.exists(directory):
            data = self.render(template_file, params)
            with open(output_file, "w") as file:
                file.write(data)
        else:
            self.error(StatusCode[505], directory)
