from __future__ import print_function, absolute_import

# -*- coding: utf-8 -*-
__author__ = "perfguru87@gmail.com"
__copyright__ = "Copyright 2018, The PerfTracker project"
__license__ = "MIT"


import citizenshell
import logging
from perftrackerlib.helpers.decorators import cached_property
from functools import wraps


def os_is_in(_lambda, def_val, *os_args):
    def wrapper(f):
        @wraps(f)
        def wrapped(self, *f_args, **f_kwargs):
            os = self.os_info.family
            if os in os_args:
                return f(self, *f_args, **f_kwargs)
            else:
                logging.warning("the %s.%s function is not implemented for OS: %s" % (self.__class__.__name__, f.__name__, os)) 
                return def_val
        return wrapped
    return wrapper


class ShellError(Exception):
    pass


class Os:
    def __init__(self, shell):
        assert isinstance(shell, Shell)
        self._shell = shell
        self._family = None
        self._version = None
        self._hostname = ''
        self._inited = False

    @cached_property
    def family(self):
        self._init()
        return self._family

    @cached_property
    def version(self):
        self._init()
        return self._version

    @cached_property
    def hostname(self):
        family = self.os_info.family
        f = self._shell.execute_fetch_one

        if family in ("Linux", "Darwin"):
            return f("hostname")
        
        logging.warning("os.hostname: %s OS is not supported" % str(family))
            
        self._init()
        return self._hostname

    def _init(self):
        if self._inited:
            return

        f = self._shell.execute

        status, out, _ = f("python -c 'from __future__ import print_function; import platform; print(platform.platform())'")
        self._version = out.strip()
        if self._version.startswith("Linux"):
            self._family = "Linux"
            self._hostname = f("hostname")
        elif self._version.startswith("Darwin"):
            self._family = "Darwin"
        elif self._version.startswith("Windows"):
            self._family = "Windows"
        else:
            raise ShellError("%s: can't recognize the OS family" % (str(self._shell)))

        self._inited = True


class Hw:
    def __init__(self, shell, os_info=None):
        assert isinstance(shell, Shell)
        self._shell = shell
        self._os_info = os_info

    @cached_property
    @os_is_in('', "Linux", "Darwin")
    def uuid(self):
        if self.os_info.family == "Linux":
            return self._shell.execute_fetch_one("cat /sys/class/dmi/id/product_uuid")
        elif self.os_info.family == "Darwin":
            return self._shell.execute_fetch_one("ioreg -rd1 -c IOPlatformExpertDevice | grep IOPlatformUUID | cut -d\"\\\"\" -f 4")

        raise RuntimeError("Never happens")

    @cached_property
    @os_is_in('', "Linux")
    def serial(self):
        if self.os_info.family == "Linux":
            return self._shell.execute_fetch_one("cat /sys/class/dmi/id/product_serial")

        raise RuntimeError("Never happens")

    @cached_property
    @os_is_in('', "Linux")
    def vendor(self):
        if self.os_info.family == "Linux":
            return self._shell.execute_fetch_one("cat /sys/class/dmi/id/sys_vendor")

        raise RuntimeError("Never happens")

    @cached_property
    @os_is_in('', "Linux")
    def model(self):
        if self.os_info.family == "Linux":
            return self._shell.execute_fetch_one("cat /sys/class/dmi/id/sys_vendor")

        raise RuntimeError("Never happens")

    @cached_property
    @os_is_in('', "Linux")
    def cpu_model(self):
        if self.os_info.family == "Linux":
            return self._shell.execute_fetch_one("cat /proc/cpuinfo | grep 'model name' | head -n 1 | cut -d':' -f 2")

        raise RuntimeError("Never happens")

    @cached_property
    @os_is_in(0.0, "Linux")
    def cpu_freq(self):
        if self.os_info.family == "Linux":
            return self._shell.execute_fetch_one("cat /proc/cpuinfo | grep 'cpu MHz' | head -n 1 | cut -d':' -f 2", float)

        raise RuntimeError("Never happens")

    @cached_property
    @os_is_in(0, "Linux")
    def cpu_count(self):
        if self.os_info.family == "Linux":
            return self._shell.execute_fetch_one("cat /proc/cpuinfo | grep processor | wc -l", float)

        raise RuntimeError("Never happens")

    @cached_property
    @os_is_in(0, "Linux")
    def ram_kb(self):
        if self.os_info.family == "Linux":
            return self._shell.execute_fetch_one("cat /proc/cpuinfo | grep processor | wc -l", float)

        raise RuntimeError("Never happens")

    @cached_property
    def os_info(self):
        return Os(self._shell) if self._os_info is None else self._os_info


class Shell:
    def __init__(self, shell):
        assert isinstance(shell, citizenshell.LocalShell) or isinstance(shell, citizenshell.SecureShell)
        self.shell = shell
        self._hw_info = None
        self._os_info = None

    @cached_property
    def hw_info(self):
        return Hw(self, self.os_info)

    @cached_property
    def os_info(self):
        return Os(self)

    def __str__(self):
        if isinstance(self.shell, citizenshell.LocalShell):
            return "localhost"
        if isinstance(self.shell, citizenshell.SecureShell):
            return self.shell._hostname
        return str(self.shell)

    def _debug(self, msg):
        print(msg)
        logging.debug("%s: %s" % (str(self), msg))

    def execute(self, cmdline, raise_exc=True):
        self._debug("%s ..." % cmdline)
        ret = self.shell(cmdline)
        if ret.exit_code():
            msg = "ERROR: %s: %s, exit status: %d\n%s" % (str(self), cmdline, ret.exit_code(), ret.stderr())
            if raise_exc:
                raise RuntimeException(msg)
            self._debug(msg)

        return ret.exit_code(), "\n".join(ret.stdout()), "\n".join(ret.stderr())

    def execute_fetch_one(self, cmdline, type=None):
        status, out, err = self.execute(cmdline, raise_exc=None)
        if status:
            ret = None
        else:
            ret = out.strip()
        if type:
            try:
                return type(ret)
            except ValueError:
                self._debug("ERROR: can't cast '%s' to '%s'" % (str(ret), str(type)))
                return type()
        return ret


##############################################################################
# Autotests
##############################################################################


def _coverage():
    logging.basicConfig(level=logging.DEBUG)

    sh = Shell(citizenshell.LocalShell())

    print("os family: ", sh.os_info.family)
    print("os version:", sh.os_info.version)
    print("hostname:  ", sh.os_info.hostname)
    print("uuid:      ", sh.hw_info.uuid)
    print("uuid:      ", sh.hw_info.uuid)
    print("serial:    ", sh.hw_info.serial)
    print("vendor:    ", sh.hw_info.vendor)
    print("model:     ", sh.hw_info.model)
    print("cpu_model: ", sh.hw_info.cpu_model)
    print("cpu_freq:  ", sh.hw_info.cpu_freq)
    print("cpu_count: ", sh.hw_info.cpu_count)
    print("ram_kb:    ", sh.hw_info.ram_kb)


if __name__ == "__main__":
    _coverage()
