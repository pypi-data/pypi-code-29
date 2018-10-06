#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import subprocess
import psutil
from public import public


class Response:
    args = None
    code = None
    out = None
    err = None
    pid = None

    def __init__(self, args, code, out, err, pid, **kwargs):
        self.args = args
        self.out = out.rstrip()
        self.err = err.rstrip()
        self.code = code
        self.pid = pid

    def _raise(self):
        if self.pid and not self.ok:
            output = self.err
            if not self.err:
                output = self.out
            if output:
                raise OSError("%s exited with code %s\n%s" % (self.args, self.code, output))
            raise OSError("%s exited with code %s" % (self.args, self.code))
        return self

    @property
    def text(self):
        return "\n".join(filter(None, [self.out, self.err]))

    @property
    def ok(self):
        return self.code == 0

    @property
    def running(self):
        zombie = psutil.Process(self.pid).status() == psutil.STATUS_ZOMBIE
        return not zombie and os.system("kill -0 %s &> /dev/null" % self.pid) == 0

    def __bool__(self):
        return self.ok

    def __non_zero__(self):
        return self.ok

    def __str__(self):
        return "<Response code=%s>" % self.code


class Command:
    custom_popen_kwargs = None

    def __init__(self, **popen_kwargs):
        self.custom_popen_kwargs = dict(popen_kwargs)

    @property
    def _default_popen_kwargs(self):
        return {
            'env': os.environ.copy(),
            'stdin': subprocess.PIPE,
            'stdout': subprocess.PIPE,
            'stderr': subprocess.PIPE,
            'shell': False,
            'universal_newlines': True,
            'bufsize': 0
        }

    @property
    def popen_kwargs(self):
        kwargs = self._default_popen_kwargs
        kwargs.update(self.custom_popen_kwargs)
        return kwargs

    def run(self, args, cwd=None, env=None, background=False):
        args = list(map(str, args))
        kwargs = self.popen_kwargs
        kwargs["cwd"] = cwd
        if env:
            kwargs["env"].update(env)
        if background:
            # prevent process from stdout/stderr error
            DEVNULL = open(os.devnull, 'wb')
            kwargs["stdout"] = DEVNULL
            kwargs["stderr"] = DEVNULL
        process = subprocess.Popen(args, **kwargs)
        if not background:
            stdoutdata, stderrdata = process.communicate()
            code = process.returncode
        else:
            code, stdoutdata, stderrdata = None, "", ""
        pid = process.pid
        response = Response(args=args, code=code, out=stdoutdata, err=stderrdata, pid=pid)
        return response


@public
def run(args, cwd=None, env=None, background=False):
    return Command().run(args, cwd=cwd, env=env, background=background)
