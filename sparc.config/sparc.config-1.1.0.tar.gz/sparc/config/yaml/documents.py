from os.path import isfile
import yaml
from zope import interface
from jinja2 import Template

from sparc.config.container import SparcConfigContainer
from .interfaces import ISparcYamlConfigContainers

@interface.implementer(ISparcYamlConfigContainers)
class SparcYamlConfigContainers(object):

    def containers(self, yaml_config, render_context=None):
        config = yaml_config if not isfile(yaml_config) else open(yaml_config).read()
        if render_context:
            config = Template(config).render(render_context)
        for doc in yaml.load_all(config):
            yield SparcConfigContainer(doc)

    def first(self, yaml_config, render_context=None):
        return next(self.containers(yaml_config,render_context))