import ast
import inspect
import re
import sys
import typing

import astor
import sphinx.ext.autodoc.importer
import sphinx.util.inspect


def format_annotation(annotation):
    return sphinx.util.inspect.Signature(format_annotation).format_annotation(annotation)


def process_signature(app, what, name, obj, options, signature, return_annotation):
    if not callable(obj):
        return

    if what in ('class', 'exception'):
        obj = getattr(obj, '__init__', getattr(obj, '__new__', None))

    if not getattr(obj, '__annotations__', None):
        return

    tmp = obj.__annotations__
    obj.__annotations__ = None
    result = sphinx.util.inspect.Signature(obj).format_args()
    obj.__annotations__ = tmp
    return result, None


def process_docstring(app, what, name, obj, options, lines):
    if what in ('attribute', 'data'):
        parts = name.split('.')
        mod_parts = [parts[0]]
        while len(mod_parts) < len(parts):
            if '.'.join(mod_parts + [parts[len(mod_parts)]]) in sys.modules:
                mod_parts += [parts[len(mod_parts)]]
            else:
                break
        mod = sys.modules['.'.join(mod_parts)]
        attr_name = parts[-1]
        parts = parts[len(mod_parts) : -1]
        container = mod
        while parts:
            container = getattr(container, parts[0])
            parts = parts[1:]
        hints = typing.get_type_hints(container)
        if attr_name not in hints:
            return
        hint = hints[attr_name]
        lines += [
            '',
            ':type: {}'.format(format_annotation(hint)),
            '',
        ]
        return

    if isinstance(obj, property):
        obj = obj.fget

    if callable(obj):
        if what in ('class', 'exception'):
            obj = getattr(obj, '__init__')

        obj = inspect.unwrap(obj)
        try:
            type_hints = typing.get_type_hints(obj)
        except (AttributeError, TypeError) as e:
            import traceback
            traceback.print_exc()
            print(obj)
            print(obj.__annotations__)
            # Introspecting a slot wrapper will raise TypeError
            return

        # If using autoclass_content = 'both', we will be called twice for the __init__ method
        if getattr(obj, '__sphinx_autodoc_future_annotations_seen__', False):
            return
        try:
            setattr(obj, '__sphinx_autodoc_future_annotations_seen__', True)
        except AttributeError:
            # Cannot set the attribute on a slot wrapper
            return

        for argname, annotation in type_hints.items():
            formatted_annotation = format_annotation(annotation)

            if argname == 'return':
                if what in ('class', 'exception'):
                    # Don't add return type None from __init__()
                    continue

                insert = True
                for line in lines:
                    if line.startswith(':rtype:'):
                        insert_index = False
                        break
                if insert:
                    lines.extend([
                        '',
                        ':rtype: {}'.format(formatted_annotation),
                        '',
                    ])

            else:
                insert = True
                for line in lines:
                    if re.match(r':(type|param\s+\S+)\s+{}:'.format(argname), line):
                        insert = False
                        break
                if insert:
                    lines.extend([
                        '',
                        ':type {}: {}'.format(argname, formatted_annotation),
                        '',
                    ])

                    # Insert an empty :param: tag for the parameter so that the type is shown in the docs
                    for line in lines:
                        if re.match(r':param\s+{}:'.format(argname), line):
                            insert = False
                            break
                    if insert:
                        lines.extend([
                            '',
                            ':param {}:'.format(argname),
                            '',
                        ])


def flatten_attribute(node):
    if isinstance(node, ast.Name):
        return node.id
    elif isinstance(node, ast.Attribute):
        left = flatten_attribute(node.value)
        if left is None:
            return None
        else:
            return '{}.{}'.format(left, node.attr)
    else:
        return None


def get_attribute(obj, name):
    if '.' in name:
        parts = name.split('.', maxsplit=1)
        return get_attribute(getattr(obj, parts[0]), parts[1])
    else:
        return getattr(obj, name)


def load_type_checking_imports(mod):
    mod_ast = ast.parse(open(mod.__spec__.origin).read())

    for node in mod_ast.body:
        if not isinstance(node, ast.If):
            continue
        if not isinstance(node.test, ast.Attribute):
            continue
        if node.test.attr != 'TYPE_CHECKING':
            continue
        attr_mod = flatten_attribute(node.test.value)
        if attr_mod is None:
            continue
        if get_attribute(mod, attr_mod) is not typing:
            continue
        for line in node.body:
            exec(astor.to_source(line), mod.__dict__)


def setup(app):
    app.connect('autodoc-process-signature', process_signature)
    app.connect('autodoc-process-docstring', process_docstring)

    import_module_original = sphinx.ext.autodoc.importer.import_module

    def import_module(modname, warningiserror=False):
        mod = import_module_original(modname, warningiserror=warningiserror)
        load_type_checking_imports(mod)
        return mod

    sphinx.ext.autodoc.importer.import_module = import_module

    return dict(parallel_read_safe=True)
