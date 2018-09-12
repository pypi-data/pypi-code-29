"""Make Pyramid routes and the route_path() function available to JS.

...in the client, under the name "jurl()".
"""


def treated_routes(config, base_path='/'):
    """A dict containing each of the routes configured in this application.

    In your app configuration, ``config.make_wsgi_app()`` must be
    called *before* routes are extracted::

        app = config.make_wsgi_app()
        config.registry.app_routes = treated_routes(config)
        return app

    The return value is a dict like this::

         {'__static': '/static',  # static routes start with "__"
          'activate': '/activate/{user_id}/{code}'}
    """
    adict = {}
    for route in config.get_routes_mapper().routes.values():
        name = route.name.rstrip('/')
        pattern = route.pattern.strip('/')  # remove the slash from both sides
        if pattern.endswith("/*subpath"):
            pattern = pattern[:-9]
        adict[name] = base_path + pattern
    return adict


def routes_as_json(config, base_path='/'):
    from json import dumps
    return dumps(treated_routes(config, base_path=base_path))


def write_routes_js_file(config, file_path, base_path='/'):
    routes = routes_as_json(config, base_path=base_path)
    prefix = config.registry.settings.get('scheme_domain_port')
    if prefix:
        prefix = '"' + prefix + '"'
    else:
        prefix = 'window.location.protocol + "//" + window.location.host'
    with open(file_path, 'w') as js_file:
        js_file.write(JS_TEMPLATE.replace('{routes}', routes).replace(
            '{scheme_domain_port}', prefix))


JS_TEMPLATE = '''"use strict";
// Do not edit this file; it is autogenerated.

window.jurl = function (routes) {
    // Usage: jurl(ROUTE_NAME, key1, val1, key2, val2...)
    return function() {
        // Copy arguments to args
        var args = [];
        for (var i = 0; i < arguments.length; i++) {
            args.push(arguments[i]);
        }
        var name = args.shift();
        var s = routes[name];
        if (!s)  throw 'jurl: No route called ' + name;
        while (args.length > 0) {
            var key = args.shift();
            var placeholder = '{' + key + '}';
            if (s.indexOf(placeholder) == -1) {
                throw 'jurl: Route "' + name + '" does not have placeholder: '
                    + placeholder;
            }
            var val = args.shift();
            if (val == null)  throw 'jurl: Missing value for placeholder '
                + placeholder + ' of route "' + name + '"';
            s = s.replace(placeholder, val);
        }
        return s;
    }
}({routes});

window.schemeDomainPort = {scheme_domain_port};
'''
