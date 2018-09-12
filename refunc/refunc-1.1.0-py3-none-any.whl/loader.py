# -*- coding: utf-8 -*-

import sys
import traceback

import six

__all__ = ['CustomError', 'CustomException', 'compile_func']


class CustomError(object):
    def __init__(self):
        self.stacks = []
        self.msg = None
        self.exc_type = None
        self.exc_val = None
        self.exc_tb = None
        self.max_exc_var_len = 160

    def set_exc(self, exc_type, exc_val, exc_tb):
        self.exc_type = exc_type
        self.exc_val = exc_val
        self.exc_tb = exc_tb

    def set_msg(self, msg):
        self.msg = msg

    def add_stack_info(self, filename, lineno, func_name, code, local_variables={}):
        self.stacks.append((filename, lineno, func_name, code, local_variables))

    @property
    def stacks_length(self):
        return len(self.stacks)

    def __repr__(self):
        if len(self.stacks) == 0:
            return self.msg

        def _repr(v):
            try:
                var_str = repr(v)
                if len(var_str) > self.max_exc_var_len:
                    var_str = var_str[: self.max_exc_var_len] + " ..."
                return var_str
            except Exception:
                return 'UNREPRESENTABLE VALUE'

        content = ["Traceback (most recent call last):"]
        for filename, lineno, func_name, code, local_variables in self.stacks:
            content.append('  File %s, line %s in %s' % (filename, lineno, func_name))
            content.append('    %s' % (code,))
            for k, v in local_variables.items():
                content.append('    --> %s = %s' % (k, _repr(v)))
            content.append('')
        content.append("%s: %s" % (self.exc_type.__name__, self.msg))

        return "\n".join(content)


class CustomException(Exception):
    def __init__(self, error):
        self.error = error


def create_base_scope():
    import copy

    from . import func_scope

    scope = copy.copy(func_scope.__dict__)
    # scope.update({
    #     "logger": user_log,
    #     "print": user_print,
    # })

    return scope


def compile_func(source_code, scope, funcpath):
    error = None
    try:
        funcpath = funcpath if funcpath else 'refunc-inst.py'
        code = compile(source_code, funcpath, 'exec')
        scope = scope if scope is not None else {}
        g = create_base_scope()
        if '__name__' in scope:
            g.pop('__name__')
        if '__file__' in scope:
            g.pop('__file__', '')
        scope.update(g)
        six.exec_(code, scope)
        return scope
    except Exception as e:
        exc_type, exc_val, exc_tb = sys.exc_info()
        try:
            msg = str(exc_val)
        except Exception:
            msg = ""

        error = CustomError()
        error.set_msg(msg)
        error.set_exc(exc_type, exc_val, exc_tb)
        stackinfos = list(traceback.extract_tb(exc_tb))

        if isinstance(e, (SyntaxError, IndentationError)):
            error.add_stack_info(exc_val.filename, exc_val.lineno, "", exc_val.text)
        else:
            for item in stackinfos:
                filename, code = item[0], item[-1]
                if funcpath == filename:
                    error.add_stack_info(*item)
            # avoid empty stack
            if error.stacks_length == 0:
                error.add_stack_info(*item)

    if error:
        raise CustomException(error)
