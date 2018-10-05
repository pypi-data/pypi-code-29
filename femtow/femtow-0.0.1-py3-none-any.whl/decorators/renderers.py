import json

from mako.template import Template


def string_(view_dict, response):
    response.text = view_dict


def json_renderer(view_dict, response):
    response.text = json.dumps(view_dict)
    response.headers['Content-Type'] = 'application/json; charset=UTF-8'


def mako_renderer(template):
    template = Template(filename=template)

    def template_renderer(view_dict, response):
        response.text = template.render(**view_dict)

    return template_renderer


def http_exception_renderer(status):
    template = Template(filename='./femtow/templates/http-exception.mako')

    def http_exception_renderer_(view_dict, response):
        response.text = template.render(status=status, **view_dict)
        response.status = status

    return http_exception_renderer_
