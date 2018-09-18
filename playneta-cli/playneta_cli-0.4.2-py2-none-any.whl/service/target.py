import uuid


class Target:
    def __init__(self, file_root, options):
        self._file_root = file_root
        self._file_separator = str(uuid.uuid4()) + '--'
        self._component = options['component']
        self._lang = options['lang']
        self._params = options['params']

    def file_separator(self):
        return self._file_separator

    def template_path(self):
        return self._file_root + '/codegen/' + self._lang + '/' + self._component

    def language(self):
        return self._lang

    def meta(self):
        root = self._params['root']
        namespace = self._params['namespace']

        return {
            'namespace': namespace,
            'package': namespace.split('.').pop(),
            'root': root + '/' + '/'.join(namespace.split('.'))
        }
