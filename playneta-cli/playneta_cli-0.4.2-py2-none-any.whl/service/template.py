import inflection
import jinja2

LANG_PHP = 'php'

MACRO = """
{%- macro file(path, new_name='', key='') -%}
    {{ '\n' + __file_separator }}
    {%- if new_name == '' -%}
        {{ path }}
    {%- else -%}
        {{ new_name }}
    {%- endif -%}
    {{ '\n' }}

    {%- include __input_path + '/' + path + '.j2' -%}
{%- endmacro -%}
"""

MACRO_TYPESCRIPT = """
{%- macro type(schema, namespace='') -%}
    {%- set sort, type = schema|schema -%}

    {% if sort == 'class' -%}
        {{ namespace }}{{ type|classname }}
    {%- elif sort == 'array' -%}
        {{ array_type(type, namespace) }}
    {%- elif sort == 'mixed' -%}
        {{ mixed_type(type) }}
    {%- else -%}
        void
    {%- endif -%}
{%- endmacro -%}

{%- macro array_type(schema, namespace) -%}
    {%- set sort, type = schema|schema -%}

    {%- if sort == 'class' -%}
        {{ namespace }}{{ type|classname }}[]
    {%- elif sort == 'array' -%}
        {{ array_type(type, namespace) }}[]
    {%- else -%}
        {{ mixed_type(type) }}[]
    {%- endif -%}
{%- endmacro -%}

{%- macro mixed_type(type) -%}
    {%- if type == 'number' or type == 'integer'  -%}
        number
    {%- elif type == 'string' -%}
        string
    {%- elif type == 'boolean' or type == 'bool' -%}
        boolean
    {%- else -%}
        unknown
    {%- endif -%}
{%- endmacro -%}
"""

MACRO_PHP = """
{%- macro type(schema, namespace='', suffix='') -%}
    {%- set sort, type = schema|schema -%}

    {%- if sort == 'class' -%}
        {{ namespace }}{{ type|classname }}{{ suffix }}
    {%- elif sort == 'array' -%}
        array
    {%- elif sort == 'mixed' -%}
        {{ mixed_type(type) }}
    {%- else -%}
        void
    {%- endif -%}
{%- endmacro -%}

{%- macro array_type(schema, namespace, suffix) -%}
    {%- set sort, type = schema|schema -%}

    {%- if sort == 'class' -%}
        {{ namespace }}{{ type|classname }}{{ suffix }}[]
    {%- elif sort == 'array' -%}
        {{ array_type(type, namespace, suffix) }}[]
    {%- else -%}
        {{ mixed_type(type) }}[]
    {%- endif -%}
{%- endmacro -%}

{%- macro mixed_type(type) -%}
    {%- if type == 'number' -%}
        float
    {%- elif type == 'integer' -%}
        int
    {%- elif type == 'boolean' or type == 'bool' -%}
        bool
    {%- elif type == 'string' -%}
        string
    {%- elif type == 'object' -%}
        \stdClass
    {%- else -%}
        \JsonSerializable
    {%- endif -%}
{%- endmacro -%}

{%- macro comment_type(schema, namespace='', suffix='') -%}
    {%- set sort, type = schema|schema -%}

    {% if sort == 'class' -%}
        {{ namespace }}{{ type|classname }}{{ suffix }}
    {%- elif sort == 'array' -%}
        {{ array_type(type, namespace, suffix) }}
    {%- elif sort == 'mixed' -%}
        {{ mixed_type(type) }}
    {%- else -%}
        void
    {%- endif -%}
{%- endmacro -%}

{% macro input_decoder(schema, namespace='', suffix='', method='DECODER') -%}
    {%- set sort, type = schema|schema -%}

    {%- if sort == 'class' -%}
        {{ namespace }}{{ type|classname }}{{ suffix }}::{{ method }}
    {%- elif sort == 'array' -%}
        {% set decoder -%}
            {{ input_decoder(type, namespace, suffix, method) }}
        {%- endset %}

        {%- if decoder != '' -%}
            function($array) { return array_map({{ decoder }}, $array); }
        {%- endif -%}
    {%- endif -%}
{%- endmacro %}
"""


def classname(name):
    tokens = name.replace('/', '-').split('-')

    return inflection.camelize(tokens[-1])


def methodname(name):
    return inflection.camelize('_'.join(name.split('/')), False)


def resources(paths):
    result = set()

    for path in paths:
        result.add(path_resource(path))

    return result


def path_resource(path):
    return path.strip('/').split('/')[0]


def schema(data):
    if '$ref' in data:
        return 'class', data['$ref'].split('/')[-1]

    if 'type' in data:
        if data['type'] != 'array':
            return 'mixed', data['type']
        else:
            return 'array', data['items']

    raise Exception('Invalid type schema.')


def optional(data):
    return 'optional' in data and data['optional']


def path_method(path):
    prefix = '/' + path_resource(path)
    return methodname(path[1 + len(prefix):])


def methods(paths, resource):
    result = []

    for key, data in paths.iteritems():
        prefix = '/' + resource
        if key.startswith(prefix):
            item = {}

            response = data.get('post', {}).get('responses', {}).get(200, {})
            if 'schema' in response:
                item['output'] = response['schema']

            parameters = data.get('post', {}).get('parameters', [])
            if len(parameters) > 0 and 'schema' in parameters[0]:
                item['input'] = parameters[0]['schema']

            result.append((key[1 + len(prefix):], item))

    return sorted(result)


def render(target, service):
    """
    :param {Target} target:
    :param {dict} service:
    :return {list}:
    """
    input_path = target.template_path()
    target_macro = MACRO

    if target.language() == 'typescript':
        target_macro += MACRO_TYPESCRIPT
    elif target.language() == 'php':
        target_macro += MACRO_PHP

    env = jinja2.Environment(loader=jinja2.ChoiceLoader([
        jinja2.FileSystemLoader('/'),
        jinja2.DictLoader({
            'playneta': (
                "{% set __input_path = '" + input_path + "' %}"
                "{% set __file_separator = '" + target.file_separator() + "' %}" + target_macro
            )
        })
    ]))

    env.filters['classname'] = classname
    env.filters['methodname'] = methodname
    env.filters['resources'] = resources
    env.filters['methods'] = methods
    env.filters['schema'] = schema
    env.filters['optional'] = optional
    env.filters['path_resource'] = path_resource
    env.filters['path_method'] = path_method

    template = env.get_template(input_path + '/index.j2')
    context = {'meta': target.meta()}
    context.update(service)

    return template.render(context).splitlines()
