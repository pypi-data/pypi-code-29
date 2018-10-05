from zope import interface

class ISparcYamlConfigContainers(interface.Interface):
    def containers(yaml_config, render_context=None):
        """Generator of sparc.config.IConfigContainer providers
        
        Args:
            yaml_config: Unicode valid file path to a Yaml configuration or a 
                         valid Yaml content string.
            render_context: A mapping that will be used as the context for
                            template rendering.
        """
    def first(yaml_config, render_context=None):
        """first sparc.config.IConfigContainer provider in yaml_config
        
        Args:
            yaml_config: [same as documents()]
            render_context: [same as documents()]
        """